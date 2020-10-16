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
import requests

def read_file_contents(filename):
    # open file, read and close
    with open(filename) as file:
        contents = file.read()
        return contents

def apply(function, value):
    return function(value)

def format_url(artist_name):
    return "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&indexpageids&rvsection=0&titles=" + artist_name

def extract_dates(wiki_data):
    pageid = wiki_data["query"]["pageids"][0]
    text = wiki_data["query"]["pages"][pageid]["revisions"][0]["*"]
    death_index = text.index("{{death date and age") + 28
    death_end = text.index("}}", death_index)
    return text[death_index:death_end]

def get_first(values):
    return values[0]

def process_name(artist_name):
    *first_name, last_name = apply(str.split, artist_name)
    first_letters = list(map(get_first, first_name))
    print(first_letters)

contents = read_file_contents("Functional_Programming/artist.txt")
names = apply(str.splitlines, contents)

url = format_url(names[0])
response = apply(requests.get, url)
wikidata = apply(requests.Response.json, response)

print(extract_dates(wikidata))

print(process_name(names[1]))