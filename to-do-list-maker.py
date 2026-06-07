
# To Do List

import os

tasks = []

menu = [
    "Add a New Task",
    "Remove a Task",
    "Change a Task",
    "View All Tasks",
    "Export All Task into File",
    "Exit",
]

print("\n" + "="*55)
print(" "*13 + " Welcome to To_Do List Maker " + " "*13)
print("="*55)

while True:
    # print("\n")
    try:
        for index, features in enumerate(menu, start=1):
            print(f"{index} - {features}")

        features_selected = int(input("\nEnter a Number to Proceed: "))

        if features_selected == 1:
            task = input("Enter a New Task: ")
            tasks.append(task)
            print(f"\nTask Added: {task}\n")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            continue

        elif features_selected == 2:
            if not tasks:
                print("\nNo Tasks Available!\n")
                continue

            for idx, task_1 in enumerate(tasks, start=1):
                print(f"{idx} - {task_1}")

            remove_task = int(input("\nEnter a Task Number to Remove: "))
            tasks.pop(remove_task - 1)
            print("\nTask Removed!\n")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            continue

        elif features_selected == 3:
            for num, task_2 in enumerate(tasks, start=1):
                print(f"{num} - {task_2}")

            change_task = int(input("Enter a Task Number: "))
            tasks.pop(change_task - 1)

            update_task = input("\nEnter Updated Task: ")
            tasks.insert(change_task - 1, update_task)

            # tasks[change_task] = update_task

            print(f"\nTask Updated: {update_task}\n")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            continue

        elif features_selected == 4:
            if not tasks:
                print("\nNo Tasks Available!\n")
                continue

            for num, task_3 in enumerate(tasks, start=1):
                print(f"{num} - {task_3}")
            
            print("\n")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            continue

        elif features_selected == 5:
            save_path = input("\nEnter save path (Leave blank for current folder): ").strip()
            
            if '"' in save_path:
                save_path = save_path.replace('"', '')

            if not save_path:
                save_path = "."
            else:
                save_path = os.path.expanduser(save_path)
                if not os.path.exists(save_path):
                    print(f"\nDirectory doesn't exist. Creating: {save_path}")
                    os.makedirs(save_path, exist_ok=True)

            file_name = input("Enter Name for File: ")
            file_name = file_name.strip()

            with open(f"{file_name}.txt", "w") as file:
                for num, task_5 in enumerate(tasks, start=1):
                    file.write(f"\nProject {num} - {task_5}")

            if save_path == ".":
                print(f"\nSaved Successfully to: Current Folder")

            else:
                print(f"\nSaved Successfully to: {save_path}")

            print("\n" + "="*15 + " Coded 1by: Basant Jangra " + "="*15)      
            continue

        elif features_selected == 6:
            print("\nSee You Next Time!")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            exit()
            
        else:
            print("Invalid Value! Enter Value as Per Format Only.")
            print("\n" + "="*15 + " Coded by: Basant Jangra " + "="*15)
            continue
            
    except KeyboardInterrupt:
        print("\nProgram Closed by User.")
        break

    except ValueError:
        print("Enter Value as Per Requested Format Only.")
        continue

    except IndexError:
        print("\nTask Number Not Found!")
        continue
