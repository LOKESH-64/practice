# def bill_gen():
#     items = []
#     n = int(input("enter the number of items "))
#     for i in range (n):
#         name = input("enter item name:")
#         price = float(input("enter price :"))
#         qyt = int(input("enter qyt:"))
#         items.append({"name":name,"price":price,"qyt":qyt})
        
#     total = 0
#     print("\n------BILL------")
#     print("date:",datetime.date.today()) 
# bill_gen()
import random

users = {}

def generate_otp():
    return random.randint(1000, 9999)


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {"password": password, "profile": {}}
    print("Registration successful!")


def login():
    username = input("Enter username: ")

    if username not in users:
        print("User not found!")
        return None

    choice = input("Login using (1) Password (2) OTP: ")

    if choice == "1":
        password = input("Enter password: ")
        if password == users[username]["password"]:
            print("Login successful!")
            return username
        else:
            print("Wrong password!")

    elif choice == "2":
        otp = generate_otp()
        print("OTP:", otp)
        entered = int(input("Enter OTP: "))
        if entered == otp:
            print("Login successful!")
            return username
        else:
            print("Invalid OTP!")

    return None


def update_profile(username):
    if username:
        key = input("Enter field (age/email/etc): ")
        value = input("Enter value: ")
        users[username]["profile"][key] = value
        print("Profile updated!")


def logout():
    print("Logged out successfully!")


# Main Program
while True:
    print("\n1.Register 2.Login 3.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        register()
    elif ch == "2":
        user = login()
        if user:
            update_profile(user)
            logout()
    elif ch == "3":
        break
    else:
        print("Invalid choice")