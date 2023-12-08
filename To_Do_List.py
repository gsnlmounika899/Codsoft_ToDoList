List = []
def display_list():
    if List:
        print("The tasks in the List :")
        for i in range(len(List)):
            print(f"{i+1}.{List[i]}")
    else:
        print("There is no Task yet.")
def add_Task():
    Task= input("Enter the  Task: ")
    List.append(Task)
    print(f"{Task} added to the  list.")
def remove_Task():
    display_list()
    if List:
        try:
            idx = int(input("Enter the index of the Task you want to remove: "))
            if 0 <= idx < len(List):
                remove_task = List.pop(idx)
                print(f"Removed: {remove_task}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    else:
        print("There is no Task in the List.")
while True:
    print("\nMenu:")
    print("1. Add a Task")
    print("2. View the list")
    print("3. Remove a Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_Task()
    elif choice == '2':
        display_list()
    elif choice == '3':
        remove_Task()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid choice.")
