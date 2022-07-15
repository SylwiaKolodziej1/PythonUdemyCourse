import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
           try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
           except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1
                
    return completedTaskFrequencyByUser


def get_top_users(completedTaskFrequencyByUser):
    bestUsersID = []
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            bestUsersID.append(userId)
            
    return bestUsersID

def change_list_ito_conj(my_list, key="id"):
    conj = key + "="

    lastIteration = len(my_list)
    i = 0
    for item in my_list:
        i += 1
        if (i == lastIteration):
            conj += str(item)
        else:
            conj += str(item) + "&" + key + "="
            
    return conj

            
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Inappropriate format")
else:
    completedTaskFrequencyByUser = count_task_frequency(tasks)
    bestUsersID = get_top_users(completedTaskFrequencyByUser)
    
    
conj = change_list_ito_conj(bestUsersID, key="id")    
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conj)

users = r.json()
for user in users:
    print("The prize goes to", user["name"])
        
