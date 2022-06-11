#Sum squared numbers from 0 to 100 

numbersGenerator = (item**2
                    for item in range(101)
                   )

print(sum(numbersGenerator))
