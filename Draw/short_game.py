"""
Short game:

You have 5 steps in the chamber and in each step you can win a box or nothing.

Boxes are in various colors:
green - 75%
orange - 20%
violet - 4%
gold - 1%

There is 40% chance of finding nothing and 60% chance of finding a box.

Amount of gold in boxes:
green - 1000
orange - 4000
violet - 9000
gold - 16000
"""

import random
from enum import Enum

def FindApproximateValue(value):
    lowestValue = value - 0.1 * value
    highestValue = value + 0.1 * value
    return random.randint(lowestValue, highestValue)

Event = Enum("Event", ["Chest", "Empty"])

EventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }
EventList = list(EventDictionary.keys())
EventProbability = list(EventDictionary.values())

Colours = Enum("Colours", {"Green": "green",
                           "Orange": "orange",
                           "Purple": "purple",
                           "Gold": "gold"}
               )

ColoursDictionary = {
                    Colours.Green  : 0.75, 
                    Colours.Orange : 0.2, 
                    Colours.Purple : 0.04, 
                    Colours.Gold : 0.01, 
                    }
ColourList = list(ColoursDictionary.keys())
ColourProbability = list(ColoursDictionary.values())

Rewards = {
            ColourList[reward]: (reward + 1) * (reward + 1) * 1000
            for reward in range(len(ColourList))
          }

GameLength = 5
goldAcquired = 0

print("""Welcome in my simple game 'the chamber', you have 5 steps to make
How much gold can you acquire?""")

while GameLength > 0:
    gamerAnswer = input("Do you want to move forward? ")
    if (gamerAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(EventList, EventProbability)[0]
        if (drawnEvent == Event.Chest):
            drawnColour = random.choices(ColourList, ColourProbability)[0]
            print("You've drawn a", drawnColour.value, "chest")
            gamerReward = FindApproximateValue(Rewards[drawnColour])
            goldAcquired = goldAcquired + gamerReward
        elif (drawnEvent == Event.Empty):
            print("You've drawn nothing, you're so unlucky")
        
    else:
        print("You can go just straight")
        continue

    GameLength -= 1

print("Congratulatios, you've acquired: ", goldAcquired)
