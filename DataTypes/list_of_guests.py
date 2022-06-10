GuestsList = [
                ("Sylwia", 21, "female"),
                ("Piotr", 28, "male"),
                ("Katarzyna", 23, "female")
            ]

GuestsList.append(("Karol", 26, "male"))

for name, age, sex in GuestsList:
    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)
    print("\n")
