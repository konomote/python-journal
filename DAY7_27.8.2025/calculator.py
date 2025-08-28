"""👉 Day 7: Build a CLI Calculator that supports +, -, *, /

This means:
User can run your Python file,
Input two numbers and an operator (+ - * /),
Program gives the result.
Extra (optional if you want):
Keep running until the user types exit.
Handle invalid input gracefully."""

"========================================================================="

def program_names()->list:
    return ["Addition (+)","Substraction (-)","Multiplication (*)", "Division (/)" ,"Quit (enter 5/ type quit)"]


"========================================================================="

def adding_numbers_x_and_y( first_number , second_number):
 
    print()
    addition_result=0
    addition_result = first_number + second_number
    print (f"{first_number} + {second_number} = {addition_result}")
    print ("__________________________")
    print()


"=============================================================================="

def substracting_numbers_x_and_y(first_number , second_number)->int:
    total_added=0

    print()
    substraction_result=0
    substraction_result = first_number - second_number
    print (f"{first_number} - {second_number} = {substraction_result}")
    print ("__________________________")
    print()


"=============================================================================="


def multiply_numbers_x_and_y(first_number , second_number):

    print()
    multiplication_result=0
    multiplication_result = first_number * second_number
    print (f"{first_number} x {second_number} = {multiplication_result}")
    print ("__________________________")
    print()


"=============================================================================="


def devide_numbers_x_and_y(first_number , second_number):

    print()
    division_result=0
    division_result += first_number / second_number
    print (f"{first_number} / {second_number} = {division_result}")
    print ("__________________________")
    print()


"=============================================================================="


def main ():

    program_names_in_a_list=program_names()

    

    while True:
        print()
        formatted_program_names= "\n".join(f"{idx}) {program_names_in_a_list}" for idx,program_names_in_a_list in enumerate(program_names_in_a_list,start=1))
        print(formatted_program_names)
        user_program_choice = input("\nEnter the ID of program you want to use : ").lower().strip()


        if user_program_choice=="1":
            try:
                print()
                print("Program Picked : Addition")
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))
                adding_numbers_x_and_y( start,end )

            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()

        elif user_program_choice=="2":
            try:
                print()
                print("Program Picked : Substraction")
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))
                substracting_numbers_x_and_y( start,end )

            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()

        elif user_program_choice=="3":
            try:
                print()
                print("Program Picked : Multiplication")
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))
                total = multiply_numbers_x_and_y( start , end )

            except ValueError:
                print("Enter a valid number to continue , try agian.")

        elif user_program_choice=="4":
            try:
                print()
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))
                total = devide_numbers_x_and_y( start , end )

            except ValueError:
                print("Enter a valid number to continue , try again.")
                #while upgrading this function to print in the main statement ; i thought to myself that 
#this for loop on top is what i got and practiced with chatgpt ;
#what bothers me is idk if this line is getting assigned with the return value the multiplication function is returning
#if so does it only print after all ten lines get printed or it prints every line for every loop ?
            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()


        elif user_program_choice=="q" or user_program_choice=="5" or user_program_choice=="quit":
            break
        #if user inputs q then the program quits itself


        else:
            print("Please enter a valid number.")


"=============================================================================="





if __name__=="__main__":
    main()