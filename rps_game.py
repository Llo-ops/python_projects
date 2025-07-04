#Rock, Paper, Scissors Game
import random
score = 0

rps_choices = ['rock', 'paper', 'scissors']

print()
print("Welcome to the Game!")
print("Here are your Choices: ")
print()

for pick in rps_choices:
  print(f"{pick}")

print()
user_pick = str(input("Enter your weapon of choice: ")).lower().strip()

if user_pick in rps_choices:
  print(f"You picked: {user_pick.capitalize()}")
else:
  print("Your choice is not in the list.")
  exit()
  
cpu_pick = random.choice(rps_choices)
print(f"CPU picked: {cpu_pick.capitalize()}")

if user_pick == cpu_pick:
  print("It's a tie.")
elif (user_pick - cpu_pick) % 3 == 1:
  print(f"You picked: {user_pick}\nCPU picked: {cpu_pick}\nYou win!")
else:
  print("You lose...")