x = int(input("Give a number to sum all numbers from 1 to the given number: "))
sum = 0

def Sum_To(number):
    sum = 0  
    for number in range(1, x+1):
        sum = sum + number
    return sum

def Sum_To2(number):
    sum = (1 + x) / 2 * x
    return sum
    

print(Sum_To(x))
print(Sum_To2(x))

