# Take user input
word=input("Please enter a word:")

if word == word[::-1]:
  print("This word is a palindrome!")
else:
  print("This word is not a palindrome!")
