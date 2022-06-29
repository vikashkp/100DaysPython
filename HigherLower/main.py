import random
from replit import clear
from HigherLower.gamedata import data
from HigherLower.art import logo, vs

def choose_profile():
  return random.choice(data)

def print_profile(profile):
  return f"{profile['name']}, {profile['description']}, from {profile['country']}"

def run_game():
  global score, lastWin
  clear()
  print(logo)
  if score > 0:
    if lastWin:
      print(f"You're right! Current Score: {score}")
    else:
      print(f"Wrong Answer! Game Ended! Final Score: {score} \n")
      exit()

  profile1 = choose_profile()
  profile2 = choose_profile()
  while profile2 == profile1:
    profile2=choose_profile()
  print("compare A: " + print_profile(profile1))  
  print(vs)
  print("compare B: " + print_profile(profile2))
  user_answer = input("Who has more followers? Type 'A' or 'B':")
  if profile1['follower_count'] > profile2['follower_count'] and user_answer == "A":
    score += 1
    return
  elif profile1['follower_count'] < profile2['follower_count'] and user_answer == "B":
    score += 1
    return
  elif user_answer != "A" and user_answer != "B":
    lastWin = False
    print("Unknown Input! Game Over!")
  else:
    lastWin = False

score = 0
lastWin = True
while True:
  run_game()