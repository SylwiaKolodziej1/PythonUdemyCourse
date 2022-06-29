import random

gameAward = ["green", "purple", "silver", "legendary"]

from collections import Counter

print(Counter(random.choices(gameAward, [80, 15, 4, 1], k = 100)))
              
