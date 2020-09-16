#calc with exceptions

def add(a, b):
  return(a + b)
  
def subtract(a, b):
  return a - b
  
def multiply(a, b):
  return a * b
  
def divide(a, b):
  return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()

while True:
  try:
    operation = int(input("Select Operation (1, 2, 3, 4): "))

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if operation == 1:
      print(add(a, b))
    elif operation == 2:
      print(subtract(a, b))
    elif operation == 3:
      print(multiply(a, b))
    elif operation == 4:
      print(divide(a, b))
    else:
      print("Non-Valid Number")
  except ZeroDivisionError:
    print()
    print("Impossible - Can't Divide by Zero")
    break
  except ValueError:
    print()
    print("Enter a Whole Number Please")
    break


#Example
#while True:
  #try:
    #age = int(input('Enter your age: '))
  #except ValueError:
    #print('Enter a whole number!')
  #else:
    #if age < 21:
      #print('Not Allowed!')
      #break
    #else:
      #print('Welcome!')
      #break
