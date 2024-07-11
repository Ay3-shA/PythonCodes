#Tip Calculator

print ("Welcome to the tip Calculator!!!")

bill = float(input ("What was the total bill? $"))
tip = int(input ("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input ("How many people to split the bill? "))
total = tip / 100 * bill + bill
Each_person_bill = round(total / people, 2)

print (f"Each person should pay: $ {Each_person_bill} ")