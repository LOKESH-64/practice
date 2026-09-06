import random
gussing_number = random.randint(1,4)

print("_________WELCOME TO RANDOM GUESSING GAME___________")

# count = 1
# while True :
#     user =  int(input("enter your guessing number :"))
#     if gussing_number==user:
#         print("hurray you have guessed the number ")
        
#         break
#     else:
#         print("guess again ")
#     count+=1

    
# print("your guess counnt",count)

user = int(input("How many guesses you would take to guess:"))
for i in range(user):
    u= int(input("enter your guessing number"))

    if gussing_number!=u:
        print("guesss again")
    elif gussing_number==u:
        
        print(f"hurray you have guessed your number under {user} ")
        break
    