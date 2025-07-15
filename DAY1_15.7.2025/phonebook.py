"""🎯 Goal:
Make a Python program that:
Stores a phonebook of 5+ names with numbers
Asks the user to enter a name
Checks if that name exists in the phonebook
If found → print the phone number
If not found → print a “not found” message
Show total contacts at the end"""


def get_contact_list()->dict:
    return            {"hasan":209320,
                       "lawda":400934,
                       "lassan":230923,
                       "cloud":20394,
                       "developer":209320}


    """so idk why but for some reason this structure within what i knew was a set {} is
    called a "Dictionary" pardon if i spelled that wrong but damn . 
            what it does is just the left side is called key and right is called value ; 
            if i for some reason search with the key it will return the corresponding value
            assigned with it .
            
            i have just made the dictionary inside a function so that if in the future ive to
            import data from JSON or DB replacing this sample data while keeping the code intact"""
    



def name_is_in_phonebook(name:str,contact_list:dict)->bool:
    """this function just checks if the variable name is in the this dictionary ; it works
    because in works with both list and dictionaries """
    return name in contact_list
    



def display_contact_search(name: str,contact_list: dict)->None:
    """returns ntohign becuase it only displays things on the terminal """

    if name_is_in_phonebook(name,contact_list) :
            print(f"The number assigned to the username {name} is  : {contact_list[name]}")
    else:
            print(f"Person Doesn't exist")
    
    print(f"You have {len(contact_list)} contacts Added In Your phonebook .")
         



def main():
    ContactDict=get_contact_list()
    user_input_name = input("    Enter the name you want to search in your contact list : ").strip()
    display_contact_search(user_input_name,ContactDict)




if __name__=="__main__":
         """"this looks wierd but make a habit of it ; it just means run the functions if they
    are ran only if they are directly run on this page ."""
         main()
         