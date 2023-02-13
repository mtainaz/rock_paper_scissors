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
import random

choice=[rock, paper, scissors]
index=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

error_stat="You picked an invalid number."
if index<0 or index>2:
  print(error_stat)
else:
  user_choice=choice[index]
  print(user_choice)
  comp_choice=random.choice(choice)
  print("Computer chose:\n"+comp_choice)

  if user_choice==comp_choice:
    print("It's a draw")
  elif user_choice==rock:
    if comp_choice==paper:
      print("You lose")
    else:
      print("You win")
  elif user_choice==scissors:
    if comp_choice==paper:
      print("You win")
    else:
      print("You lose")
  else:
    if comp_choice==rock:
      print("You win")
    else:
      print("You lose")
   