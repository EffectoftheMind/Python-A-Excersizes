import numpy
# input how many arrays
num_arrays = int(input("How many arrays do you want to find the average of?"))


#Hint:
for x in range(num_arrays):
  a = input("Enter your array").split()
  a = [int(x) for x in a]
  print("The average is: ", numpy.mean(a))

  
#Now use the code to see how many arrays?
#use a loop to now find the average and print the average.
