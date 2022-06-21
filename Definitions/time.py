import time

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

def Function_Performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

print(Sum_To(x))
print(Function_Performance(Sum_To, x, 25), "- Time of running function 1")
print(Function_Performance(Sum_To2, x), "- Time of running function 2")
