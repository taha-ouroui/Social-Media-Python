from Post import Post

class TextPost(Post):
    # we don't need __init__ cuz we aren't changing it at all
        
    #override
    def Display(self) -> str:
        print(f"{self.author} posted on {self.time}:\n\"{self.content}\"")