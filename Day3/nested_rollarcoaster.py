#Rollarcoaster Nested if else 

print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0

if height>=120:
  #print("You can ride!!!")
  if age<12:
    bill = 5
    print("Child tickets are for $5.")
  elif age <=18:
    bill = 7
    print("Youth tickets are for $7.")
  else:
    bill = 12
    print("Adult tickets are for $12.")

  photo = input ("Do you want a photo taken ? y or n \n")
  if photo == "y":
    total_bill = int(bill) + 3
    print(f"Your total bill is {total_bill}$")
  else: 
    print(f"Your total bill is {bill}$")
    
else:
  print("Sorry! You have to grow taller before you can ride!!!")

#-----------------------------------------------------------
