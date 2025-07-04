import random
import string

new_password = ""
 
def password_select():
  global new_password
  try:
    enter_length_password = int(input("Enter the length of your new password: "))
    if enter_length_password < 6:
      print("Password length must be at least 6 characters.")
      return
    elif enter_length_password > 20:
      print("Password length must not exceed 20 characters.")
      return
    else:
      hide_or_view = str(input("Would like your password to be hidden? (yes/no)")).lower()
      characters = string.ascii_letters + string.digits + string.punctuation
      new_password = ''.join(random.choice(characters) for _ in range(enter_length_password))
      if hide_or_view == 'yes':
        print(f"Your new password is hidden for security reasons.\n {'*' * len(new_password)}")
        ask_view = input("Your password is hidden. Would you like to view it? (yes/no): ").lower()
        if ask_view == 'yes':
          print(f"Your new password is: {new_password}")
          exit()
        elif ask_view == 'no':
          print("Exiting without revealing the password.")
          exit()
        else:
          print("Invalid input. Please enter 'yes' or 'no'.")
          return
      elif hide_or_view == 'no':
        print(f"Your new password is: {new_password}")
        exit()
      else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return
      
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

password_select()


