#countdown clock

import time
import datetime
from datetime import timedelta
import replit

current = datetime.datetime.now() - timedelta(hours = 6)

preset_option=input("Would you like to use a preset? If yes, type 'y', otherwise, 'type 'n'.")

if preset_option == 'y':
  presets = input("New Year's [1], Valentine's Day [2], Halloween [3], Thanksgiving [4], or Christmas [5]. Please type the number.")
  if presets == '1':
    while True:
      current = datetime.datetime.now() - timedelta(hours = 6)
      print("There are:")
      print(str(19-current.day) + " days")
      print(str(23-current.hour) + " hours")
      print(str(59-current.minute) + " minutes")
      print(str(59-current.second) + " seconds")
      print("Until New Years Day!")
      time.sleep(1)
      replit.clear()
  if presets == '2':
    while True:
      current = datetime.datetime.now() - timedelta(hours = 6)
      print("There are:")
      print(str(64-current.day) + " days")
      print(str(23-current.hour) + " hours")
      print(str(59-current.minute) + " minutes")
      print(str(59-current.second) + " seconds")
      print("Until Valentine's Day!")
      time.sleep(1)
      replit.clear()
  if presets == '3':
    while True:
      current = datetime.datetime.now() - timedelta(hours = 6)
      print("There are:")
      print(str(323-current.day) + " days")
      print(str(23-current.hour) + " hours")
      print(str(59-current.minute) + " minutes")
      print(str(59-current.second) + " seconds")
      print("Until Halloween!")
      time.sleep(1)
      replit.clear()
  if presets == '4':
    while True:
      current = datetime.datetime.now() - timedelta(hours = 6)
      print("There are:")
      print(str(334-current.day) + " days")
      print(str(23-current.hour) + " hours")
      print(str(59-current.minute) + " minutes")
      print(str(59-current.second) + " seconds")
      print("Until Thanksgiving Day!")
      time.sleep(1)
      replit.clear()
  if presets == '5':
    current = datetime.datetime.now() - timedelta(hours = 6)
    while True:
      print("There are:")
      print(str(24-current.day) + " days")
      print(str(23-current.hour) + " hours")
      print(str(59-current.minute) + " minutes")
      print(str(59-current.second) + " seconds")
      print("Until Christmas Day!")
      time.sleep(1)
      replit.clear()
  else:
    print("Invalid!")
if preset_option == 'n':
  event_day = int(input("How many days until your event?"))
  current = datetime.datetime.now() - timedelta(hours = 6)
  while True:
    print("There are:")
    print(str(event_day - current.day) + " days")
    print(str(23- current.hour) + " hours")
    print(str(59- current.minute) + " minutes")
    print(str(59- current.second) + " seconds")
    print("Until The Event!")
    time.sleep(1)
    replit.clear()
