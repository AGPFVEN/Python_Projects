# A program to create labels to be used in a museum indexing system. Each artist needs a label in the format:
# 	FFFLLLLL-XX
# 		F     = First letters of each first name
# 		LLLLL = Up to 5 letters of last name
# 		XX    = Age at death
# 
#    https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&indexpageids&rvsection=0&titles={name}

#  For example:
#     Wassily Kandinsky
#     WKANDI-78

import datetime
import requests
import operator

from functools import reduce


def read_file_contents(filename):
    with open(filename) as file:
        contents = file.read()
        return contents


def apply(function, value):
    return function(value)


def format_url(artist_name):
    return "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&indexpageids&rvsection=0&titles=" + artist_name


def extract_dates(wiki_data):
    pageid = wiki_data["query"]["pageids"][0]
    text = wiki_data["query"]["pages"][pageid]["revisions"][0]["*"].lower()
    death_index = text.index("{{death date and age") + 28
    death_end = text.index("}}", death_index)
    date_string = text[death_index:death_end].strip("df").strip("=y").strip("=yes").strip("df").strip("mf").strip("|")
    born_string, _, death_string = date_string.replace("|", "-", 2).partition("|")

    born_date = datetime.datetime.strptime(born_string, "%Y-%m-%d")
    death_date = datetime.datetime.strptime(death_string, "%Y|%m|%d")
    return born_date, death_date


def get_first(values):
    return values[0]


def get_five(values):
    if len(values) < 5:
        return values
    else:
        return values[0:5]


def process_name(artist_name):
    *first_names, last_name = apply(str.split, artist_name)
    first_letters = list(map(get_first, first_names))
    last_letters = apply(get_five, last_name)
    return first_letters, last_letters


def stick_strings(strings):
    return "".join(strings)

def get_year(date):
    return date.days // 365

def create_lable(name):
    #Wikipedia API
    url = format_url(name)
    response = apply(requests.get, url)
    wiki_data = apply(requests.Response.json, response)
    born, died = extract_dates(wiki_data)

    #Calculate age at death 
    age = reduce(operator.sub, [born, died])
    age = apply(get_year, age)

    # Process names
    firsts, last = apply(process_name, name)
    label = reduce(operator.add, [stick_strings(firsts), last, "-", str(age)])
    label = apply(str.upper, label)
    return label

contents = read_file_contents("Functional_Programming/artist.txt")
names = apply(str.splitlines, contents)
labels = list(map(create_lable, names))

print(labels)
