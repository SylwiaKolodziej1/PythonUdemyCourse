"""

json.dumps(data) - saves data in string form  json
json.dump(data, nameOfFileHandler, ensure_ascii=False) - saves data as a file

"""

import json

film = {
    "title" : "Dawno temu",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Sylwia Kołodziej", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Alan Brave",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedFilm = json.dumps(film, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)


