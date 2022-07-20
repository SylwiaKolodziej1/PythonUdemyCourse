import requests
import json
import webbrowser
from pprint import pprint

headers = {
    "x-api-key" : "f27358d5-fbca-4fdc-8689-added8369c27"
}

def get_json_content(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Inappropriate format", response.text)
    else:
        return content
    
def get_favourite_cats(userID):
    params = {
        "sub_id" : userID
    }
    r = requests.get("https://api.thecatapi.com/v1/favourites", params, headers=headers)
    return get_json_content(r)

def get_random_cat():
    r = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)
    return get_json_content(r)[0]

def add_favourite_cat(catId, userId):
    catData = {
        "sub_id" : userId,
        "image_id" : catId
    }
    r = requests.post("https://api.thecatapi.com/v1/favourites/", json = catData, headers=headers)
    return get_json_content(r)

def remove_favourite_cat(userId, favouriteCatId):
    r = requests.delete("https://api.thecatapi.com/v1/favourites/"+favouriteCatId, headers=headers)
    return get_json_content(r)
    

print("Give your login and password")

userId = "sk2001"
name = "Sylwia"

favouriteCats = get_favourite_cats(userId)
print("Hello", name, "let me show you your favourite cats ", favouriteCats)
randomCat = get_random_cat()
print("You've drawn a random cat", randomCat["url"])

addToFavourites = input("Do you want to add a cat to your Favourites? Y/N ")

if(addToFavourites.upper() == "Y"):
    add_favourite_cat(randomCat["id"], userId)
else:
    print("The cat is sad, maybe next time")

favouriteCatsById = {
    favouriteCat["id"] : favouriteCat["image"]["url"]
    for favouriteCat in favouriteCats
}

pprint(favouriteCatsById)
favouriteCatId = input("Do you want to remove a cat from Favourites? If so, give the cat's id: ")

print(remove_favourite_cat(userId, favouriteCatId))
    


