def menu():
    print("To-Do List:")
    print("1. Add task")
    print("2. View task")
    print("3. Mark Task as completed")
    print("4. Delete task")
    print("5. Exit")

def add(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("---------------------------")

def view(tasks, done):
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        if task in done:
            print(f"{i}. {task} is done")
            print("---------------------------")
        else:
            print(f"{i}. {task} is not done")
            print("---------------------------")
            

def TaskDone(tasks, done):
    view(tasks, done)
    n = int(input("enter number of which task you'd like to mark as done: ")) - 1
    if 0 <= n < len(tasks):
        done.add(tasks[n])
        print(f"task {n} has been marked as done")
        print("---------------------------")

def delete(tasks, done):
    view(tasks, done)
    n = int(input("enter the number of the task would you like to delete: ")) - 1
    if 0 <= n < len(tasks):
        done.discard(tasks[n])
        tasks.pop(n)
        print(f"task {n} has been deleted")
        print("---------------------------")

def main():
    tasks = []
    done = set()
    choice = "0"

    while choice != "5":
        menu()
        choice = input("enter choice: ")
        if choice == "1":
            print("---------------------------")
            add(tasks)
        elif choice == "2":
            print("---------------------------")
            view(tasks, done)
        elif choice == "3":
            print("---------------------------")
            TaskDone(tasks, done)
        elif choice == "4":
            print("---------------------------")
            delete(tasks, done)
        elif choice == "5":
            break
           
if __name__ == "__main__":
    main()