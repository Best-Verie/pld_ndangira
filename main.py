from auth.auth import register, login

user_id = None

def print_menu():
    print("==============================================================================")
    print("|                   Ndangira Job Search                                      |")
    print("==============================================================================")
    print("| 1. Register                                                                |")
    print("| 2. Login                                                                   |")
    print("| 3. View All jobs                                                           |")
    print("| 4. Manage your Account                                                     |")
    print("| 5. Delete account                                                          |")
    print("| 6. Clear                                                                   |")
    print("| 7. Menu                                                                    |")
    print("| 8. Exit                                                                    |")
    print("==============================================================================")

def manage_account():
    print("==============================================================================")
    print("|                   Account Management                                      |")
    print("==============================================================================")
    print("| 1. Change password                                                         |")
    print("| 2. Update profile                                                           |")
    print("| 3. Update account status                                                           |")
    print("| 4. Go back to main menu                                                     |")
    print("| 5. Exit                                                                    |")
    print("==============================================================================")
   
    choice = input("Choose option: ")
    while True:
        if choice == '1':
            print("\nChange password still under construction!\n")
            break
        elif choice == '2':
            print("\nUpdate profile still under construction!\n")
            break
        elif choice == '3':
            print("\nUpdate account status still under construction!\n")
            break
        elif choice == '4':
            print_menu()
            break
        elif choice == '5':
            print_menu()
            break
        else:
            print("\nInvalid option!\n")
            manage_account()

if __name__ == '__main__':
    choice = '7'
    while True:
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("\nBye!\n")
        elif choice == '4':
            manage_account()
        elif choice == '5':
            print("\nBye!\n")
        elif choice == '6':
            print("\nBye!\n")
            print_menu()
        elif choice == '7':
            print_menu()
        elif choice == '8':
            print("\nBye!\n")
            break
        else:
            print("\nInvalid option!\n")
        choice = input("Choose option: ")
