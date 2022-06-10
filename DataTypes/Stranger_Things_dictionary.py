characters = {"Jane Hopper" : 18,"Mike Wheeler" : 19, "Dustin Henderson" : 19}
                 

print("""Age of Stranger Things Series characters
""")

while(True):
    print("1: Add character")
    print("2: Find character")
    print("3: Remove character")
    print("4: Close a program")

    choose = input("Choose what you want to do: ")

    if (choose == "1"):
        newName = input("Give a name of a character: ")
        newAge = input("Give age of a character: ")
        characters[newName] = newAge
        print("You added a definition")
        print(characters)

    elif (choose == "2"):
        name = input("Choose a character: ")
          if name in characters:
            print(characters[name])
          else:
            print("No such a character")

    elif (choose == "3"):
        name = input("Choose a character to remove: ")
        characters.pop(name, None)
        print(characters)

    elif (choose == "4"):
         print("We're ending the program")
         break

    else:
        print("You didn't choose a proper option")
