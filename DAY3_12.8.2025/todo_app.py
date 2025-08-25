"""
Plan

Store tasks in a file so they persist after you close the program.
Load tasks into a list when the app starts.
Show a menu (Add, View, Remove, Quit).
Write changes back to file after each update.
Use with open() for clean file handling.
"""
"=============================================================================="

def import_tasks()->list:
    return ["eat your food", "drink water", "wash them dishes"]



def view_todo_list(tasks_list:list)->None:
    serial_number=1

    for idx, task in enumerate(tasks_list,start=1):
        print(f"{idx}) {task}")


"""i just wrote this for loop thinking it would result in that output and it did 
IN FIRST TRY
i missed a space in between tho
but damn
holy
but i want to store this print structure in a single variable ;
so i can just print it whenever by printting a variable instead of writing this
whole for loop everytime
how do i do that ; will figure out later ; for now imma just skip it and just finish
 the skeleton first ; """

"=============================================================================="



def add_tasks_in_todo_list(tasks_list:list)->list:
    task_to_be_added_in_the_tasksList = input("Enter task you want to add in your ToDo List : ")
    tasks_list.append(task_to_be_added_in_the_tasksList)
    
    
    print(f"Your Updated List Down Below - ")
    serial_number=1
    for task in tasks_list :
        print (f"{serial_number}) {task}")
        serial_number+=1


"=============================================================================="



def remove_task_in_todo_list(tasks_list:list)->list:

    picked_task_to_remove=int(input(f"Enter the ID of task you want to remove : "))
    del tasks_list[picked_task_to_remove-1]

    for idx,task in enumerate(tasks_list,start=1):
        print(f"{idx}) {task}")




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

        elif user_choice_on_menu=="3":
            remove_task_in_todo_list(tasks_list)
        
        elif user_choice_on_menu=="q":
            #quit_the_program()

            break #this means this loop of continuously asking for user input will only break if user input matches these options; only then it would go further into next step . 
        else:
            print ("Invalid Input . Try Again .")





if __name__=="__main__":
    main()