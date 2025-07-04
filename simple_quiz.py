score = 0

questions = {
  1: ("What is the color of the sky? ", ['a. blue', 'b. pink', 'b. red'], 'a'),
  2: ("What are the colors of an apple? ", ['a. Red and Green', 'b. Red and Yellow', 'c. Green and Yellow'], 'a'),
  3: ("what is the color of a ripe banana? ", ['a. Blue', 'b. Green', 'c. Yellow'], 'c')
}

for index, q in enumerate(questions):
  print(f"{index + 1}. {questions[q][0]}")
  
print()
print("Here are your choices for each question: ")

for index, c in enumerate(questions):
  print(f"\n{index + 1}. {'-' * 20}")
  for choice in questions[c][1]:
    print(choice)
    
while True:
  for index, a in enumerate(questions):
    user_answer = input(f"Enter the answer for number {index + 1}: ").lower().strip()
    if user_answer == questions[a][2]:
      print("Your answer is correct!")
      score += 1
    else:
      print("That is the wrong answer...")
    
  print('Your Score is: ' + str(score))
  if score == 0:
    print("Better luck next time...")
  elif score > 0 and score < 3:
    print("Congrats! You passed the test.")
  else:
    print("Congratulations! You perfected the test.")
  break
  