#coin flip

import random

flip_coin = int(input('How many times do you want to flip a coin?\n'))

coin_face = ["Heads", "Tails"]

head_count = 0
tail_count = 0

for i in range(flip_coin):
  coin_choice = random.choice(coin_face)
  if coin_choice == "Heads":
    head_count +=1
  elif coin_choice == "Tails":
    tail_count +=1
  
print("Total Flips:")
print("------------")
print("Heads: ", head_count)
print("Tails: ", tail_count)
