number = 41
x = 0

while (x != number):
    x = int(input("Guess the number: "))

    if (x > number):
        print("The number is smaller than", x,"try again")
    elif (x < number):
        print("The number is bigger than", x,"try again")
    elif (x == number):
        print("Bravo! You guessed the number!")
