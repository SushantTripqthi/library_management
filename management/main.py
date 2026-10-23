from library.library import Library
from library.exceptions import LibraryError


def print_list(items, empty_message):
    if not items:
        print(empty_message)
    for item in items:
        print(item)


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        raise LibraryError("Please enter a valid number.")


def show_menu():
    print("\n===== LIBRARY MENU =====")
    print("1. Add book")
    print("2. Register member")
    print("3. Search book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Show all books")
    print("7. Show available books")
    print("8. Show all members")
    print("9. Show books borrowed by a member")
    print("0. Exit")


def main():
    library = Library("City Library")

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                library.add_book(read_int("Book ID: "),
                                 input("Title: ").strip(),
                                 input("Author: ").strip())
                print("Book added.")
            elif choice == "2":
                library.register_member(read_int("Member ID: "),
                                        input("Name: ").strip())
                print("Member registered.")
            elif choice == "3":
                print_list(library.search_books(input("Title or author: ")),
                           "No matching books.")
            elif choice == "4":
                library.borrow_book(read_int("Member ID: "),
                                    read_int("Book ID: "))
                print("Book borrowed.")
            elif choice == "5":
                library.return_book(read_int("Member ID: "),
                                    read_int("Book ID: "))
                print("Book returned.")
            elif choice == "6":
                print_list(library.all_books(), "No books yet.")
            elif choice == "7":
                print_list(library.available_books(), "No available books.")
            elif choice == "8":
                print_list(library.all_members(), "No members yet.")
            elif choice == "9":
                print_list(library.member_books(read_int("Member ID: ")),
                           "This member has no borrowed books.")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except LibraryError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
