print("Hotel rooms")


rooms = {49: "Sylwia Kolodziej", 17: "Malgorzata Nowak", 69: ":Artur Wlodarczyk"}
rooms.update({400: "Jan Kowalski"})
del(rooms[69])

print(rooms)
print(len(rooms), "rooms occupied")


