tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    for task in tasks:
        print(task)