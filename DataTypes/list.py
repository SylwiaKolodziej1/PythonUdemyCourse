numbers = [1, 2, 3, 4, 5, 6]

compoundNumber = []
for item in numbers:
    compoundNumber.append(item**2)

#equals

compoundNumber2 = [item**2
                  for item in numbers
                   ]


evenNumber = []
for item in numbers:
    if (item % 2 == 0):
        evenNumber.append(item)

#equals

evenNumber2 = [item
               for item in numbers
               if (item % 2 == 0)
               ]
