import datetime

enter_date = input("Enter tour date of birth (YYYY-MM-DD): ")
today = datetime.date.today()
try:
  birth_date = datetime.datetime.strptime(enter_date, "%Y-%m-%d").date()
  age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
  print(f"Your age is: {age} years")
except ValueError:
  print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
except Exception as e:
  print(f"An error occurred: {e}")
finally:
  print("Thank you for using the age calculator!")
  print("Goodbye!")