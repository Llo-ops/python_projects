# Based on watsojar github and Code Coach on Youtube

import random

list_confirmation_yes = ['y', 'yes', 'Yes', 'yEs', 'yeS', 'YES']
list_confirmation_no = ['n', 'no', 'No', 'nO']

player = ['x', 'o']
player_chosen = None
winner = None
gameRunning = True
game_coin = ['heads', 'tails']

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

def printBoard(board):
  print(board[0] + '  |  ' + board[1] + '  |  ' + board[2])
  print('---+-----+---')
  print(board[3] + '  |  ' + board[4] + '  |  ' + board[5])
  print('---+-----+---')
  print(board[6] + '  |  ' + board[7] + '  |  ' + board[8])

def choose_player():
  print("Available pieces: ")
  for p in player:
    print(f"{p}")
    
  chosen_player = input("Pick a character to play: ").lower()
  
  if chosen_player in player:
    return chosen_player
  
  else:
    print("Invalid input. please choose 'x' or 'o'")
    return None
    
def coin_toss():
  coin = random.choice(game_coin)
  for c in game_coin:
    print(f"- {c}")
   
  chosen_side_coin = input("Heads or Tails: ").capitalize().strip()
  if chosen_side_coin == coin:
    print(f"The coin landed on {chosen_side_coin}")
    return 'first'
  else:
    print(f"The coin landed on {chosen_side_coin}")
    return 'second'  

def check_horizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[0] != ' ':
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != ' ':
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != ' ':
    winner = board[6]
    return True
  
def check_vertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != ' ':
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[3] != ' ':
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[6] != ' ':
    winner = board[3]
    return True
  
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != ' ':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != ' ':
        winner = board[2]
        return True
    
def check_win(board):
  global gameRunning
  if check_horizontal(board):
    printBoard(board)
    print(f"The Winner is {winner}!")
    gameRunning = False
    
  elif check_vertical(board):
    printBoard(board)
    print(f"The Winner is {winner}!")
    gameRunning = False
    
  elif check_diagonal(board):
    printBoard(board)
    print(f"The Winner is {winner}!")
    gameRunning = False
    
def check_tie(board):
  global gameRunning
  if ' ' not in board:
    printBoard(board)
    print("It's a Tie")
    gameRunning = False
  
def ask_restart():
  restart_game = input("Would you like to play again? (y/n)").lower().strip()
  try:
    if restart_game in list_confirmation_yes:
      main()
    elif restart_game in list_confirmation_no:
      print("Alright thanks for playing!")
      exit()
    else:
      print("Try again...")
  except ValueError:
    print("Invalid Input.")

def main():
  chosen_player = choose_player()
  
  if chosen_player:
    print(f"This is your chosen player: {chosen_player}")
  else:
    print(f"No valid player was selected...")
    
  turn = coin_toss()
  print(f"You go {turn}") 
  
  while gameRunning:
    printBoard(board)
    chosen_placement = int(input("Enter a number (1-9): "))
    if board[chosen_placement - 1] == ' ':
      board[chosen_placement - 1] = chosen_player
      if chosen_player == 'x':
        chosen_player = 'o'
      else:
        chosen_player = 'x'
    else:
      print(f"{board[chosen_placement - 1]} is already occupied")
    
    check_horizontal(board)
    check_vertical(board)
    check_diagonal(board)
    
    check_win(board)
    check_tie(board)
    
    if gameRunning == False:
      ask_restart()

main()
