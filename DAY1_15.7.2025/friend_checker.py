"""friends = ["rafi","orbi" , "Bluvi" , "tera" , "maka " , "bhosdra "]"""




def get_friends_list():
    return["rafi","orbi" , "Bluvi" , "tera" , "maka " , "bhosdra "]

def is_friend(name: str, friend_list: list)->bool:
    """checks if the given name is in the friends list"""
    return name in friend_list

def display_friend_checker(name:str,friend_list:list)->None:
    if is_friend (name,friend_list):
        print(f"{name} is in your friend list")
    else:
        print(f"{name} is not your friend list")
    print(f"you had {len(friend_list)} friends in your friend list in total )")
    
def main():
    friendsNames=get_friends_list()
    user_name_input=input("enter the name you want to search : ").strip()
    display_friend_checker(user_name_input,friendsNames)


if __name__=="__main__":
    main()