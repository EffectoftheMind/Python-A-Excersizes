#cesar cipher

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Enter the key shift'))
newMessage = ''

message = input('Please enter a message: ')

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter
  else:
    newMessage += character
print('Your new message is: ', newMessage)
