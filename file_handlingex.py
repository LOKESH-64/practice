import re
def validate_username(name):
    pattern = r'^[a-zA-Z0-9_]{3,15}$'
    return re.match(pattern, name)

def validate_age(age):
    pattern = r'^(?:1[01][0-9]|120|[1-9]?[0-9])$'
    return re.match(pattern, age)

def validate_DOB(dob):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(pattern, dob)

def validate_gender(gender):
    pattern = r'^(Male|Female|Other)$'
    return re.match(pattern, gender)

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{8,}$'
    return re.match(pattern, password) is not None

def validate_phone(phone):
    pattern = r'^[6-9][0-9]{9}$'
    return re.match(pattern, phone) is not None


def register_user():
    user_data = {}
    
    while True:
        name = input("Enter your username: ")
        if validate_username(name):
            user_data['username'] = name
            break
        else:
            print("Invalid username. Please enter a valid username.")

    while True:
        age = input("Enter your age: ")
        if validate_age(age):
            user_data['age'] = age
            break
        else:
            print("Invalid age. Please enter a valid age between 1 and 119.")

    while True:
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        if validate_DOB(dob):
            user_data['dob'] = dob
            break
        else:
            print("Invalid date of birth format. Please enter in YYYY-MM-DD format.")
    
    while True:
        gender = input("Enter your gender (Male/Female/Other): ")
        if validate_gender(gender):
            user_data['gender'] = gender
            break
        else:
            print("Invalid gender. Please enter Male, Female, or Other.")

    while True:
        email = input("Enter your email: ")
        if validate_email(email):
            user_data['email'] = email
            break
        else:
            print("Invalid email format. Please try again.")
    
    while True:
        password = input("Enter your password: ")
        if validate_password(password):
            user_data['password'] = password
            break
        else:
            print("Password must be at least 8 characters long and contain both letters and numbers. Please try again.")
            
    while True:
        phone = input("Enter your phone number: ")
        if validate_phone(phone):
            user_data['phone'] = phone
            break
        else:
            print("Invalid phone number format. Please try again.")
        
    
    
    with open('users.txt', 'a') as file:
        file.write(str(user_data) + '\n')
    
    print("Registration successful!")

register_user()