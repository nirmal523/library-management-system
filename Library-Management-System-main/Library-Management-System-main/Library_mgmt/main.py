from controller.book_controller import BookController

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            BookController.add_book()
        elif choice == "2":
            BookController.view_books()
        elif choice == "3":
            BookController.search_book()
        elif choice == "4":
            BookController.delete_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print("Error:", e)
