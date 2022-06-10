people = [
        {"id": "xyz", "name": "John", "age": 23, "telephone number": "728274686"},
        {"id": "abc", "name": "Marie", "age": 22, "telephone number": "700214686"},
        {"id": "tuw", "name": "Ana", "age": 25, "telephone number": "698274686"}
        ]

for dictionary in people:
    for record in dictionary:
        print(record,":", dictionary[record])

