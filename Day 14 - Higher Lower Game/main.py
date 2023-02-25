def print_logo():
  from art import logo
  print(logo)

def print_vs():
  from art import vs
  print(vs)

def print_a(person, bio, country):
  print(f"Compare A: {person}, a {bio}, from {country}")

def print_b(person, bio, country):
  print(f"Against B: {person}, a {bio}, from {country}")

def scored_point(score):
  print(f"You're right! Current score: {score}")

def lose_game(score):
  print(f"Sorry, that's wrong. Final score: {score}")

from game_data import data
from random import choice
from replit import clear

#preload for while loop to work.
B = choice(data)
score = 0

show_score = False
continue_game = True
while continue_game == True:
  clear()
  print_logo()

  if show_score == True:
    scored_point(score)
  
  #Setup the choices
  A = B
  while A == B:
    B = choice(data)
  
  #Setup the screen
  print_a(A['name'], A['description'], A['country'])
  print_vs()
  print_b(B['name'], B['description'], B['country'])

  #Player choose
  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  A_count = int(A['follower_count'])
  B_count = int(B['follower_count'])

  #Determine Answer
  if A_count > B_count and guess == 'A':
    score += 1
  elif A_count < B_count and guess == 'B':
    score += 1
  elif A_count == B_count:
    score += 1
  else:
    continue_game = False
    clear()
    print_logo()
    lose_game(score)

  show_score = True
  