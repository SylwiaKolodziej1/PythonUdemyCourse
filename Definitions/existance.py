import time

def Function_Performance(func, how_many_times = 1, *arg):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

a = int(input("Give a number: "))

def is_element_in(a, container):
    if a in container:
        return True
    else:
        return False


print(Function_Performance(is_element_in, 300, a, setContainer))
print(Function_Performance(is_element_in, 300, a, listContainer))
