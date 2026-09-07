"""
While Loop Answers
==================
This file contains sample solutions for each question in whileloops.py.
These are beginner-friendly answers that focus on while loop logic.
"""

# ---------------------------------------------------------
# BASIC LEVEL ANSWERS
# ---------------------------------------------------------

def q1():
    i = 1
    while i <= 10:
        print(i, end=' ')
        i += 1
    print()


def q2():
    i = 10
    while i >= 1:
        print(i, end=' ')
        i -= 1
    print()


def q3():
    i = 1
    while i <= 20:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
    print()


def q4():
    total = 0
    i = 1
    while i <= 50:
        total += i
        i += 1
    print("Sum from 1 to 50 =", total)


def q5():
    product = 1
    i = 1
    while i <= 5:
        product *= i
        i += 1
    print("Product from 1 to 5 =", product)


def q6():
    correct_password = "python123"
    password = ""

    while password != correct_password:
        password = input("Enter password: ")
        if password != correct_password:
            print("Wrong password! Try again.")
    print("Access granted!")


def q7():
    num = 0
    count = 0

    while num < 100:
        num += 1
        count += 1

    print("It took", count, "steps to reach 100.")


def q8():
    n = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1


def q9():
    total = 0
    num = int(input("Enter a number (0 to stop): "))

    while num != 0:
        total += num
        num = int(input("Enter a number (0 to stop): "))

    print("Total =", total)


def q10():
    word = input("Enter a word: ")
    vowels = "aeiouAEIOU"
    count = 0
    i = 0

    while i < len(word):
        if word[i] in vowels:
            count += 1
        i += 1

    print("Vowel count =", count)


# ---------------------------------------------------------
# INTERMEDIATE LEVEL ANSWERS
# ---------------------------------------------------------

def q11():
    items = []
    choice = ""

    while choice != "3":
        print("\n1. Add item\n2. View items\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item: ")
            items.append(item)
            print("Item added.")
        elif choice == "2":
            print("Your items:", items)
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid choice.")


def q12():
    secret = 7
    guess = 0

    while guess != secret:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You guessed it!")


def q13():
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose operation: ")

        if choice == "5":
            print("Thank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result =", a + b)
        elif choice == "2":
            print("Result =", a - b)
        elif choice == "3":
            print("Result =", a * b)
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print("Result =", a / b)


def q14():
    total = 0
    count = 0
    num = 0

    while num >= 0:
        num = int(input("Enter a number (negative to stop): "))
        if num < 0:
            break
        total += num
        count += 1

    print("Total =", total)
    print("Count =", count)


def q15():
    n = int(input("Enter a number: "))
    is_prime = True

    if n < 2:
        is_prime = False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1

    if is_prime:
        print(n, "is prime.")
    else:
        print(n, "is not prime.")


def q16():
    num = int(input("Enter a number: "))
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    print("Reversed number =", reversed_num)


def q17():
    n = int(input("Enter a number: "))
    fact = 1
    i = 1

    while i <= n:
        fact *= i
        i += 1

    print(f"Factorial of {n} = {fact}")


def q18():
    mark = -1
    while mark < 0 or mark > 100:
        mark = int(input("Enter a valid mark from 0 to 100: "))
        if mark < 0 or mark > 100:
            print("Invalid mark. Try again.")
    print("Valid mark entered:", mark)


def q19():
    rows = 5
    i = 1
    while i <= rows:
        j = 1
        while j <= i:
            print('*', end='')
            j += 1
        print()
        i += 1


def q20():
    text = input("Enter a sentence: ")
    count = 0
    i = 0

    while i < len(text):
        count += 1
        i += 1

    print("Character count =", count)


# ---------------------------------------------------------
# ADVANCED LEVEL ANSWERS
# ---------------------------------------------------------

def q21():
    balance = 1000
    while True:
        print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose option: ")

        if choice == '4':
            print("Exiting ATM.")
            break
        elif choice == '1':
            print("Balance:", balance)
        elif choice == '2':
            amt = int(input("Enter deposit amount: "))
            balance += amt
            print("Updated balance:", balance)
        elif choice == '3':
            amt = int(input("Enter withdraw amount: "))
            if amt <= balance:
                balance -= amt
                print("Withdraw successful. Balance:", balance)
            else:
                print("Insufficient balance.")
        else:
            print("Invalid option.")


