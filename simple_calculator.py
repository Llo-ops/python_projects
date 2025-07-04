
operators = ["+", "-", "*", "/", "%"]
result = ""
x = ""
y = ""


def main():
  global result, x, y
  print("Welcome to the Simple Calculator!")
  x = int(input("Enter the first Number: "))
  y = int(input("Enter the second Number: "))
  chosen_operator = input(f"Choose an operator: {operators}\n")

  match chosen_operator:
    case "+":
      result = x + y
    case "-":
      result = x - y
    case "*":
      result = x * y
    case "/":
      result = x / y
    case "%":
      result = x % y
    case _:
      print("Invalid operator. Please try again.")
      main()  # Restart if invalid operator is chosen
      
      
  print(f"Total of {x} {chosen_operator} {y} is {result}")
main()
