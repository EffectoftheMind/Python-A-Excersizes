# A1 - combining inputs
# This program reads two numbers and prints their sum:


def sum_three():
  a = int(input())
  b = int(input())
  c = int(input())
  return (a+b+c)
  
print(sum_three())



#A2 - Area of a Triangle
def tri_area():
  b = int(input())
  h = int(input())
  return (b*h/2)

print(tri_area())

#A3 - Combining Strings
def combine_str():
  a = (input())
  return ("Hello, " + a + "!")

print(combine_str())

#A4 - Find the larger of 2 numbers
def larger_num():
  a = input()
  b = input()
  if a>b:
    return ("The bigger number is " + a)
  else:
    return ("The bigger number is " + b)

print(larger_num())

#A5 - Printing Arrays
food_items = ["turkey","ham", "spam","eggs","nuts"]

def print_array():
  print(food_items[3])
  print("This will print the array of food items")
  for x in food_items:
    return(x)

print(print_array())
#A6 - Else if statements

grade = int(input("Enter Your Grade:"))
  
def if_grade():
  if grade in range (0, 59):
    return("F")
  elif grade in range (60, 69):
    return("D")
  elif grade in range (70, 79):
    return("C")
  elif grade in range (80, 89):
    return("B")
  else:
    return("A")

#A7 - Partial Arrays
a1 = [1, 1, 2, 3, 4, 5, 8, 11, 13, 17, 19, 20, 21, 34, 43, 55, 89]
def part_array():
  for x in a1:
    if x<30:
      return(x)

print(part_array())

#converting old assignments to functions
