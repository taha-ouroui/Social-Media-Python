from abc import ABC, abstractmethod
from datetime import datetime

class Post(ABC):
    def __init__(self, author : str, content : str, time : str = None) -> None:
        self.author : str = author
        self.content : str = content
        
        if time is None:
            self.time : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.time : str = time
    
    @abstractmethod
    def Display(self) -> str:
        pass