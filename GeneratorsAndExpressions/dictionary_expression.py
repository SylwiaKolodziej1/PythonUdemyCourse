numbers = [1, 2, 3, 4, 5, 6]

multipliedNumbers = {
    number : number ** 2
    for number in numbers
}


names = {"Sylwia", "Ola", "Artur", "Piotr", "Gosia"}

namesLength = {
    name : len(name)
    for name in names
}


celcius = {"t1": -20, "t2": -15, "t3": 0, "t4": 12}

farenheit = {
    key : celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if (celcius > -5)
    if (celcius < 20)
}


