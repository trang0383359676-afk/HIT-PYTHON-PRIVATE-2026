#bai1
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_borrowed = False
        self.history = []
    def describe(self):
        return f"{self.title} - {self.author}"
    @property
    def is_borrowed(self):
        return self._is_borrowed
    def borrow(self):
        if self._is_borrowed == False:
            self._is_borrowed == True
            self.history.append("borrow")
            return True
        return False
    def return_book(self):
        if self._is_borrowed == True:
            self._is_borrowed = False
            self.history.append("return")
            return True
        return False
    
a = Book("Python cơ bản", "Linh")
b = Book("Git thực hành", "Hà")
print(a.borrow())
print(a.borrow())
print(b.is_borrowed)
print(a.return_book())
print(a.is_borrowed)
print(a.return_book())
print("Lịch sử sách a:", a.history)
print("Lịch sử sách b:", b.history)
