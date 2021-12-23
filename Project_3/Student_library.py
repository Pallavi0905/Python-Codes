class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry! This book is not either not avaliable or has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book. Hope you enjoying reading this book.")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book        

if __name__ == "__main__":
    centralLibrary = Library(["Algorithm", "Maths", "Physics", "Chemistry", "Biology", "clrs", "Django"])
    centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        WelcomeMessage = '''==== Welcome to Central Library ====
        Please choose an option:
        1. List all the books.
        2. Request for a book.
        3. Add/Return a book.
        4. Exit the library.
        '''
        print(WelcomeMessage)

        a = int(input("Enter the choice: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central Library! Have a good day ahead.")
            exit()
        else:
            print("Invalid Choice!")