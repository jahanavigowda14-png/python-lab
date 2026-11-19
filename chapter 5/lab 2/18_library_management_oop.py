class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print("Book added")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print(book)

    def search_book(self, title):
        if title in self.books:
            print("Book available")
        else:
            print("Book not found")


library = Library()

while True:
    print("\n1.Add Book")
    print("2.Display Books")
    print("3.Search Book")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book name: ")
        library.add_book(title)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        title = input("Enter book name: ")
        library.search_book(title)

    elif choice == 4:
        break

    else:
        print("Invalid choice")