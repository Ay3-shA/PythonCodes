#Treasure map

row1 = ["⬜️️","️⬜️️","️⬜️️"]
row2 = ["⬜️️","⬜️️","️⬜️️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

num1 = int(position[0]) #row position
num2 = int(position[1]) #column position 

row = map[num2-1]
row[num1-1] = "X"

print(f"{row1}\n{row2}\n{row3}")



# num1 = int(position[0])
# num2 = int(position[1])

# if num2 == 1:
#   row1[num1-1] = "X"
# elif num2 == 2:
#   row2[num1-1] = "X"
# elif num2 == 3:
#   row3[num1-1] = "X"
# else:
#   print("This place does not exist!!!")

# print(f"{row1}\n{row2}\n{row3}")

  

