# todo list
def show_optins():
    print("1: add task")
    print("2: view task")
    print("3: mark as complet")
    print("4: exit")
    task=[]
def add_task():
    task = input("Enter your task")
    tasks.append(task)
    save_tasks()
    
    
def view_task():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
def mark_done():
    view_task()
    index = int(input("enter task number to mark:"))-1
    if 0<= index<len(tasks):
        print(f"Task '{tasks[index]}'marked")
        del tasks[index]
        save_task()
    else:
        print("invalid")
    
def save_task():
    with open("task.txt","w") as file:
        for task in tasks:
            file.write(task + "\n")
def load_task():
    try:
        with open("task.txt","r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
def main():
    load_tasks()
    while True:
        show_option()
        choice = input("enter choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            print("exiting")
            break
        else:
            print("invalid choice")
    
    
if _name_ == "_main_"
            
        
