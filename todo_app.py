class TaskManager:
    def __init__(self):
        # List ki jagah dictionary use ki hai, jisse structure badal gaya
        self.todo_list = {}

    def insert_item(self, text):
        clean_text = text.strip()
        if not clean_text:
            print("Error: Task cannot be blank.")
            return
        
        # ID generate karne ka tarika badal diya
        current_id = max(self.todo_list.keys(), default=0) + 1
        self.todo_list[current_id] = {"name": clean_text, "completed": False}
        print(f"Successfully added: '{clean_text}'")

    def show_all(self):
        if not self.todo_list:
            print("Your list is currently empty.")
            return
        
        print("\n--- Current Tasks ---")
        for t_id, info in self.todo_list.items():
            check = "[✓]" if info["completed"] else "[ ]"
            print(f"{t_id}. {check} {info['name']}")

    def modify_item(self, t_id, updated_name):
        if not updated_name.strip():
            print("Error: New title cannot be blank.")
            return
        
        if t_id in self.todo_list:
            self.todo_list[t_id]["name"] = updated_name.strip()
            print("Task updated successfully.")
        else:
            print("System Error: ID not found.")

    def remove_item(self, t_id):
        if t_id in self.todo_list:
            del self.todo_list[t_id]
            print("Task has been removed.")
        else:
            print("System Error: ID not found.")

    def toggle_status(self, t_id):
        if t_id in self.todo_list:
            # Status toggle karne ka naya logic
            self.todo_list[t_id]["completed"] = not self.todo_list[t_id]["completed"]
            current_status = "Done" if self.todo_list[t_id]["completed"] else "Pending"
            print(f"Task status changed to: {current_status}")
        else:
            print("System Error: ID not found.")


def start_app():
    manager = TaskManager()
    
    while True:
        print("\n=====================")
        print("    MY TODO BOARD    ")
        print("=====================")
        print("[1] Display Tasks")
        print("[2] Create New Task")
        print("[3] Edit Existing Task")
        print("[4] Erase a Task")
        print("[5] Toggle Complete/Incomplete")
        print("[0] Shutdown App")
        
        user_select = input("Pick an option: ").strip()

        if user_select == "1":
            manager.show_all()
            
        elif user_select == "2":
            title_input = input("Enter what to do: ")
            manager.insert_item(title_input)
            
        elif user_select == "3":
            manager.show_all()
            try:
                target_id = int(input("Select ID to modify: "))
            except ValueError:
                print("Invalid input! Numbers only.")
                continue
            new_title = input("Enter new description: ")
            manager.modify_item(target_id, new_title)
            
        elif user_select == "4":
            manager.show_all()
            try:
                target_id = int(input("Select ID to delete: "))
            except ValueError:
                print("Invalid input! Numbers only.")
                continue
            manager.remove_item(target_id)
            
        elif user_select == "5":
            manager.show_all()
            try:
                target_id = int(input("Select ID to flip status: "))
            except ValueError:
                print("Invalid input! Numbers only.")
                continue
            manager.toggle_status(target_id)
            
        elif user_select == "0":
            print("Goodbye!")
            break
        else:
            print("Command not recognized. Try again.")


if __name__ == "__main__":
    start_app()