import random

difficulty = ['EASY', 'MEDIUM', 'HARD']
number_of_guesses = ""
user_guess = ""
random_number = ""

def main():
  global user_guess, random_number
  print("Welcome to the Number Guessing Game!")
  diff = input(f"Choose a difficulty level: {difficulty}\n").upper()
  
  match diff:
    case "EASY":
      easy_mode()
    case "MEDIUM":
      medium_mode()
    case "HARD": 
      hard_mode()
    case _:
      print("Invalid difficulty level. Please try again.")
      main()
  
def easy_mode():
  global number_of_guesses, user_guess, random_number
  number_of_guesses = 3
  random_number = random.randint(1, 10)
  print("You have chosen EASY mode. You have 3 guesses")
  user_guess = int(input("From 1-10 guess the number\n"))
  
  while number_of_guesses > 0:
    if user_guess == random_number:
      print("Congratulations! You guessed the number correctly")
      return
    elif user_guess < random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too low. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
    elif user_guess > random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too high. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
    
def medium_mode():
  global number_of_guesses, user_guess, random_number
  number_of_guesses = 5
  random_number = random.randint(1, 20)
  print("You have chosen MEDIUM mode. You have 5 guesses")
  user_guess = int(input("From 1-20 guess the number\n"))

  while number_of_guesses > 0:
    if user_guess == random_number:
      print("Congratulations! You guessed the number correctly")
      return
    elif user_guess < random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too low. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
    elif user_guess > random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too high. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
      
def hard_mode():
  global number_of_guesses, user_guess, random_number
  number_of_guesses = 7
  random_number = random.randint(1, 50)
  print("You have chosen HARD mode. You have 7 guesses")
  user_guess = int(input("From 1-50 guess the number\n"))

  while number_of_guesses > 0:
    if user_guess == random_number:
      print("Congratulations! You guessed the number correctly")
      return
    elif user_guess < random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too low. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
    elif user_guess > random_number:
      number_of_guesses -= 1
      if number_of_guesses == 0:
        print("Game Over! You've run out of guesses.")
        return
      print(f"Your guess is too high. You have {number_of_guesses} guesses left.")
      user_guess = int(input("Try again: "))
  
main()

