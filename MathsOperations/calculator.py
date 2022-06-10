print("""Choose what you want to do
* - multiply
/ - divide
+ - add
- - substract
^ - compound
% - remainder""")
x = input()

print("Give first number: ")
a = int(input())

print("Give second number: ")
b = int(input())

if (x == "*"):
    print("Result of multiplying is:", a * b)
elif (x == "/"):
    if (b == 0):
        print("You cannot divide by 0!")
    else:
        print("Result of dividing is:", a / b)
elif (x == "+"):
    print("Result of adding is:", a + b)
elif (x == "-"):
    print("Result of substraction is:", a - b)
elif (x == "^"):
    print("Result of exponentation is:", a ** b)
elif (x == "%"):
    print("Rest from dividing:", a % b)
else:
    print("You haven't chosen appropriate sign!")
    