def q22():
    score = 0
    question_num = 1
    total_questions = 3

    while question_num <= total_questions:
        answer = input(f"Question {question_num}: 2 + 2 = ")
        if answer == '4':
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
        question_num += 1

    print("Final score:", score)


def q23():
    import random
    import string

    while True:
        choice = input("Generate password? (y/n): ")
        if choice.lower() == 'n':
            print("Stopped generating passwords.")
            break

        length = int(input("Password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        print("Generated password:", password)


def q24():
    cart = []
    total = 0

    while True:
        print("\n1. Add item\n2. Remove item\n3. View total\n4. Exit")
        choice = input("Choose option: ")

        if choice == '4':
            print("Cart closed.")
            break
        elif choice == '1':
            item = input("Item name: ")
            price = float(input("Item price: "))
            cart.append((item, price))
            total += price
        elif choice == '2':
            if not cart:
                print("Cart is empty.")
            else:
                item_name = input("Enter item to remove: ")
                for item in cart:
                    if item[0] == item_name:
                        cart.remove(item)
                        total -= item[1]
                        break
        elif choice == '3':
            print("Cart:", cart)
            print("Total:", total)
        else:
            print("Invalid choice.")


def q25():
    while True:
        secret = 7
        attempts = 0
        guess = 0

        while guess != secret:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < secret:
                print("Too low")
            elif guess > secret:
                print("Too high")
            else:
                print("Correct! Attempts:", attempts)

        again = input("Play again? (y/n): ")
        if again.lower() != 'y':
            print("Game over.")
            break


def q26():
    products = {1: ("Water", 10), 2: ("Snack", 25), 3: ("Candy", 15)}
    money = 0

    while True:
        print("\n1. Water - $10\n2. Snack - $25\n3. Candy - $15\n4. Exit")
        choice = input("Choose product: ")

        if choice == '4':
            print("Vending machine closed.")
            break

        if choice in products:
            item, price = products[int(choice)]
            money = int(input("Insert money: "))
            if money >= price:
                print("You bought:", item)
                print("Change:", money - price)
            else:
                print("Not enough money.")
        else:
            print("Invalid product.")


def q27():
    import random

    tries = 0
    while True:
        roll = random.randint(1, 6)
        tries += 1
        print("Rolled:", roll)
        if roll == 6:
            print("You got a 6 after", tries, "tries.")
            break


def q28():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0

    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            attempts += 1
            print("Invalid login. Attempts left:", 3 - attempts)

    if attempts == 3:
        print("Locked out.")


def q29():
    books = []
    while True:
        print("\n1. Add book\n2. Remove book\n3. List books\n4. Exit")
        choice = input("Choose option: ")

        if choice == '4':
            print("Library closed.")
            break
        elif choice == '1':
            book = input("Enter book name: ")
            books.append(book)
        elif choice == '2':
            remove_book = input("Enter book to remove: ")
            if remove_book in books:
                books.remove(remove_book)
                print("Book removed.")
            else:
                print("Book not found.")
        elif choice == '3':
            print("Books:", books)
        else:
            print("Invalid choice.")


def q30():
    room = "start"
    inventory = []

    while room != "exit":
        if room == "start":
            move = input("You are at the start. Go left or right? ")
            if move.lower() == "left":
                room = "forest"
            else:
                room = "cave"
        elif room == "forest":
            item = input("You found a key. Pick it up? (y/n): ")
            if item.lower() == 'y':
                inventory.append('key')
                print("Key added to inventory.")
            room = "exit"
        elif room == "cave":
            print("You were trapped! Game over.")
            break

    print("Game ended. Inventory:", inventory)


# ---------------------------------------------------------
# EXAMPLE CALLS (SAFE TO RUN)
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Sample runs for non-interactive questions:\n")
    q1()
    q2()
    q3()
    q4()
    q5()
    q7()
    q12()
    q15()
    q16()
    q17()
    q19()
    q20()
    q22()
    q27()
