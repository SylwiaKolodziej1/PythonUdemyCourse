"""

json.loads(jsonstring) - converts jsonstring to Python

json.load(filePointer) - loads json from file and as a result returns Python datas 
"""

import json

encodedRetrievedMovie = '{"title": "Dawno temu", "release_year": 1969, "won_oscar": true, "actors": ["Sylwia Kołodziej", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Alan Brave", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decodedMovie = json.loads(encodedRetrievedMovie, encoding="UTF-8")

with open("sample.json", encoding="UTF-8") as file:
    result = json.load(file)
