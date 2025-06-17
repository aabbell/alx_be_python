class book:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    
    def __del__ (self):
        print(f"Deleting {self.title}")
    
    def __str__():
        print(f"{self.title} by {self.author} published in {self.year}")
    
    def __repr__():
        print(f"Book('{self.title}', '{self.author}', {self.year})")

        