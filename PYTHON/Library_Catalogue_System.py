# Class definition for Book
class Book:
    def __init__(self, title, author, available=True):
        """Initialize the book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.available = available  # True means the book is available, False means it's checked out

    def display_info(self):
        """Display information about the book."""
        availability = "Available" if self.available else "Checked out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {availability}")

    def checkout(self):
        """Check out the book by updating the availability status."""
        if self.available:
            self.available = False
            print(f"{self.title} has been checked out.")
        else:
            print(f"Sorry, {self.title} is already checked out.")

    def return_book(self):
        """Return the book by updating the availability status."""
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

# Class definition for LibraryCatalogue
class LibraryCatalogue:
    def __init__(self):
        """Initialize the catalogue with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a new book to the catalogue."""
        self.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the catalogue.")

    def display_all_books(self):
        """Display all books in the catalogue."""
        if not self.books:
            print("The catalogue is empty.")
        else:
            print("\nCatalogue of Books:")
            for book in self.books:
                book.display_info()
                print("-" * 40)

# Main function to simulate the scenario
def main():
    # Create an instance of LibraryCatalogue
    library = LibraryCatalogue()

    # Add books to the catalogue
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", False)  # Already checked out

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Display all books in the catalogue
    library.display_all_books()

    # Simulate checking out and returning books
    print("\nChecking out 'The Great Gatsby'...")
    book1.checkout()

    print("\nChecking out '1984'...")
    book2.checkout()

    print("\nReturning 'The Great Gatsby'...")
    book1.return_book()

    print("\nTrying to return '1984' (it was already returned)...")
    book2.return_book()

    # Display all books after some actions
    print("\nDisplaying catalogue after some actions:")
    library.display_all_books()

# Run the main function
if __name__ == "__main__":
    main()
