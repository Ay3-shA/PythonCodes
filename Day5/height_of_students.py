#height of the students

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

height = 0
student = 0

for student_height in student_heights:
  height = height + int(student_height)
#print(height)

for students in student_heights:
  student = int(student) + 1
#print (student)

average_height = round(height / student)
print(f"The Average Height of a student is {average_height}.")

#------------------------------------------------------------------