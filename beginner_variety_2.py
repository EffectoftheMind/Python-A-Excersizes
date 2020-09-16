#see a23

import time

# inputs
name = input('Enter your name: ')
num_of_stars = int(input('Please Enter the rows of stars you would like to print: '))
count = int(input('What number do you want to count to? '))

array = input('Please enter an array separated by spaces to check for duplicates.\n').split()
array = [int(x) for x in array]


# Exercise 1 function
def rev_name():
  print(name[::-1])

# Exercise 2 function
def star_rows():
  for x in range(1, num_of_stars + 1):
    print("*" * x)

# Exercise 3 function
def count_time():
  for x in range(1, count + 1):
    time.sleep(x)
    print(x)

# Exercise 4 function
def dup_check(array):
  array = list(set(array))
  print(array)

# Call your functions here!
rev_name()
star_rows()
count_time()
dup_check(array)
