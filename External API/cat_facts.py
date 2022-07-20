import json
import webbrowser
import requests
from pprint import pprint

params = {
    "amount" : 10
}

r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Inappropriate format")
else:
    for cat in content:
        pprint(cat["text"])
