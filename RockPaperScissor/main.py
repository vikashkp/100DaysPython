import random
from replit import clear
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

def print_choice(input_choice):
  if input_choice==0:
    print("Rock")
    print(rock)
  elif input_choice==1:
    print("Paper")
    print(paper)
  elif input_choice==2:
    print("Scissors")
    print(scissors)
  else:
    print("You didnt choose anything relevent!")

def play(n1,n2):
  if(n1==n2):
    print("Tied! Try Again!")
  elif n1 == (n2+1)%3:
    print("You win!")
  else:
    print("You lose!")
def play_game():
  user_choice = int(input("Input: 1=Rock, 2=Paper, 3=Scissors: "))
  user_choice -= 1
  if user_choice > 2:
    print("Invalid Input, chose 1/2/3 ")
    return
  print_choice(user_choice)
  computer_choice= int(random.randint(0,2))
  print("Computer chooses:")
  print_choice(computer_choice)
  play(user_choice, computer_choice)
play_game()
while input("Press 'y' to start game, 'n' to quit: ")=="y":
  clear()
  play_game()