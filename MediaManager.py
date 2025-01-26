import csv
import os

from User import User
from TextPost import TextPost
from ImagePost import ImagePost

# filePaths
currentDirectory = os.path.dirname(os.path.abspath(__file__)) # getting current file path
usersFile: str = os.path.join(currentDirectory, "database", "users.csv")
postsFile: str = os.path.join(currentDirectory, "database", "posts.csv")
friendsFile: str = os.path.join(currentDirectory, "database", "friends.csv")

# Helper functions
def FileExists(filePath : str) -> bool :
    return os.path.exists(filePath)

def GetUserFromName(name : str, list : list[User]) -> User:
    for user in list:
        if user.name == name:
            return user
    
    return None

# the actual class
class MediaManager:
    
    #static attribute
    users : list[User] = []
    
    @staticmethod
    def ConnectUser(email : str, password : str) -> User:
        for user in MediaManager.users:
            if user.email == email and user.password == password:
                user.status = True
                print(f"Welcome, {user.name}!")
                return user
        
        print("Invalid email or password. Please try again.")
        return None
    
    @staticmethod
    def DisconnectUser(user : User):
        user.status = False
    
    # method for handling adding users
    @staticmethod
    def AddUser(newUser : User) -> bool:
        
        if newUser in MediaManager.users:
            # the user is already registered!
            print("ERROR: THIS USER IS ALREADY REGISTERED")
            return False
        else:
            
            sameEmailFound = False
            
            # trying to find a matching email
            for user in MediaManager.users:
                if newUser.email == user.email:
                    sameEmailFound = True
                    break
            
            if sameEmailFound:
                print("ERROR: THIS EMAIL ALREADY EXISTS")
                return False
            else:
                # the user is not registered, so we add him/her
                MediaManager.users.append(newUser)
                print("SUCCESS: USER ADDED")
                return True
    
    # method for saving users into csv file
    @staticmethod
    def SaveUsers():
        
        try:
            header = ["name", "email", "password"]
            allUsers : list[dict[str, str]] = []
            
            # getting all info from users
            for user in MediaManager.users:
                userDict : dict[str, str] = {}
                
                # storing all info
                userDict["name"] = user.name
                userDict["email"] = user.email
                userDict["password"] = user.password
                
                allUsers.append(userDict)
                
            
            # opening the csv file
            with open(usersFile, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header, delimiter="|", quotechar='"')
                
                writer.writeheader()
                writer.writerows(allUsers)
                
            print("SUCESS: USERS SAVED")
        except Exception as e:
            print(f"ERROR: SOMETHING OCCURRED WHEN SAVING USERS: {e}")
    
    @staticmethod
    def SavePosts():
        
        try:
            header = ["author", "content", "time", "url"]
            allPosts : list[dict[str, str]] = []
            
            # getting all posts from users
            for user in MediaManager.users:
                for post in user.posts:
                    postDict : dict[str, str] = {}
                
                    # storing all info
                    postDict["author"] = post.author
                    postDict["content"] = post.content
                    postDict["time"] = post.time
                    
                    if isinstance(post, ImagePost):
                        print("saving image")
                        postDict["url"] = post.url
                    else:
                        print("saving text")
                        postDict["url"] = None
                    
                    allPosts.append(postDict)
                
            
            # opening the csv file
            with open(postsFile, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header, delimiter="|", quotechar='"')
                
                writer.writeheader()
                writer.writerows(allPosts)
                
            print("SUCESS: POSTS SAVED")
        except Exception as e:
            print(f"ERROR: SOMETHING OCCURRED WHEN SAVING POSTS: {e}")
    
    @staticmethod
    def SaveFriends():
        try:
            header = ["friender", "friend"]
            allFriends : list[dict[str, str]] = []
            
            # getting all posts from users
            for user in MediaManager.users:
                for friend in user.friends:
                    friendDict : dict[str, str] = {}
                
                    # storing all info
                    friendDict["friender"] = user.name
                    friendDict["friend"] = friend.name
                    
                    allFriends.append(friendDict)
                
            
            # opening the csv file
            with open(friendsFile, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=header, delimiter="|", quotechar='"')
                
                writer.writeheader()
                writer.writerows(allFriends)
                
            print("SUCCESS: FRIENDS SAVED")
        except Exception as e:
            print(f"ERROR: SOMETHING OCCURRED WHEN SAVING FRIENDS: {e}")
    
    @staticmethod
    def Load():
        try:
            
            # loading users
            if FileExists(usersFile):
                with open(usersFile, "r") as file:
                    header = ["name", "email", "password"]
                    reader = csv.DictReader(file, fieldnames=header, delimiter="|")
                    next(reader, None)
                    
                    for row in reader:
                        name = row["name"]
                        email = row["email"]
                        password = row["password"]
                        
                        userAdd = User(name, email, password, False) # instantiating a new user but not connected cuz we are loading
                        MediaManager.users.append(userAdd)
            else:
                print("NO USER DATA FOUND!")
                
            # loading posts
            if FileExists(postsFile):
                with open(postsFile, "r") as file:
                    header = ["author", "content", "time", "url"]
                    reader = csv.DictReader(file, fieldnames=header, delimiter="|")
                    next(reader, None)
                    
                    for row in reader:
                        author : str = row["author"]
                        content : str = row["content"]
                        time : str = row["time"]
                        url : str = row["url"]
                        
                        user : User = GetUserFromName(author, MediaManager.users)
                        
                        if not user is None:
                            if url == "":
                                postAdd = TextPost(author, content, time)
                                user.posts.append(postAdd)
                            else:
                                postAdd = ImagePost(author, content, time, url)
                                user.posts.append(postAdd)
                        
            else:
                print("NO POST DATA FOUND!")
                
            # loading friends
            if FileExists(friendsFile):
                with open(friendsFile, "r") as file:
                    header = ["friender", "friend"]
                    reader = csv.DictReader(file, fieldnames=header, delimiter="|")
                    next(reader, None)
                    
                    for row in reader:
                        friender : str = row["friender"]
                        friend : str = row["friend"]
                        
                        user : User = GetUserFromName(friender, MediaManager.users)
                        friendUser : User = GetUserFromName(author, MediaManager.users)
                        
                        if not user is None and not friendUser is None:
                            user.friends.append(friendUser)
                        
            else:
                print("NO POST DATA FOUND!")
                
            print("SUCCESS: LOADED DATA")
        except Exception as e:
            print(f"ERROR: SOMETHING OCCURRED WHEN LOADING DATA ({e})")
    
    