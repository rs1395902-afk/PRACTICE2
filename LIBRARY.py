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
    elif choice == "2":
        #ADD BOOKS
