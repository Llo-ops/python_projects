import random

def generate_random_num():
  input_num = input("Press Enter to generate a number: ")
  random_num = random.randint(1, 100)
  print(f"Generated random number: {random_num}")
  return random_num
generate_random_num()