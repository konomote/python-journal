print ("Day 2 : Project 2 , lesgo")

"""🔨 Project 2 — slicing_trainer.py

🎯 Objective:
Build a Python program to experiment with slicing (strings & lists).

🔧 Functions to Build:
- get_sample_string() → returns "cloudengineering"
- get_sample_list() → returns [10, 20, 30, 40, 50, 60, 70]
- ask_user_for_range() → asks for start, end, step and returns as integers
- slice_string(string, start, end, step) → returns sliced string
- slice_list(lst, start, end, step) → returns sliced list

🧠 Program Flow:
- Ask: "Slice a string or a list?" (loop until user types 'q' or 'quit')
- Show the sample string/list
- Get range inputs from user
- Slice and display result
"""

def get_sample_string()->str:
    return "cloudengineering"
#making seperate function so later i can import from DB or JSON

def get_sample_list()->list:
    return [10, 20, 30, 40, 50, 60, 70]
#making seperate function so later i can import from DB or JSON


def ask_user_for_range():
    start_position_slicing_userchoice=int(input(f"Enter your start position of slicing :").strip())-1
    step__slicing_userchoice=int(input(f"Enter your step of slicing :").strip())
    end_index_slicing_userchoice=int(input(f"Enter your end position of slicing :").strip())+1
    #asking user for the their choices of positions ; adding -1 and +1 to convert positions to slicing indexes . 
    return start_position_slicing_userchoice , step__slicing_userchoice , end_index_slicing_userchoice


def sliced_string(stored_word:str )->str:
    start , step , end = ask_user_for_range()
    return stored_word[start:end:step]
    #we can slice strings but we cant assign another letter to any postion of a string like replacing a letter in a list ; 
    #its becuase strings are immutable ; 

def sliced_list(stored_list:list )->list:
    start , step , end = ask_user_for_range()
    return stored_list[start:end:step]
    #this returns the value as a tuple


def handle_user_choice(choice,stored_word:str,stored_list=list,):
        if choice in ['s','string']:
            print(sliced_string(stored_word)) 
        elif choice in ['l', 'list']:
            print(*sliced_list(stored_list))
        else:
            print("Invalid input. Please select a valid option.")
#this is what happens if the user doesnt enter q/quit to exit the software ; 

    

def main():

    stored_word=get_sample_string()
    stored_list=get_sample_list()
    print(f"This the word saved in the program : {stored_word}")
    print(f"This the list saved in the program : {stored_list}")

    while True:
        #while true simply means ; dont stop until youre told so . 
        program_choice=input(f"Slice a ('s'/'string') string or a ('l'/'list') list? ('q' or 'quit' to quit program) :").strip().lower()
        
        if program_choice in ['q','quit']:
            break
        #means to stop
        
        handle_user_choice(program_choice, stored_word, stored_list) #this isnt else ; this is destined to run regardless until break



        


if __name__=="__main__":
    main()