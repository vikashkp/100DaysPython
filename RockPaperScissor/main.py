import random
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

def prtn(inpt):
  if inpt==0:
    print("Rock")
    print(rock)
  elif inpt==1:
    print("Paper")
    print(paper)
  elif inpt==2:
    print("Scissors")
    print(scissors)
  else:
    print("You didnt choose anything relevent!")
    exit()


def play(n1,n2):
  if(n1==n2):
    print("Tied! Try Again!")
  elif n1 == (n2+1)%3:
    print("You win")
  else:
    print("You lose")

inp1 = int(input("Input: 1=Rock, 2=Paper, 3=Scissors"))
inp1=inp1-1
prtn(inp1)
inp2= int(random.randint(0,2))
print("Computer chooses:")
prtn(inp2)
play(inp1,inp2)

#Rock Paper Scissor Game