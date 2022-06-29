"""
indent=4,
sort_keys=True
"""

import json

film = {
    "title" : "Dawno temu",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Sylwia Kołodziej",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4)

with open("sample.json", encoding="UTF-8") as file:
    result = json.load(file)


import pprint
pprint.pprint(result)
