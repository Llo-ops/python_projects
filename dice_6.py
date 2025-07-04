import random 

die_side = [1, 2, 3, 4, 5, 6]

def main():
  global die_side
  print("6-sided Dice Simulator")
  number_of_dices = int(input(f"How many dices would you like to roll?\n"))
  match number_of_dices:
    case 1:
      print(f"You rolled a {random.choice(die_side)}")
    case 2:
      print(f"You rolled a {random.choice(die_side)} and a {random.choice(die_side)}")
    case 3:
      print(f"You rolled a {random.choice(die_side)}, a {random.choice(die_side)}, and a {random.choice(die_side)}")
    case _:
      print("Invalid number of dices.")
      main()
main()