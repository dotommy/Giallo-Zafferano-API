# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template
import functions
import json

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return render_template('index.html')

@app.route('/meal_<id_meal>/page_<id_page>')
# ‘/’ URL is bound with hello_world() function.
def recipe_list(id_meal, id_page):
    try:
        id_meal = int(id_meal)
        id_page = int(id_page)
    except ValueError:
        # Se la conversione fallisce, restituisci un errore HTTP 400 Bad Request
        return 'id is not int', 400

    list_ = functions.json_title_link(id_page, id_meal)
    return json.loads(list_)

@app.route('/meal_<id_meal>/page_<id_page>/recipe_<id_recipe>')
# ‘/’ URL is bound with hello_world() function.
def recipe(id_meal, id_page, id_recipe):
    try:
        id_meal = int(id_meal)
        id_page = int(id_page)
        id_recipe = int(id_recipe)
    except ValueError:
        # Se la conversione fallisce, restituisci un errore HTTP 400 Bad Request
        return 'id is not int', 400

    recipe_ = functions.json_recipes(id_page, id_meal, id_recipe)
    return recipe_

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
