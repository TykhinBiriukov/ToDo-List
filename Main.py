tasks = []

def addTask():
    while True:
        task = input("Please enter a task: ")
        tasks.append(task)
        print(f"Task '{task} wass successfully added to the list")
    
def deleteTask():
    listTask()
    try:
        tasktoDelete = int(input("Choose number of the task you want to delete: "))
        if tasktoDelete >= 0 and tasktoDelete < len(tasks):
            tasks.pop(tasktoDelete)
            print(f"Task {tasktoDelete} has beeen removed.")
        else:
            print(f"Task #{tasktoDelete} was not found.")
    except:
        print("Invalid input")

def listTask():
    if not tasks:
       print("There are no tasks.")
    else:
        print("Current Tasks:")  
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

if __name__ == "__main__":
    # Create loop to run the app
    print("Welcome to the ToDo List app")
    while True:
        print("\nPlease select one of the following options:")
        print("___________________________________________\n")
        print("1. Add a new task;")
        print("2. Delete a task;")
        print("3. List tasks;")
        print("4. Quit;")
        
        choice = input("Enter your choice:")
        
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")