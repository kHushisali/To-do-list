# TO-DO list in python

tasks = []

def show_menu():
       print("\n--- To-do List ---")
       print("1. Add Task")
       print("2 view Task")
       print("3. mark Task as done")
       print("5. Update Task")
       print("4. Delete Task") 
       print("5.Exit")

def add_task():
    task = input("Enter task: ") 
    tasks.append({"task": task, "done":False})
    print(f"Task '{task}' added!")

def view_task():
     if not tasks: 
          print("No tasks yet!")
          return 
     print("\n Your Tasks:")
     for index, task in enumerate(tasks, start=1):
          status = "wrong" if task ["done"] else "right"
          print(f"{index}. {task['task']} [{status}]")

def mark_done():
     view_task()
     if not tasks:
       return
     try:
          index = int(input("Enter task number to mark done: ")) -1 
          
          if 0 <= index < len(tasks):
               tasks[index]["done"] = True
               print("Marked as done!")
          else:
               print("Invalid number!")
     except ValueError:
          print("please enter a valid number.")

def update_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            if new_task.strip():
                tasks[index]["task"] = new_task
                print("Task updated successfully!")
            else:
                print("Task cannot  be empty.")
        else:
            print("Invalid number!")
    except ValueError:5
    print("Please enter a valid number.")

while True:
     show_menu()
     choice = input("Choose an options (1-5): ")

     if choice == '1':
          add_task()

     elif choice == '2':
          view_task()

     elif choice == '3':
          mark_done()

     elif choice == '4':
          delete_task()
  
     elif choice == '5':
          update_task()

     elif choice == '6':
          print("Goodbye!")
          break
     else:
          print("INvalid choice. try again. ")
          




     
     

       