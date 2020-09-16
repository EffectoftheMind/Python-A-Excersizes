#find the sum of all of the multiples of 3 and 5 under 500

total=0
for x in range (0,500):
  if x%3==0 or x%5==0:
   total = total + x
print (total)
