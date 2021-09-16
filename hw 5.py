#Question 1
#you're having coffee/tea/beverage of your choice with a friend that is learning to program in
#Python. They're curious about why they would use pip.
#Explain what pip is and one benefit of using pip.

#is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.
# provides more sets of tools and libraries that speed up the development process of a Python application.

#2. This program should save my data to a file, but it doesn't work when I run it. What is the problem
#and how do I fix it?
#move the poem line inside the program and cahnge the 'r' to 'w'

with open('poem.txt', 'w+') as poem_file:
    poem = 'I like Python and I am not very good at poems'
    poem_file.write(poem)

#Question 3
#In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
#retrieve multiple Pokemon and save their names and moves to a file.
#Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
#Pokemon. Save their names and moves into a file called 'pokemon.txt'

import random
import requests
import re

def get_six_pokemon_names_and_moves():
    # create random pokemon ids
    pokemon_ids = random.sample(range(1, 898), 6)
    # create string for pokemon moves
    p_moves = ""
    # create string for all pokemon data from the txt file
    pokemon_data = ""

    for id_no in pokemon_ids:
        url = f'https://pokeapi.co/api/v2/pokemon/{id_no}/'
        response = requests.get(url)
        # print(response)
        pokemon = response.json()

        pokemon_name = pokemon['name']
        # print(pokemon_name)

        moves = pokemon['moves']
        # print(moves)