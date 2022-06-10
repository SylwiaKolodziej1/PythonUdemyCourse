result = 0

i = 0

while i < 3:
    x = int(input("Give a positive number: "))
    if (x > 0):
        result += x
    else:
        print("A number is not positive!")
        continue
    print("Actual result:", result)
    i += 1
