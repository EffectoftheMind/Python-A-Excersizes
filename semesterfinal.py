tri_input = input("Enter your numbers: ").split(" ")

print()
print()

tri_a = int(tri_input[0])
tri_b = int(tri_input[1])
tri_c = int(tri_input[2])

def tri_type():
  if tri_c**2 < tri_a**2 + tri_b**2:
    print("The triangle is acute!")
  elif tri_c**2 == tri_a**2 + tri_b**2:
    print("The triangle is right!")
  else:
   print("The triangle is obtuse!")
    
tri_type()
