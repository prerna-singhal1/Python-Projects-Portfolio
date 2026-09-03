class Book:
    def __init__(self, title, author, number):
        self.title = title
        self.author = author
        self.number = number
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __gt__(self, other):
        return self.number > other.number
    
    def __lt__(self, other):
        return self.number < other.number
    
    def __add__(self, other):
        return f"Pages = {self.number + other.number}"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "number of pages":
            return self.number
        else:
            return print("You have entered something that wasn't found.")

Book_1 = Book("The kid who came from space", "Ross Welford", 400)
Book_2 = Book("Journey to the Sideways World", "Ross Welford", 360)
Book_3 = Book("1984", "George Orwell", 380)

