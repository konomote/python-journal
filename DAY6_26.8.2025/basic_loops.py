"""Day 6 (Aug 26): Loops Basics ✅ Today

Topics: for, while, break, continue
Practice Exercises:
Print numbers 1 to 20 using a loop
Sum numbers 1 to 100
Print multiplication table for a number
Loop through a list of strings and print each"""
#i thought that making a program picker for these would be better ;
#that way i can implement the last requirement in a list of strings with program names. 



def program_names()->list:
    return ["Print Numbers (from-to)","Sum Numbers (from-to)","Print Multiplication Table (any number with range limit 10)","Quit (enter 4/q)"]


"========================================================================="

def printing_numbers_from_x_to_y(start_printing_from , end_printing_at):
 
    print()
    for number in range (start_printing_from , end_printing_at):
        print (number)
    print ("_________________________________________________________________________")
    print()


"=============================================================================="

def summing_numbers_from_x_to_y(start_adding_from , end_adding_at)->int:
    total_added=0

    for number in range (start_adding_from , end_adding_at+1):
        total_added+=number
    return total_added


"=============================================================================="


def multiplication_table(number, multiplication_limit):
    for idx in range(1, multiplication_limit+1):
        print(f"{number} x {idx} = {number*idx}")
    print ("_________________________________________________________________________")


"=============================================================================="


def main ():
    print ("_________________________________________________________________________")

    program_names_in_a_list=program_names()
    
    

    while True:
        print()
        formatted_program_names= "\n".join(f"{idx}) {program_names_in_a_list}" for idx,program_names_in_a_list in enumerate(program_names_in_a_list,start=1))
        print(formatted_program_names)
        user_program_choice = input("\nEnter the ID of program you want to use : ").lower().strip()
        print ("_________________________________________________________________________")


        if user_program_choice=="1":
            try:
                print("Program Picked : Print numbers")
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))+1
                printing_numbers_from_x_to_y( start,end )

            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()

        elif user_program_choice=="2":
            try:
                print("Program Picked : Sum numbers")
                start = int (input("  starting number : "))
                end =   int (input("  ending number : "))
                total = summing_numbers_from_x_to_y( start,end )
                print(f"{start}+{start+1}...{end} = {total}")
                print ("_________________________________________________________________________")

            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()

        elif user_program_choice=="3":
            try:
                print("Program Picked : Multiplication Table")

                multiplication_limit=10
                user_input_for_multiplication_table = int (input("  Of which number : "))
                multiplication_table( user_input_for_multiplication_table,multiplication_limit )

            except ValueError:
                print ("Enter a valid number to continue , try again.")
                print()


        elif user_program_choice=="q" or user_program_choice=="4":
            break
        #if user inputs q then the program quits itself


        else:
            print("Please enter a valid number.")


"=============================================================================="





if __name__=="__main__":
    main()