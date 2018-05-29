import collections

# Read inputs, don't generate random

def dice_poker():
  rolls = int(input())
  answers = []
  for roll in range(rolls):
    roll = input().split()            #this splits input at the spaces
    values = sorted([x for x in collections.Counter(roll).values()])   #this sorts the array and counts the values
    
    if sorted(roll) == ['2','3', '4', '5', '6',]:
      answers.append('big-straight')
    elif values == [2, 3, 4, 5, 6]:
      answers.append('small-straight')
    elif values == [2, 3]:
      answers.append('full-house')
    elif values == [1, 1, 1, 2]:
      answers.append('pair')
    elif values == [1, 2, 2]:
      answers.append('two-pairs')
    elif values == [1, 1, 3]:
      answers.append('three')
    elif values == [1, 4]:
      answers.append('four')
    elif values == [5]:
      answers.append('yacht')
    else:
      answers.append('none')
  
  print(' '.join(answers))
  
dice_poker()
