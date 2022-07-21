def generate_even_numbers():
    for item in range(400):
        if (item % 2) == 0:
            yield item

a = generate_even_numbers()

def generate_10_numbers():
    x = 0
    while x < 10:
        yield x
        x += 1

print(list(generate_10_numbers()))
