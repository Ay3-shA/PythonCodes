#Rollarcoaster Nested if else 

print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height>=120:
  print("You can ride!!!")
  if age >=18:
    print("You have to pay $12.")
  elif age<12:
    print("You have to pay $5")
  else:
    print("You have to pay $7")
else:
  print("Sorry! You have to grow taller before you can ride!!!")

#----------------------------------------------------------------
