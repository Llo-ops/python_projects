conversion_map = [
  (1, 'meters', 'kilometers'),
  (2, 'grams', 'kilograms'),
  (3, 'liters', 'milliliters'),
  (4, 'celsius', 'fahrenheit'),
  (5, 'seconds', 'minutes'),
  (6, 'hours', 'days'),
  (7, 'inches', 'feet'),
]

print("Welcome to the Unit Converter!")
print()
print("Here are the conversions available:")
print()

for index_number, from_conversion, to_conversion in conversion_map:
  print(f"{index_number} {from_conversion} --> {to_conversion}")
  
print()
conversion_index = input(f"Please Enter a number from the Conversion Table: ")
try:
  number_conversion = int(conversion_index) - 1
except ValueError:
  print("Invalid input, Please try again.")
  
number_conversion, from_conversion, to_conversion = conversion_map[number_conversion]
print()
from_value = float(input(f"Enter {from_conversion}: "))

if number_conversion == 1:
  to_value = from_value / 1000
  print(f"Meter: {from_value} {from_conversion} --> Kilometers: {to_value} {to_conversion}")
elif number_conversion == 2:
  to_value = from_value / 1000
  print(f"Grams: {from_value} {from_conversion} --> Kilograms: {to_value} {to_conversion}")
elif number_conversion == 3:
  to_value = from_value / 1000
  print(f"Liters: {from_value} {from_conversion} --> Mililiters: {to_value} {to_conversion} ")
elif number_conversion == 4:
  to_value = from_value * (9/5) + 32
  print(f"Celsius: {from_value} {from_conversion} --> Farenheit: {to_value} {to_conversion}")
elif number_conversion == 5:
  to_value = from_value / 60
  print(f"Seconds: {from_value} {from_conversion} --> Minutes: {to_value} {to_conversion} ")
elif number_conversion == 6:
  to_value = from_value / 24
  print(f"Hours: {from_value} {from_conversion} --> Days: {to_value} {to_conversion}")
elif number_conversion == 7:
  to_value = from_value / 12
  print(f"Inches: {from_value} {from_conversion} --> Feet: {to_value} {to_conversion} ")
else:
  print("Invalid Input. Please try again")
  