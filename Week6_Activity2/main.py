has_access = False

def login_required(func):
    def wrapper():
        if has_access:
            func()
        else:
            print("Access not granted. Please Login\n")
    return wrapper

@login_required
def view_salary():
    print("Salary\n")

@login_required
def view_personal_details():
    print("Details\n")

@login_required
def download_report():
    print("Report\n")

view_salary()
view_personal_details()
download_report()

def login():
    global has_access
    has_access = True
    print("Logged in\n")

while True:
    print("1. Login")
    print("2. View Salary")
    print("3. View Personal Details")
    print("4. Download Report")
    option = int(input("Select Option:"))

    if option == 1:
        login()
    elif option == 2:
        view_salary()
    elif option == 3:
        view_personal_details()
    elif option == 4:
        download_report()
    else:
        print("Invalid input")
