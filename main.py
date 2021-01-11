#ROCK-PAPER-SCISSORS game

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

rps=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))


computer=random.randint(0,2)

if rps==0 and computer==0:
  print(rock, end="\n")
  print("Computer chooses: ,\n"+rock)
  print("Draw")
elif rps==0 and computer==1:
  print(rock, end="\n")
  print("Computer chooses: ,\n"+paper)
  print("You loose!")
elif rps==0 and computer==2:
  print(rock, end="\n")
  print("Computer chooses: ,\n"+scissors)
  print("You win!")

if rps==1 and computer==0:
  print(paper, end="\n")
  print("Computer chooses: ,\n"+rock)
  print("Win!")
elif rps==1 and computer==1:
  print(paper, end="\n")
  print("Computer chooses: ,\n"+paper)
  print("Draw!")
elif rps==1 and computer==2:
  print(paper, end="\n")
  print("Computer chooses: ,\n"+scissors)
  print("You lose!")

if rps==2 and computer==0:
  print(scissors, end="\n")
  print("Computer chooses: ,\n"+rock)
  print("You lose!")
elif rps==2 and computer==1:
  print(scissors, end="\n")
  print("Computer chooses: ,\n"+paper)
  print("You win!")
elif rps==2 and computer==2:
  print(scissors, end="\n")
  print("Computer chooses: ,\n"+scissors)
  print("Draw!")


