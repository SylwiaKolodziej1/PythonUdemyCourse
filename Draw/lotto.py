import random

container = []
x = 0

while x < 6:
    random.randint(0, 50)
    if random.randint(0, 50) in container:
        continue
    else:
        container.append(random.randint(0, 50))
    x += 1
    
print(container)

