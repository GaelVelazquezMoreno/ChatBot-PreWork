print('Hello and welcome to the Elite101 ChatBot!')
print('We are excited to have you here!')
print('I am going to ask you a few questions to get to know you better!')
# I used for .isalpha from this source: https://www.youtube.com/watch?v=TWlRjAqxVH8
name = input('What is your name?')
while not name.isalpha():
    print('Please enter a valid name with only alphabetic characters.')
    name = input('What is your name?')
  
print(f'Hello {name}! It is nice to meet you!')

try:
 age = int(input('How old are you?'))
except ValueError:
  age = 0
  age = input('Enter a Valid Age: ')
else:
  if age < 15:
    print('You are too young to be here!')
  elif 15 <= age < 18:
    print('You are a teenager!')
  elif 18 <= age < 55:
    print('You are an adult!')
  elif 55 <= age < 120:
    print(f'You are pretty old {name}')
  else:
    print('And I thought I was old!')

print(f'How can I assit you today {name}?')

def display_menu():
  print('\n Please select from the following options:')
  print('1.Tell me horror story')
  print('2.Tell me a joke')
  print('3.Tell me a fact')
  print('4.Exit the conversation\n')

def Necromancer_story():
  print('There was a city that lived in some cold moutins called Windhelm.')
  print('In this city lived viking warroirs and bards but there also some gray skin people with pointy ears.') 
  print('They are referd as gray folk and lived in a part of the city called Gray Quarter.')
  print('The vikings and the gray folk never got along well as the viking were extreamly rude to the gray folk because they thought some of them were spys of their enemys.')
  print('But there was another problem in Windhelm, there were a lot of muders going on in the city.')
  print('The lates of the muderes was a women in the cemetery with several scar on her body from a dagger.')
  print('The guards were able so see someone run away from the crime scene but they were not able to find the person.')
  print('Were able to talk to the women  before she died and she told the guards that he the muderer is an abonden house called Curse Vial.')
  print('So the guards went to the house and found blood on the floor,some broken glass,and some odd looking stacetd frunture.')
  print('But no sign of the muderer but when they were about to leave one of the guards saw a hidden door in the closet so they activated it and they could in be more scared in their lifes than what they just witness.')
  print('A room with blood all over the ceiling and walls,surgery tolls on a table, and a book shelf with journals and papers.')
  print('But what couth their eye was the flooting mutalted body of a man with no skin with a blue glowing aura around him flooting.')
  print('And at the same time a man with a neclace with skull saying chanting words as the dead body comes to life.')
  print('THE END...')

def user_selection():
  in_use = True
  user_chose = int(input('Enter a number between 1-4: '))
  if user_chose == 1:
    Necromancer_story()
  elif user_chose == 2:
   print('What did the pig say when it was hot outside?I am out of bacon hear.')
  elif user_chose == 3 :
   print('A polar bear standing up is almost as tall as the largest african elephant which was 13ft tall.')
  elif user_chose == 4:
    print('Thank you for using the Elite101 ChatBot!')
    in_use = False
  else:
    print('Please enter a valid number between 1-4')

    return in_use

display_menu()
user_selection()
  
  
  

  
