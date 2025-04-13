import json


class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Save the book list to a JSON file."""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection."""
        print("\n📖 Add a New Book")
        print("-" * 30)
        book_title = input("📚 Title: ")
        book_author = input("✍️  Author: ")
        publication_year = input("📅 Year: ")
        book_genre = input("🏷️  Genre: ")
        is_book_read = input("✅ Have you read it? (yes/no): ").strip().lower() == "yes"

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully!\n")

    def delete_book(self):
        """Remove a book by title."""
        print("\n🗑️ Delete a Book")
        print("-" * 30)
        book_title = input("Enter the title to remove: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("🗑️ Book removed successfully!\n")
                return
        print("⚠️ Book not found!\n")

    def find_book(self):
        """Search by title or author."""
        print("\n🔍 Search Books")
        print("-" * 30)
        search_type = input("Search by:\n1️⃣ Title\n2️⃣ Author\nChoose (1 or 2): ")
        search_text = input("🔎 Enter search term: ").lower()

        found_books = []
        if search_type == "1":
            found_books = [book for book in self.book_list if search_text in book["title"].lower()]
        elif search_type == "2":
            found_books = [book for book in self.book_list if search_text in book["author"].lower()]
        else:
            print("⚠️ Invalid choice.\n")
            return

        if found_books:
            print("\n📚 Matching Books:")
            for index, book in enumerate(found_books, 1):
                status = "✅ Read" if book["read"] else "📖 Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print("🚫 No matching books found.\n")

    def update_book(self):
        """Update an existing book."""
        print("\n✏️ Update Book Details")
        print("-" * 30)
        book_title = input("Enter the book title to edit: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("🔁 Leave blank to keep current value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]

                read_input = input("Have you read this book? (yes/no): ").strip().lower()
                if read_input in ["yes", "no"]:
                    book["read"] = (read_input == "yes")

                self.save_to_file()
                print("✅ Book updated successfully!\n")
                return
        print("⚠️ Book not found!\n")

    def show_all_books(self):
        """Show all books."""
        print("\n📚 Your Book Collection")
        print("-" * 40)
        if not self.book_list:
            print("📭 Collection is empty.\n")
            return

        for index, book in enumerate(self.book_list, 1):
            status = "✅ Read" if book["read"] else "📖 Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()

    def show_reading_progress(self):
        """Show reading stats."""
        print("\n📈 Reading Progress")
        print("-" * 30)
        total = len(self.book_list)
        completed = sum(1 for book in self.book_list if book["read"])
        progress = (completed / total * 100) if total > 0 else 0
        print(f"📚 Total books: {total}")
        print(f"✅ Completed: {completed}")
        print(f"📊 Progress: {progress:.2f}%\n")

    def start_application(self):
        """Run the app menu loop."""
        while True:
            print("🎉 Welcome to Book Collection Manager 🎉")
            print("=" * 45)
            print("1️⃣  Add a new book")
            print("2️⃣  Remove a book")
            print("3️⃣  Search for books")
            print("4️⃣  Update book details")
            print("5️⃣  View all books")
            print("6️⃣  View reading progress")
            print("7️⃣  Exit")
            print("=" * 45)

            choice = input("👉 Choose an option (1-7): ")

            if choice == "1":
                self.create_new_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.find_book()
            elif choice == "4":
                self.update_book()
            elif choice == "5":
                self.show_all_books()
            elif choice == "6":
                self.show_reading_progress()
            elif choice == "7":
                self.save_to_file()
                print("\n👋 Thanks for using Book Collection Manager. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    try:
        book_manager = BookCollection()
        book_manager.start_application()
    except KeyboardInterrupt:
        print("\n\n👋 Application exited by user. Goodbye!")
