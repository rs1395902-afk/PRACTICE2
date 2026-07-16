books = ["PYTHON", "JAVA", "C++", "JAVASCRIPT", "HTML", "CSS"]

while True:         #SHOW THE MENU BAR
    print("\n======LIBRARY MANAGEMENT SYSTEM======")
    print("1. SHOW BOOKS")
    print("2. ADD BOOKS")
    print("3. ISSUE BOOKS")
    print("4. RETURN BOOKS")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE : ") #FOR USER INPUT

    if choice == "1":  #SHOW BOOKS
        print("\nAVAILABLE BOOKS : ")
        for book in books:
            print(book)
    elif choice == "2":  #ADD BOOKS
        new_book = input("ENTER THE NAME OF THE BOOK TO ADD : ")
        books.append(new_book)
        print(f"{new_book} HAS BEEN ADDED TO THE LIBRARY ")
    elif choice == 3:  #ISSUE BOOKS
        issue_book = input("ENTER THE BOOK NAME TO ISSUE : ")
        if issue_book in books:
            books.remove(issue_book)
            print(f"{issue_book} HAS BEEN ISSUED")
        else:
            print("NOT AVAILABLE")
    
       