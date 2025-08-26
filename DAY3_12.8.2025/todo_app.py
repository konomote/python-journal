"""
Plan

Store tasks in a file so they persist after you close the program.
Load tasks into a list when the app starts.
Show a menu (Add, View, Remove, Quit).
Write changes back to file after each update.
Use with open() for clean file handling.
"""
"=============================================================================="
import os

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
TASKS_FILE=os.path.join(BASE_DIR,"tasks.txt")





def import_tasks(filename=TASKS_FILE):
    try:
        with open(filename,"r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks=[]
    return tasks




def format_todo_list(tasks_list: list) -> str:
    """Return the todo list as a single formatted string"""
    if not tasks_list:
        return "No tasks yet!"
    
    formatted = "\n".join(f"{idx}) {task}" for idx, task in enumerate(tasks_list, start=1))
    return formatted




def save_tasks(tasks, filename=TASKS_FILE):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")



"=============================================================================="


"""in this version i added the print loop for the tasts in a variable; 
and just printed the returned variable from the function called format_todo_list"""

"=============================================================================="




def view_todo_list(tasks_list:list)->None:
    print(format_todo_list(tasks_list))



"=============================================================================="



def add_tasks_in_todo_list(tasks_list:list)->list:
    task_to_be_added_in_the_tasksList = input("Enter task you want to add in your ToDo List : ")
    if task_to_be_added_in_the_tasksList!="":
        tasks_list.append(task_to_be_added_in_the_tasksList)
    #at first i didnt add this if statement ; it added empty string as a task ; this prevents that
    
    print("Your Updated List:")
    print(format_todo_list(tasks_list))
    save_tasks(tasks_list)



"=============================================================================="



def remove_task_in_todo_list(tasks_list:list)->list:

    picked_task_to_remove=int(input(f"Enter the ID of task you want to remove : "))
    del tasks_list[picked_task_to_remove-1]
    print("Your Updated List:")
    print(format_todo_list(tasks_list))
    save_tasks(tasks_list)


"=============================================================================="


def main () :

    tasks_list = import_tasks()

    while True :
        print ("\n1)View 2)Add 3)Remove 4)Quit")
        user_choice_on_menu = input (("Pick a number to go forward : ").strip()).lower()
        print("\n")

        if user_choice_on_menu=="1":
            view_todo_list(tasks_list)

        elif user_choice_on_menu=="2":
            add_tasks_in_todo_list(tasks_list)
            save_tasks(tasks_list)


        elif user_choice_on_menu=="3":
            remove_task_in_todo_list(tasks_list)
            save_tasks(tasks_list)

        
        elif user_choice_on_menu=="q" or user_choice_on_menu=="4" :
            break #this means this loop of continuously asking for user input will only break if user input matches these options; only then it would go further into next step . 
        
        else:
            print ("Invalid Input . Try Again .")





if __name__=="__main__":
    main()