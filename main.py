from auth.auth import register, login

user_id = None

def print_menu() :
    print( "==============================================================================")
    print( "|                   Ndangira Job Search                                      |")
    print( "==============================================================================")
    print( "| 1. Register                                                                |")
    print( "| 2. Login                                                                   |")
    print( "| 3. View All jobs                                                           |")
    print( "| 4. Manage your Account                                                     |")
    print( "| 5. Delete account                                                          |")
    print( "| 6. Clear                                                                   |")
    print( "| 7. Menu                                                                    |")
    print( "| 8. Exit                                                                    |")
    print( "==============================================================================")


if __name__ == '__main__':
    print_menu()
    # register()
    login()
