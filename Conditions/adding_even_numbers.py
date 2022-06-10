result = 0

i = 0

while i < 3:
    x = int(input("Give a positive, even number: "))
    if (x % 2 == 0 and x > 0):
        result += x
    else:
        print("You've given inappropriate number, give a number again ")
        continue
    print("Actual result:", result)
    i += 1
        
