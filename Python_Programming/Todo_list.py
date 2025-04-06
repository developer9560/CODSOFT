import os
import json
import datetime
import uuid

class Task:
    def __init__(self, title, description="", due_date=None, status=False):
        self.id = str(uuid.uuid4())[:8]  # Generate a unique ID
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status  # False = incomplete, True = complete
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"], data["due_date"], data["status"])
        task.id = data["id"]
        task.created_at = data["created_at"]
        return task

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.file_path = "tasks.json"
        self.load_tasks()
    
    def add_task(self, title, description="", due_date=None):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_all_tasks(self):
        return self.tasks
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if due_date is not None:
                task.due_date = due_date
            if status is not None:
                task.status = status
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def toggle_task_status(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = not task.status
            self.save_tasks()
            return True
        return False
    
    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.status == status]
    
    def get_incomplete_tasks(self):
        return self.get_tasks_by_status(False)
    
    def get_completed_tasks(self):
        return self.get_tasks_by_status(True)
    
    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json_data = [task.to_dict() for task in self.tasks]
            json.dump(json_data, f, indent=4)
    
    def load_tasks(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.tasks = []
        else:
            self.tasks = []

# Command-line interface
class CLI:
    def __init__(self):
        self.todo_list = ToDoList()
    
    def display_menu(self):
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View incomplete tasks")
        print("4. View completed tasks")
        print("5. Update a task")
        print("6. Delete a task")
        print("7. Mark task as complete/incomplete")
        print("8. Exit")
        return input("Enter your choice (1-8): ")
    
    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description (optional): ")
        due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
        due_date = due_date if due_date else None
        
        self.todo_list.add_task(title, description, due_date)
        print("Task added successfully!")
    
    def view_tasks(self, tasks):
        if not tasks:
            print("No tasks found.")
            return
        
        print("\n{:<10} {:<20} {:<30} {:<15} {:<10}".format(
            "ID", "Title", "Description", "Due Date", "Status"))
        print("-" * 90)
        
        for task in tasks:
            status = "Complete" if task.status else "Incomplete"
            desc = task.description[:27] + "..." if len(task.description) > 30 else task.description
            print("{:<10} {:<20} {:<30} {:<15} {:<10}".format(
                task.id, task.title[:17] + "..." if len(task.title) > 20 else task.title,
                desc, task.due_date if task.due_date else "N/A", status))
    
    def update_task(self):
        self.view_tasks(self.todo_list.get_all_tasks())
        task_id = input("\nEnter the ID of the task to update: ")
        task = self.todo_list.get_task_by_id(task_id)
        
        if not task:
            print("Task not found!")
            return
        
        print("\nLeave blank if you don't want to update a field.")
        title = input(f"Enter new title [{task.title}]: ")
        description = input(f"Enter new description [{task.description}]: ")
        due_date = input(f"Enter new due date [{task.due_date}]: ")
        
        title = title if title else None
        description = description if description else None
        due_date = due_date if due_date else None
        
        if self.todo_list.update_task(task_id, title, description, due_date):
            print("Task updated successfully!")
        else:
            print("Failed to update task.")
    
    def delete_task(self):
        self.view_tasks(self.todo_list.get_all_tasks())
        task_id = input("\nEnter the ID of the task to delete: ")
        
        if self.todo_list.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Failed to delete task. Task not found.")
    
    def toggle_task_status(self):
        self.view_tasks(self.todo_list.get_all_tasks())
        task_id = input("\nEnter the ID of the task to mark as complete/incomplete: ")
        
        if self.todo_list.toggle_task_status(task_id):
            print("Task status updated successfully!")
        else:
            print("Failed to update task status. Task not found.")
    
    def run(self):
        while True:
            choice = self.display_menu()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                print("\n----- All Tasks -----")
                self.view_tasks(self.todo_list.get_all_tasks())
            elif choice == '3':
                print("\n----- Incomplete Tasks -----")
                self.view_tasks(self.todo_list.get_incomplete_tasks())
            elif choice == '4':
                print("\n----- Completed Tasks -----")
                self.view_tasks(self.todo_list.get_completed_tasks())
            elif choice == '5':
                self.update_task()
            elif choice == '6':
                self.delete_task()
            elif choice == '7':
                self.toggle_task_status()
            elif choice == '8':
                print("Thank you for using the To-Do List Application!")
                break
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")


todo = CLI()
todo.run()

            
        
        

        



    
    


            


    
        