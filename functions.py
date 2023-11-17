from bs4 import BeautifulSoup
import requests
import json


def title_recipes(number_page, number_meals_array):
    number_meals_array = number_meals_array
    number_page = number_page
    if isinstance(number_meals_array, int) and isinstance(number_page, int):
        meals_array=["Antipasti","Primi","Secondi-piatti","Dolci-e-Desserts","Lievitati","Piatti-Unici"]
        url = f'https://www.giallozafferano.it/ricette-cat/page{number_page}/{meals_array[number_meals_array]}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        gzcards = soup.find_all('article', class_="gz-card")

        title_gzcards = []

        for gzcard in gzcards:
                # Trova tutti i link all'interno di ciascun elemento <article>
                a_att = gzcard.find('a').get("title")
                title_gzcards.append(a_att)
        
        return title_gzcards
    else:
        return "Error variable is not int"


def href_recipes(number_page, number_meals_array):
    number_meals_array = number_meals_array
    number_page = number_page
    if isinstance(number_meals_array, int) and isinstance(number_page, int):
        meals_array=["Antipasti","Primi","Secondi-piatti","Dolci-e-Desserts","Lievitati","Piatti-Unici"]
        url = f'https://www.giallozafferano.it/ricette-cat/page{number_page}/{meals_array[number_meals_array]}/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        gzcards = soup.find_all('article', class_="gz-card")

        title_gzcards = []

        for gzcard in gzcards:
                # Trova tutti i link all'interno di ciascun elemento <article>
                a_att = gzcard.find('a').get("href")
                title_gzcards.append(a_att)
        
        return title_gzcards
    else:
        return "Error variable is not int"



def json_title_link(number_page, number_meals_array):
    if isinstance(number_meals_array, int) and isinstance(number_page, int):
        titles = title_recipes(number_page, number_meals_array)
        links = href_recipes(number_page, number_meals_array)
        data = []
        if len(titles) == len(links):
            for i, (title, link) in enumerate(zip(titles, links)):
                product = {
                        "id": i,
                        "name": title,
                        "link": link
                }
                data.append(product)

            return json.dumps(data, indent=2)
        else:
            return 'INTERNAL ERROR'
    return "Error variable is not int"
    


# ---------END SCRAPING HOMEPAGE-------------------- #

def title_recipes_only(number_page, number_meals_array, id_recipes):
    # ----Function for scraping description or presentation in recipe page
    number_meals_array = number_meals_array
    number_page = number_page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        description = soup.find('main', class_='gz-wrapper').find('div', class_='gz-toprecipe').find('div', class_='gz-title-content').find('h1', class_='gz-title-recipe').get_text()


        return description

    else:
        return "Error variable is not int"

def description_recipes(number_page, number_meals_array, id_recipes):
    # ----Function for scraping description or presentation in recipe page
    number_meals_array = number_meals_array
    number_page = number_page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        description = soup.find('main', class_='gz-wrapper').find('div', class_='gz-innerwrapper').find('div', class_='gz-inner').find('div', class_='gz-content-recipe').find('p').get_text()


        return description

    else:
        return "Error variable is not int"



def  nutritional_table(number_page, number_meals_array, id_recipes):
    # ----Function for scraping nutritional table in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        raw_nutritional_names = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-list-macros').find('ul').find_all('li')
        nutritional_names = []
        for raw_nutritional_name in raw_nutritional_names:
            n_datas = raw_nutritional_name.find('span', class_='gz-list-macros-name').get_text().strip('\xa0')
            nutritional_names.append(n_datas)

        raw_nutritional_units = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-list-macros').find('ul').find_all('li')
        nutritional_units = []
        for raw_nutritional_unit in raw_nutritional_units:
            n_datas = raw_nutritional_unit.find('span', class_='gz-list-macros-unit').get_text()
            nutritional_units.append(n_datas)

        raw_nutritional_values = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-list-macros').find('ul').find_all('li')
        nutritional_values = []
        for raw_nutritional_value in raw_nutritional_values:
            n_datas = raw_nutritional_value.find('span', class_='gz-list-macros-value').get_text()
            nutritional_values.append(n_datas)

        return nutritional_names, nutritional_units, nutritional_values
    else:
        return "Error variable is not int"
    


def kcal_recipes(number_page, number_meals_array, id_recipes):
    # ----Function for scraping kcal in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        kcal_data = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-featured-data-recipe').find('div',class_='gz-calories-portion-top').find('div',class_='gz-text-calories').find('div',class_='gz-text-calories-total').get_text()
                
        return kcal_data
    else:
        return "Error variable is not int"
    


def type_recipes(number_page, number_meals_array, id_recipes):
    # ----Function for scraping type in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        featured_datas = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-featured-data-recipe').find('ul').find_all('li')


        options_featured = []
        for featured_data in featured_datas:
            data = featured_data.get_text()
            options_featured.append(data.lstrip(' ').replace('\xa0', '').replace('\n', ' '))

        

        return options_featured

        
    else:
        return "Error variable is not int"


