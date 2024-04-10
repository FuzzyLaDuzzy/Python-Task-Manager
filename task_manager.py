TaskList = []


def addTask():
    while True:
        task = input("Enter a task: ")
        if task == "":
            print("Please insert an actual task\n")
        else:
            TaskList.append(task)
            print("List: ")
            print(TaskList)
            print("\n\n")
            return

def removeTask():
    while(True):
        task = input("Enter the task you want to remove: ")
        if(task in TaskList):
            TaskList.remove(task)
            print("Task sucessfully removed.\n")
            print("List: ")
            print(TaskList)
            print("\n\n")
            return
        else:
            print("That task is not on the list. Please try again.\n")

def printTasks():
    print(TaskList)

def editTask():
    print(TaskList)
    while True:
        task = input("Enter the task you want to edit: ")
        if(task in TaskList):
            TaskList.remove(task)
            taskEdit = input("Enter the changed Task: ")
            TaskList.append(taskEdit)
            return
        else:
            print("That task is not on the list. Please try again.\n")

def idle():
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Print the Task List")
        print("4. Edit a task")
        print("5. Exit")
        option = input("Choose an option: ")
        if option == "1":
            addTask()
        elif option == "2":
            removeTask()
        elif option == "3":
            printTasks()
        elif option == "4":
            editTask()
        elif option == "5":
            return
        else:
            print("Invalid input. Please enter an actual choice: ")
idle()