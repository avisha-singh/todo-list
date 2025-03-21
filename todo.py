tasks = []

def add_task(task):
    if task.strip():
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Cannot add an empty task.")

def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
