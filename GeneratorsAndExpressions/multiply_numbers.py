def numbers_multiplied_generator():
    number = 0
    while True:
        number = yield number * number

generatedNumbers = []

numberGenerator = numbers_multiplied_generator()

numberGenerator.send(None)

for i in range(20):
    generatedNumbers.append(numberGenerator.send(i))


for i in range(30, 50):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)
