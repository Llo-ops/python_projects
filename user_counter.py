enter_num_for_count = int(input("Enter a number to start the count: "))

for i in range(enter_num_for_count):
  if enter_num_for_count < 0:
    print("Negative numbers are not allowed. Please enter a positive number.")
  else:
    for j in range(enter_num_for_count + 1):
      print(j)
    print("Counting completed.")
    break
else:
  print("No valid number was entered. Exiting the program.")