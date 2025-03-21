# To-Do List Application

## Overview
This is a simple command-line To-Do List application written in Python. It allows users to add, list, and remove tasks efficiently.

## Features
- **Add Tasks:** Users can add tasks to the list.
- **List Tasks:** View all tasks with their respective numbers.
- **Remove Tasks:** Delete tasks by providing their number.
- **Bug Fix:** Prevents empty tasks from being added.

## Project Structure
```
📦 todo-list
 ┣ 📜 todo.py   # Main Python script for the To-Do List
 ┣ 📜 README.md # Documentation
 ┗ 📜 .gitignore # Git ignored files
```

## Installation & Usage
### Prerequisites
- Python 3 installed on your system.
- Git installed for version control.

### Steps to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/todo-list.git
   cd todo-list
   ```
2. Run the script:
   ```sh
   python todo.py
   ```

## Git Workflow
### Branches Used:
- `main` - Stable version of the project.
- `feature-1` - Implements the `remove_task` function.
- `bug-fix` - Fixes a bug preventing empty tasks from being added.

### Commands Used:
#### Initialize Repository
```sh
git init
git add todo.py
git commit -m "Initial commit: Add basic to-do list application"
```
#### Create Branches
```sh
git branch feature-1
git branch bug-fix
```
#### Make Changes and Commit
```sh
git checkout feature-1
# Modify todo.py to add remove_task function
git commit -am "Add remove_task function to delete tasks"
```
```sh
git checkout bug-fix
# Modify todo.py to prevent empty tasks
git commit -am "Fix bug: Prevent empty tasks from being added"
```
#### Merge Changes into Main
```sh
git checkout main
git merge feature-1
git merge bug-fix
```
#### Push to GitHub
```sh
git remote add origin https://github.com/your-username/todo-list.git
git push -u origin main
```

## Author
Avisha Singh
