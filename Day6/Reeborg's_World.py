#Reeborg's World 
#game, robot, its movement, left, right, straight, back, jump.

def turn_right():
  turn_left()
  turn_left()
  turn_left() 

def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()

#for jump in range(4):
 # pattern()
number_of_hurdles = 4
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1 
  print(number_of_hurdles)