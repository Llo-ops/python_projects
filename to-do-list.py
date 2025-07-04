menu_selection = {
    1: "Add Task",
    2: "View Tasks",
    3: "Remove Task",
    4: "Exit"
}
to_do_task = []

def menu():
  try:
    for key, value in sorted(menu_selection.items()):
      print(f"{key}: {value}")
    select_option_menu = int(input(f"Please pick one of the following options: "))
  except ValueError:
    print("Invalid input. Please enter a number corresponding to the menu options.")
    return
  
  if select_option_menu not in menu_selection:
    print("Invalid selection. Please try again.")
  elif select_option_menu == 1:
    add_task()
  elif select_option_menu == 2:
    view_task()
  elif select_option_menu == 3:
    remove_task()
  elif select_option_menu == 4:
    print("Exiting the To-Do List App. Goodbye!")
    exit()
  else:
    print("Invalid selection. Please try again.")

def add_task():
  
  print(f"You have {len(to_do_task)} task(s) in the list.")
  while True:
    enter_task = input("Enter a task to add to your list: \ntype 'exit' to go back to the menu\n").strip().lower()
    if enter_task == 'exit':
      print("Exiting task addition. Returning to menu...")
      menu()
    else:
      to_do_task.append(enter_task)
      print("Task added successfully!")
  
        
def view_task():
  if not to_do_task:
    print("No tasks in the list.")
    menu()
  else:
    print("Current tasks:")
    for i, task in enumerate(to_do_task, start=1):
        print(f"{i}: {task}")
        menu()
  
  
def remove_task():
  print(f"Here are your tasks: {to_do_task}")
  try:
    rm_task = int(input("Enter the index of the task you want to remove: "))
    if rm_task not in range(len(to_do_task)):
      print("Invalid task index. Please try again.")
      remove_task()
    else:
      removed_task = to_do_task.pop(rm_task - 1)
      print(f"Task '{removed_task}' has been removed successfully!")
      menu()
  except ValueError:
    print("Invalid input. Please enter a number corresponding to the task index.")
    menu()
  
def main():
  print("Welcome to the To-Do List App!")
  print("Here is the menu: ")
  menu()

main()