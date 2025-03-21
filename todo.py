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
            
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f'Task "{removed}" removed.')
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
