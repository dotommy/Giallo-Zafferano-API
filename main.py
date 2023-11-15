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
    
    titles = title_recipes(number_page, number_meals_array)
    links = href_recipes(number_page, number_meals_array)
    data = []

    for i, (title, link) in enumerate(zip(titles, links)):
        product = {
                "id": i,
                "name": title,
                "link": link
        }
        data.append(product)

    return json.dumps(data, indent=2)


def description_recipes(number_page, number_meals_array, id_recipes):
    number_meals_array = number_meals_array
    number_page = number_page
    if (isinstance(number_meals_array, int) and isinstance(number_page, int)) and isinstance(id_recipes, int):
        recipes_link = href_recipes(number_page, number_meals_array)
        select_recipe = recipes_link[id_recipes]
        url = select_recipe
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        description = soup.find('div', class_='gz-page').find('main', class_='gz-wrapper').find('div', class_='gz-inner').find('div', class_='gz-content-recipe').find('p').get_text()


        return description

    else:
        return "Error variable is not int"
    
def type_recipes(number_page, number_meals_array, id_recipes):
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
            options_featured.append(data.strip('\n'))

        

        return options_featured

        
    else:
        return "Error variable is not int"

print(type_recipes(1, 0, 5))

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



        

