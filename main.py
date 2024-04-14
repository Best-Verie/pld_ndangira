from auth.auth import register, login

from services.account.management import change_password, update_profile, update_account_status
from services.jobs.jobs import createJob, getJobs, get_jobs_by_title, get_open_jobs, updateJobById,get_companies, closeJobById

user_id = None

def adminPanel():
    print("=============================================================================")
    print("|                   Admin Panel                                             |")
    print("=============================================================================")
    print("| 1. Create Positions                                                       |")
    print("| 2. Update positions                                                       |")
    print("| 3. View Positions                                                         |")
    print("| 4. Close By Job Id                                                        |")
    print("| 5. Go back to main menu                                                   |")
    print("| 6. Exit                                                                   |")
    print("=============================================================================")

    while True:
        choice = input("Choose option: ")
        if choice == '1':
            print("\Welcome to admin panel/ Positions creation !\n")
            createJob()
            break
        elif choice == '2':
            print("\nUpdate positions still under construction!\n")
            print_menu()
            break
        elif choice == '3':
            print("\nView Positions still under construction!\n")
            print_menu()
            break
        elif choice == '4':
            job_id = input("Enter job id: ")
            closeJobById(job_id)
            print_menu()
            break
        elif choice == '5':
            print_menu()
            break
        elif choice == '6':
            print("\nBye!\n")
            print_menu()
            break
        else:
            print("\nInvalid option!\n")
            adminPanel()

def print_menu():
    print("==============================================================================")
    print("|                   Ndangira Job Search                                      |")
    print("==============================================================================")
    print("| 1. Register                                                                |")
    print("| 2. Login                                                                   |")
    print("| 3. Job Management                                                          |")
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
    print("| 2. Update profile                                                          |")
    print("| 3. Update account status                                                   |")
    print("| 4. Go back to main menu                                                    |")
    print("| 5. Exit                                                                    |")
    print("==============================================================================")



    while True:
        choice = input("Choose option: ")
        if choice == '1':
            change_password()
            manage_account()
            break
        elif choice == '2':
            update_profile()
            manage_account()
            break
        elif choice == '3':
            update_account_status()
            manage_account()
            break
        elif choice == '4':
            print_menu()
            break
        elif choice == '5':
            print("\nBye!\n")
            print_menu()
            break
        else:
            print("\nInvalid option!\n")
            manage_account()

def view_jobs():
    print("=============================================================================")
    print("|                   Job Search and Discovery                                |")
    print("=============================================================================")
    print("| 1. Open Positions                                                         |")
    print("| 2. Add Jobs                                                               |")
    print("| 3. Browse Companies                                                       |")
    print("| 4. Application status                                                     |")
    print("| 5. View positions                                                         |")
    print("| 6. Go back to main menu                                                   |")
    print("| 7. Exit                                                                   |")
    print("=============================================================================")

    while True:
        choice = input("Choose option: ")
        if choice == '1':
            get_open_jobs()
            view_jobs()
            break
        elif choice == '2':
            createJob()
            view_jobs()

            break
        elif choice == '3':
            get_companies()
            view_jobs()
            break
        elif choice == '4':
            print("\nApplication status still under construction!\n")
            view_jobs()
            break
        elif choice == '5':
            getJobs()
            view_jobs()
            break
        elif choice == '6':
            print_menu()
            break
        elif choice == '7':
            print("\nBye!\n")
            print_menu()
            break
        else:
            print("\nInvalid option!\n")
            view_jobs()

#Choices

if __name__ == '__main__':
    choice = '7'
    while True:
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            view_jobs()
            break
        elif choice == '4':
            manage_account()
        elif choice == '5':
            print("\nDelete account still under construction!\n")
            break
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

def adminPanel():
    print("=============================================================================")
    print("|                   Admin Panel                                             |")
    print("=============================================================================")
    print("| 1. Create Positions                                                       |")
    print("| 2. Update positions                                                       |")
    print("| 3. View Positions                                                         |")
    print("| 4. Go back to main menu                                                   |")
    print("| 5. Exit                                                                   |")
    print("=============================================================================")

    while True:
        choice = input("Choose option: ")
        if choice == '1':
            # print("\Welcome to admin panel/ Positions creation !\n")
            createJob()
            break
        elif choice == '2':
            # print("\nUpdate positions still under construction!\n")
            updateJobById()
            break
        elif choice == '3':
            # print("\nView Positions still under construction!\n")
            getJobs()
            break
        elif choice == '4':
            print_menu()
            break
        elif choice == '5':
            print("\nBye!\n")
            adminPanel()
            break
        else:
            print("\nInvalid option!\n")
            adminPanel()