import random

placements = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

def generate_10():
  for i in range(10):
    gen10 = input(f"Press Enter to generate the {placements[i]} number: ")
    random_num = random.randint(1, 100)
    print(f"Generated {placements[i]} number: {random_num}")
  return random_num

generate_10()