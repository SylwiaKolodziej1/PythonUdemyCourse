class User:
    age = 20

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_age(self):
        print(self.name, "age: ", self.age)


user1 = User(21, "Sylwia")
user2 = User(29, "Arek")


user1.print_age()
user2.print_age()
