# Use the code from last exercise here.
array1 = []
number=input("How many elements do you want?: ")

for x in range (int(number)):
  n = input("Enter Number: ")
  array1.append(int(n))
print (array1)

prompt=int(input("Which number do you want to find?"))

def count_nums(array1):   #this defines the method
  count = 0
  for x in array1:    
    if x == prompt:
      
      count+=1
  return count

print("There are %x %x's in the array"%(count_nums(array1),prompt))
