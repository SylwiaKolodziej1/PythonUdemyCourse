import json
import webbrowser
import requests
from pprint import pprint

params = {
    "api_key" : "3b931c538a5f9e84071bb0427b3c1cf2331cf6e3",
    "country" : "pl",
    "year" : 2022,
    "month" : 12
}

r = requests.get("https://calendarific.com/api/v2/holidays", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Inappropriate format")
else:
    pprint(content)
