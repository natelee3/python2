phone_book = {}

main_menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
"""


running = True

while running == True:

    print(main_menu)

    user_selection = int(input("What do you want to do? (1-5) "))

    if user_selection == 1:
        name = input("Name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("That name does not appear. Please choose option 2 to add a new entry.\n") 
    elif user_selection == 2:
        new_name = input("Name to add: ")
        if new_name in phone_book:
            print("That name is already in the phonebook. Try again. ")
        else: 
            phone_book[new_name] = input("Phone number to add for " + str(new_name) + ": ")
    elif user_selection == 3:
        delete_name = input("Name to delete: ")
        if delete_name in phone_book:
            del phone_book[delete_name]
        else:
            print("That name doesn't appear in the phonebook. Try again.")
    elif user_selection == 4:
        if phone_book != {}:
            print(phone_book)
        else:
            print("There doesn't appear to be anything here. ")
    elif user_selection == 5:
        print("Thanks for using the phonebook app. Bye.")
        running = False
    else:
        print("Please choose an option 1-5.")
        user_selection = input("What do you want to do? ")

