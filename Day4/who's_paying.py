#who's paying exercise 

import random

test_seed = int(input("Create a seed number "))
random.seed(test_seed)

# Split string method  
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
print(names)
names_length = len(names)
#print(names_length)
#print(type(names_length))
random_name = random.randint(0, names_length - 1)
#print(random_name)
pay = (names[random_name])
print(f"{pay} is going to pay bill.")

#--------------------------------------------------------------------------