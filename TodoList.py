import sys
import os

FILENAME = 'tasks.txt'

def read_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as f:
        return [line.strip() for line in f.readlines()]

def write_tasks(tasks):
    with open(FILENAME, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def list_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print(f"Added: {task}")

def remove_task(index):
    tasks = read_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        write_tasks(tasks)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: todo.py [list|add|remove] [task/index]")
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "remove" and len(sys.argv) > 2:
        remove_task(int(sys.argv[2]))
    else:
        print("Invalid command.")