def recipe_details(number_page, number_meals_array, id_recipes):
    # ----Function for scraping recipe in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_recipe_details = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-topstrip-recipe').find('div', class_='gz-featured-data-cnt').find('div', class_='gz-list-featured-data').find('ul').find_all('li')
        
        recipe_name = []
        recipe_details = []

        for raw_recipe_detail in raw_recipe_details:
            strong_r_data = raw_recipe_detail.find('span', class_="gz-name-featured-data").find('strong').get_text()
            recipe_name.append(strong_r_data)
            r_data = raw_recipe_detail.find('span', class_="gz-name-featured-data").find(string=True, recursive=False).get_text().rstrip().rstrip(':')
            recipe_details.append(r_data)
        

        return recipe_details, recipe_name



def  ingredients_recipes(number_page, number_meals_array, id_recipes):
    # ----Function for scraping ingredient in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        raw_dl_tags =  soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-ingredients').find_all('dl', class_='gz-list-ingredients')

        ingredients_names = []
        ingredients = []

        for raw_dl_tag in raw_dl_tags:
            title = raw_dl_tag.find('dt').get_text().strip()
            ingredients_names.append(title)
            dd_ingredients = raw_dl_tag.find_all('dd')
            for dd_ingredient in dd_ingredients:
                a_ingredient = dd_ingredient.find('a').get_text()
                span_ingredient = dd_ingredient.find('span').get_text().lstrip(r'\n+').rstrip(r'\n+').replace(' ', '').replace('\n', ' ').replace('\t', '')
                ingredient = a_ingredient + span_ingredient
                ingredients.append(ingredient)
            ingredients_names.append(ingredients)

        return ingredients_names
    

    else:
        return "Error variable is not int"
    

def  preparation_recipes(number_page, number_meals_array, id_recipes):
    # ----Function for scraping preparation in recipe page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        gz_content_recipes =  soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-innerwrapper').find('div', class_='gz-content').find('div', class_='gz-inner').find_all('div', class_='gz-content-recipe')
        step = []
        for gz_content_recipe in gz_content_recipes:
            if gz_content_recipe .find('div', class_='gz-content-recipe-step'):
                gz_content_recipe_steps = gz_content_recipe.find_all('div', class_='gz-content-recipe-step')
                for gz_content_recipe_step in gz_content_recipe_steps:
                    p_steps = gz_content_recipe_step.find_all('p')
                    for p_step in p_steps:
                        steps = p_step.get_text().lstrip(r'\n+').replace('\n', '')
                        step.append(steps)
        return step                    

        
        
    
    else:
        return "Error variable is not int"


def json_recipes(number_page, number_meals_array, id_recipes):
    json_recipes_ = {}

    title_recipes_ = title_recipes_only(number_page, number_meals_array, id_recipes)
    json_recipes_['title'] = title_recipes_

    description_recipes_ = description_recipes(number_page, number_meals_array, id_recipes)
    json_recipes_['description'] = description_recipes_

    nutritional_table_ = nutritional_table(number_page, number_meals_array, id_recipes)
    names_nutritional_table_ = nutritional_table_[0]
    units_nutritional_table_ = nutritional_table_[1]
    values_nutritional_table_ = nutritional_table_[2]

 
    nutritional_data_json = {}
    i=0
    for name_nutritional_table, unit_nutritional_table, value_nutritional_table_ in zip(names_nutritional_table_, units_nutritional_table_, values_nutritional_table_):
        nutritional_data_json[name_nutritional_table+':'] = value_nutritional_table_ + ' ' + unit_nutritional_table
    json_recipes_['nutritional_table'] = nutritional_data_json

        
    ingredients_ = ingredients_recipes(number_page, number_meals_array, id_recipes)
    ingredients_json_1_ = {}
    ingredients_json_2_ = {}


    for ingredient_ in ingredients_:
        y = 0
        if isinstance(ingredient_, list):
            i= 0
            for ingredient_s_ in ingredient_:
                ingredients_json_2_[f"ingredient_id_{i}"] = ingredient_s_
                i= i+1
        else:
            ingredients_json_2_["ingredient_title"] = ingredient_

        
        ingredients_json_1_[f"title_id_{y}"] = ingredients_json_2_
        y = y+1
    json_recipes_['ingredients'] = ingredients_json_1_

    recipe_details_ = recipe_details(number_page, number_meals_array, id_recipes)

    name_recipe_details_ = recipe_details_[0]
    answers_recipe_details_ = recipe_details_[1]
    recipe_details_json_ = {}
    for name_recipe_details, answers_recipe_details in zip(name_recipe_details_, answers_recipe_details_):
        if answers_recipe_details == 'Nota':
            recipe_details_json_[answers_recipe_details] = name_recipe_details
        else:
            recipe_details_json_[name_recipe_details] = answers_recipe_details

    json_recipes_['recipe_details'] = recipe_details_json_

    preparation_recipes_ = preparation_recipes(number_page, number_meals_array, id_recipes)
    preparation_recipes_json_ = {}
    i = 1
    for preparation_recipe_ in preparation_recipes_:
        preparation_recipes_json_[f'step_{i}'] = preparation_recipe_
        i = i+1

    json_recipes_['recipes_steps'] = preparation_recipes_json_

    return json_recipes_



def create_json(titles, links):
    
    data = []

    for i, (title, link) in enumerate(zip(titles, links)):
        product = {
                "id": i,
                "name": title,
                "link": link
        }
        data.append(product)

    return json.dumps(data, indent=2)