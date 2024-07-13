#True Love Calculator

print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = (name1 + name2).lower()
#print(name)

T = name.count("t")
print (f"\nT occurs {T} times. \n")
R = name.count("r")
print (f"R occurs {R} times. \n")
U = name.count("u")
print (f"U occurs {U} times. \n")
E = name.count("e")
print (f"E occurs {E} times. \n")

true = T + R + U + E 
#print (true)

L = name.count("l")
print (f"L occurs {L} times. \n")
O = name.count("o")
print (f"O occurs {O} times. \n")
V  = name.count("v")
print (f"V occurs {V} times. \n")
E = name.count("e")
print (f"E occurs {E} times. \n")

love = L + O + V + E
#print (love)

lovescore = int(str(true) + str(love))
#print (f"Love score is {lovescore}")

if (lovescore < 10) or (lovescore > 90):
  print(f"Your Score is {lovescore} , you go together like coke and mentos!!!")
elif (lovescore >= 40) and (lovescore <= 50):
  print (f"Your Score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}")

#----------------------------------------------------------------------


