# This program will take a numerical grade and give a letter grade output
grade = int(input("Enter your grade: "))

# Use an else if statement to check for each letter grade
if grade in range (0, 59):
  print("F")
elif grade in range (60, 69):
  print("D")
elif grade in range (70, 79):
  print ("C")
elif grade in range (80, 89):
  print ("B")
else:
  print("A")
