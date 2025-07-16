print("hi")

"""💻 Project 1: contact_sorter.py

📝 Description:
You’ll take a dictionary of names → numbers, and print the sorted list alphabetically by name.

☑️ Requirements:
Define a function get_contacts() → returns a sample dictionary (5+ items)
Define a function sort_contacts(contacts: dict) → returns sorted list of names
Define a function display_sorted(contacts: dict) → prints each name + number in order
Use if name == "main" to run your logic

🧠 Bonus:
Add option to sort by number instead of name
Use input() to ask user how they want to sort"""

"--------------------------------------------------------------------------"

"""ok i didnt know we could use sort function for the dicts too and the idea was to
    make two differetn loops for keys and values to sort them out and add them into
    two different lists ; and then make a new empty list and add them by their indexes .
    but this way all the contacts and numbers will get mixed up cause they will be only
    sorted by their own natuar which is letters and numbers  . if we then assign [0] to
    the other list [0] they wont be the corresponding name and number which they originally
    were to each other 

    def sort_contacts(contact_list: dict,Sorted_by_numbers: bool,)->list:     
        for contact in contact_list:
            contacts_sorted=[]
            contact+=contacts_sorted
        contacts_sorted.sort()

        return contacts_sorted"""

"------------------------------------------------------------------------------"

def get_contacts()->dict:
    return            {"hasan":209320,
                       "lawda":400934,
                       "lassan":230923,
                       "cloud":20394,
                       "developer":209320}

def sort_contacts(contact_list:dict,sorted_by_number:bool,)->list:
    if sorted_by_number==True:
        return sorted(contact_list.items(), key=lambda item:item[1])
    #so here in this line i had hundreds of questions so yeah
        """first of all i asked does sorted() always return a list?
        the answer was yes ; 
        then i asked what does .items() return the key or value ;
        so what happens after you use it with a dict ; it return a view object ;
        the view object displays a list of the dictionarys key-value pairs as tuples . 
        
        it makes a tuple (imagine tuple as like , an evolved knight from clash royale
        bro has armor on) of both the key and the value as a couple
         ---
          next i was like what is key=lambda ; so lambda makes a tiny no name function for one time
          use and the item is the variable that we pass into that function ; 
          and after we write color thats the end of that function and after the colon there is a
          return which returns the 2nd item which is positioned in index 1 ; that is numbers
          of the contact list here 
            so just like x ; where i used item ; i can name the item anything ?
            or it must be named item to cycle through the positions ; and also 
            ne more thing ; what is key ; are there other things that i can replace \
            lambda with by writing key=somethingElseIDK
        YES . i can 100% rename the item to anything as i takes anything """
    else:
        return sorted(contact_list.items())






def main():
    while True:
        #while true if kinda just means starting from somewhere knwoing ure gonna go on until ure told to stop
        #its like saying "as youre alive uve to keep on living"

        user_input=input(f"Do you want the list to be sorted by numbers ? y/n : ").strip().lower()
        if user_input in ['y','n']:
            break
        else:
            print("X Invalid Input. Please enter 'y' or 'n' . ")
    """if user enters y then code will sort the results by numbers"""

    sorting_choice=user_input=="y"
# 🧠 My thought process:
# Wait, why is sort_by_number = user_input == "y" a Boolean?
# Isn't user_input just a string?
# Ohhh… so user_input == "y" is a comparison, and comparisons return True or False.
# So that whole expression becomes a boolean.
# So if I did something like user_input > 0, that would also return True or False?
# Meaning I can assign any comparison to a variable, and that variable becomes a boolean.
# That's clean as hell — now I get it.

    print (sorting_choice) #chekcing if user input (boolean) is correct or not
    ContactList=get_contacts()
    print(sort_contacts(ContactList,sorting_choice))












if __name__=="__main__":
    main()