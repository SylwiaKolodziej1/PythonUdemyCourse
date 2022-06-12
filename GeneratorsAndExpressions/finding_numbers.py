#Find numbers from 100 to 470 (included) which are dividable by 7 but undividable by 5

numbersGenerator = (
    number
    for number in range(100, 471)
    if (number % 7 == 0 and number % 5 != 0)
)

print(set(numbersGenerator))

#2nd soluction

numbers = [number
    for number in range(100, 471)
    if (number % 7 == 0 and number % 5 != 0)
]
    
