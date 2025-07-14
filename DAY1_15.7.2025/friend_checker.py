"""friends = ["rafi","orbi" , "Bluvi" , "tera" , "maka " , "bhosdra "]"""




def get_friends_list():
    """this way by storing the list inside another funtion allows us to upgrade
    our code in the future . such as if we decide to import the names from a txt file ;
    we would only have to add that functionality inside here and the rest of the code
    would just run the same ; thats why its important to make this a habit """
    return["rafi","orbi" , "Bluvi" , "tera" , "maka " , "bhosdra "]

def is_friend(name: str, friend_list: list)->bool:
    """checks if the given name is in the friends list"""
    return name in friend_list

def display_friend_checker(name:str,friend_list:list)->None:
    """here we return none cause this funtion only displays things and doesnt return anyth"""
    if is_friend (name,friend_list):
        print(f"{name} is in your friend list")
    else:
        print(f"{name} is not your friend list")
    print(f"you had {len(friend_list)} friends in your friend list in total )")
    
def main():
    friendsNames=get_friends_list()
    user_name_input=input("enter the name you want to search : ").strip()
    """strip just removes all the spaces from front and end ; litrally strips down
    the word to make it look better"""
    display_friend_checker(user_name_input,friendsNames)


if __name__=="__main__":
    """"this looks wierd but make a habit of it ; it just means run the functions if they
    are ran only if they are directly run on this page ."""
    main()