"""📌 Day 8 Task: Transaction Logger
Create a simple Python program that:

Starts with a variable balance = 1000.
Uses a loop to let the user add or subtract money.
Input "deposit" → ask how much to add.
Input "withdraw" → ask how much to subtract.
Input "exit" → stop the program.
Every time a transaction happens, store it in a list of strings like:
["Deposited 200 → Balance: 1200", "Withdrew 100 → Balance: 1100"]
When the program ends, print the full transaction history."""


"========================================================================="


def account_balance()->int:
    return 1000



def program_names()->list:
    return ["Show Balance","Deposit","Withdraw" , "Exit"]


def  account_deposit(amount,current_balance)->int:
    return (amount+current_balance)

def  account_withdraw(amount,current_balance)->int:

    """if amount>current_balance:
        return"""#was adding a condition that wihtdrawal amount cant be larger than account balance
    return (current_balance-amount)





def main():
    current_balance = account_balance()
    program_names_in_a_list = program_names()
    program_names_display = "\n".join (f"{idx}) {program_names_in_a_list}" for idx,program_names_in_a_list in enumerate (program_names_in_a_list, start=1) )

    print ("__________________________")
    print()
    print(program_names_display)
    print ()
    transactions = []
    while True : 


        user_program_choice = input ("Enter the ID of the program you want to use : ").lower().strip()

        if user_program_choice == "1":

            try:

                print (f"Your Current Balance Is : {current_balance}")
                print ("__________________________")
                print()

            except ValueError :
                print ("Enter a valid Input")



        elif user_program_choice == "2":

            try:
                deposit_amount = int(input (f"Amount of Money you want to Deposit : "))
                total_after_deposit = account_deposit(deposit_amount,current_balance)

                print()
                print (f"Your Current Balance Is : {total_after_deposit}")
                current_balance = total_after_deposit
                transactions.append(f"Deposited {deposit_amount} → Balance: {current_balance}")

                print ("__________________________")
                print()
            except ValueError :
                print ("Enter a valid Input")


        elif user_program_choice == "3":

            try:
                withdraw_amount = int(input (f"Amount of Money you want to Withdraw : "))
                total_after_withdraw = account_withdraw(withdraw_amount,current_balance)

                print()
                print (f"Your Current Balance Is : {total_after_withdraw}")
                current_balance = total_after_withdraw
                transactions.append(f"Deposited {withdraw_amount} → Balance: {current_balance}")

                print ("__________________________")
                print()
            except ValueError :
                print ("Enter a valid Input")
        
        elif user_program_choice == "q" or user_program_choice=="quit" or user_program_choice == "4" :
            break
        








if __name__=="__main__":
    main()