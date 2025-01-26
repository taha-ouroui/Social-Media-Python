import os
import time

from BetterInputs import BetterInputs
from MediaManager import MediaManager
from User import User
from Post import Post

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MainMenu():
    while True:
        print("\n--- Social Media Platform ---")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        print("\nProgrammed by Ouroui Mohammed Taha")
        print("-----------------------------")

        choice : int = BetterInputs.input_int("Choose an option: ", "Invalid digit. Please try again.")

        if choice == 1:
            SignUp()
        elif choice == 2:
            LogIn()
        elif choice == 3:
            MediaManager.SaveUsers()
            MediaManager.SavePosts()
            MediaManager.SaveFriends()
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

def SignUp():
    clear()
    print("\n--- Sign Up ---")
    name : str = input("Enter your name: ")
    email : str = input("Enter your email: ")
    password : str = input("Enter your password: ")
    print("-----------------------------")

    new_user = User(name, email, password, True)
    status: bool = MediaManager.AddUser(new_user)
    
    if not status:
        del new_user
    else:
        UserMenu(new_user)

def LogIn():
    clear()
    print("\n--- Log In ---")
    email : str = input("Enter your email: ")
    password : str = input("Enter your password: ")

    user : User = MediaManager.ConnectUser(email, password)
    
    if user is not None:
        UserMenu(user)
    
def UserMenu(user : User):
    while True:
        print("\n--- User Menu ---")
        print("1. Post")
        print("2. View Feed")
        print("3. Add Friend")
        print("4. View Friends")
        print("5. Log Out")
        print("-----------------------------")

        choice : int = BetterInputs.input_int("Choose an option: ")

        if choice == 1:
            CreatePost(user)
        elif choice == 2:
            ViewFeed(user)
        elif choice == 3:
            AddFriend(user)
        elif choice == 4:
            ViewFriends(user)
        elif choice == 5:
            MediaManager.DisconnectUser(user)
            print(f"Goodbye, {user.name}!")
            break
        else:
            print("Invalid option. Please try again.")

def CreatePost(user : User):
    clear()
    print("\n--- Create Post ---")
    print("1. Text Post")
    print("2. Image Post")
    print("-----------------------------")

    choice : int = BetterInputs.input_int("Choose an option: ","Invalid digit. Please try again.")

    if choice == 1:
        content = input("Enter your post content: ")
        user.Post(content=content)
        print("Post created successfully!")
    elif choice == 2:
        url = input("Enter the image URL: ")
        user.Post(url=url)
        print("Image post created successfully!")
    else:
        print("Invalid option. Returning to the user menu.")

def ViewFeed(user : User):
    clear()
    print("\n--- Your Feed ---")
    feed : list[Post] = user.GetFeed()

    if feed:
        for post in feed:
            post.Display()
            
    print("-----------------------------")

def AddFriend(user : User):
    clear()
    print("\n--- Add Friend ---")
    friendName : str = input("Enter the name of the friend to add: ")

    for potentailFriend in MediaManager.users:
        if potentailFriend.name == friendName and potentailFriend != user:
            user.AddFriend(potentailFriend)
            return
    
    print("ERROR: USER NOT FOUND!")

def ViewFriends(user : User):
    clear()
    print("\n--- Your Friends ---")

    if user.friends and len(user.friends) > 0:
        for friend in user.friends:
            print(friend.name)
    else:
        print("You have no friends yet.")

if __name__ == "__main__":
    MediaManager.Load()
    MainMenu()