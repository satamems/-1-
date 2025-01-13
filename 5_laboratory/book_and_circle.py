class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")
    

class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius: float):
        self.radius = radius