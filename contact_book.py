contact_book = []

print()
print("Contact Book")
print()

def main():  
  if not contact_book:
    print("Your Contact list is empty...")
  
  while True:
    name_input = input("Enter the name of your contact: ").strip()
    phone_input = input("Enter their phone humber: ").strip()
    email_input = input("Enter their email address: ").strip()
    
    contact = {
      "Name": name_input,
      "Phone": phone_input,
      "Email": email_input
    }
    
    contact_book.append(contact)
    print("Contact Added successfully")
    
    another = input("Would you like to add another contact? (yes/no): ").strip()
    if another == 'no':
      view_contacts()
    else:
      main()
    
def view_contacts():
  print("\nYour Contacts")
  for index, contact in enumerate(contact_book, start=1):
    print(f"{index} --> \nName: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\n")
  print()
  restart_process = input("Would you like to add another contact? (yes/no): ")
  if restart_process == 'yes':
    main()
  else:
    print("Alright, Goodbye!")
    exit()
    
main()