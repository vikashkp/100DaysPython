############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from Blackjack.art import logo

user_cards = []
computer_cards = []

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "Computer Wins!"
  elif user_score == 0:
    return "Win with a Blackjack!"
  elif user_score > 21:
    return "You went Over! You Lose!"
  elif computer_score > 21:
    return "Conmuter went Over! You Win!"
  elif user_score > computer_score:
    return "You Win!"
  else:
    return "You Lose!"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  isGameOver = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not isGameOver:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"User cards {user_cards}, score = {user_score}")
    print(f"Computer's first cards {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score >21:
      isGameOver = True
    else:
      user_should_deal = input("Typr 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        isGameOver = True
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
   
  print(f"User's final cards {user_cards}, score = {user_score}")
  print(f"Computer's final cards {computer_cards}, score = {computer_score}")
  
  print(compare(user_score, computer_score))

while input("Do you want to play a game of balckjack? Type 'y' or 'n' ") == "y" == 'y':
  clear()
  play_game()

clear()
print(logo)
print("Game Exited!")
exit()