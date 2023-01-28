import random
import requests
import os
from os.path import join, dirname 
from dotenv import load_dotenv
import json 

dotenv_path = join(dirname(__file__), 'spoon.env')
load_dotenv(dotenv_path)
spoon_key = os.environ['SPOON_KEY']

url = "https://api.spoonacular.com/recipes/complexSearch?query={}&apiKey={}".format("chicken", spoon_key)

response = requests.get(url)
results = response.json()
results_neat = json.dumps(results, indent = 2)
id = results["results"][0]["id"]

print (id)

url2 = "https://api.spoonacular.com/recipes/{}/information?&apiKey={}".format(id, spoon_key)

response = requests.get(url2)
results = response.json()
results_neat = json.dumps(results, indent = 2)

# print (results_neat)

title = results["title"]
summary = results["summary"]
ingredients = results ["extendedIngredients"]
items = []
for food in ingredients:
    items.append(food ["name"])
