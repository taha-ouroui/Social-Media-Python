from Post import Post

class ImagePost(Post):
    #override
    def __init__(self, author, content, time, url : str):
        super().__init__(author, content, time)
        self.url : str = url
        
    #override
    def Display(self) -> str:
        print(f"{self.author} posted on {self.time}:\n\"URL:{self.url}\"")