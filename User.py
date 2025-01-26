from datetime import datetime

from Post import Post
from TextPost import TextPost
from ImagePost import ImagePost

class User:
    def __init__(self, name : str, email : str, password : str, status : bool) -> None:
        self.name : str = name
        self.email : str = email
        self.__password : str = password
        
        self.status : bool = True
        self.friends : list[User] = []
        self.posts : list[Post] = []

    @property
    def password(self) -> str:
        return self.__password
    
    def AddFriend(self, friend: "User"):
        
        # if connected
        if self.status:
            
            # if connected, then we check if we have that friend already
            if friend in self.friends:
                print(f"ERROR: YOU ALREADY FRIENDS WITH ({friend.name})!")
                return
                
            # if we don't, then we add each other
            self.friends.append(friend)
            friend.friends.append(self)
            
            print("SUCCESS: FRIEND ADDED")
            return
                
        print("ERROR: NOT CONNECTED")
    
    def Post(self, content : str = None, url : str = None):
        
        # if connected
        if self.status:
            
            # if there is no URL, then we are dealing with a text message
            if url is None and not content is None:
                
                newPost = TextPost(self.name, content)
                self.posts.append(newPost)
                print("SUCCESS: TEXT POST POSTED!")
                return
            
            elif not url is None and content is None:
                
                # if there is, then it's an image post
                newPost = ImagePost(self.name, "", None, url)
                self.posts.append(newPost)
                print("SUCCESS: IMAGE POST POSTED!")
                return
        
        print("ERROR: NOT CONNECTED")
    
    def GetFeed(self) -> list[Post] :
        
        # checking if the user has any posts
        if len(self.posts) > 0:
            
            organizedFeed : list[Post] = []
            
            for post in self.posts:
                organizedFeed.append(post)
            
            # organizing the feed
            organizedFeed.sort(key=lambda post: datetime.strptime(post.time, "%Y-%m-%d %H:%M:%S"), reverse=True)
            
            print("SUCCESS: GOT FEED")
            return organizedFeed
        else:
            print("ERROR: THIS USER DOESN'T HAVE ANY POSTS!")
            return None