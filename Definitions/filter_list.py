"How to filter lists using lambda"


my_list = [2, 5, 18, 23, 44, 72]

my_filtered_list = list(filter(lambda x: x % 2 == 0, my_list))

print(my_filtered_list)


