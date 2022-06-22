"""
random()                    [0,1)

uniform(2.5, 10.0)          [2.5, 10.0)

randrange(10)               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
randrange(0, 15, 2)         [0, 2, 4..., 14]

randint(0, 4)               [0, 1, 2, 3, 4]

"""


import random

def will_weapon_hit(percentageChance):
    if random.uniform(0,100) < percentageChance:
        return "Hit"
    else:
        return "Not hit"

x = 0

listHit = []

while x < 100:
    x += 1
    listHit.append(will_weapon_hit(50))

from collections import Counter

dictionaryHit = Counter(listHit)
print(dictionaryHit)
