import random #this will import a random number

num = random.randint(1, 100)

guess = int(input("Guess a number: "))
retry = int(input("Guess again: "))

while True:
  if num > guess:
    print("Too high!")
    print(retry)
  if num == guess:
    print("Exactly Right.")
  if num < guess:
    print("Too low!")
    print(retry)
    break
