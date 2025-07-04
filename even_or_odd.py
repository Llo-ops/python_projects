number = int(input("Enter a number: "))
if isinstance(number, int):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
else:
    print("Please enter a valid integer.")