#Treasure Island

lr = input ("left or right ? ").lower()
#print (lr)
if lr == "right":
  print ("Game Over.")
elif lr == "left":
  sw = input ("Swim or wait ").lower()
  if sw == "swim":
    print ("Game over")
  elif sw == "wait":
    door = input("Which door ").lower()
    if door == "blue":
      print ("Game Over")
    elif door == "red":
      print ("game over")
    elif door == "yellow":
      print ("You Win!!!")
      
      
      