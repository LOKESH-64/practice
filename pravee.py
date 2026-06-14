# 🔹 Level 1 – Basic If Conditions
# 1️⃣ Write a program to check whether a number is even or odd.
# 2️⃣ Write a program to check whether a number is positive, negative, or zero.
# 3️⃣ Write a program to check whether a person is eligible to vote (age ≥ 18).
# 4️⃣ Write a program to find the largest of two numbers.
# 5️⃣ Write a program to check whether a number is divisible by 5.


# 1️⃣ Write a program to check whether a number is even or odd.
# n = int(input())
# if n%2==0:
#     print("even number ")
# else:
#     print("odd number ")

# 2️⃣ Write a program to check whether a number is positive, negative, or zero.
# n = int(input())
# if n>0:
#     print(f"positive number {n}")
# elif n==0:
#     print(f"number is zero {n}")
# else:
#     print(f"negative number {n}")

# 3️⃣ Write a program to check whether a person is eligible to vote (age ≥ 18).
# n = int(input())
# if n >=18:
#     print("you can vote ")
# elif n<=10:
#     print("you have to wait until 18 to vote ")
# else:
#     print("you are minor cannot vote  ")


# 4️⃣ Write a program to find the largest of two numbers.
# a = int(input())
# b = int(input())
# if a>b:
#     print(a)
# elif a==b:
#     print('both are equal')
# else:
#     print(b)

# 5️⃣ Write a program to check whether a number is divisible by 5.
# n = int(input())
# if n%5==0:
#     print("divisible by 5 ")
# else:
#     print("not divisible by 5 ")

# 🔹 Level 2 – Intermediate Conditions
# 6️⃣ Write a program to find the largest of three numbers.

# a,b,c = list(map(int,input().split()))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# 7️⃣ Write a program to check whether a number is a multiple of both 3 and 5.

# n = int(input())
# if n%3==0 and n%5==0:
#     print('divisible by both')
# else:
#     print('not divisible')

# 8️⃣ Write a program to calculate grade based on marks:
# 90+ → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

# marks = int(input())
# if marks>90:
#     print('grade A')
# elif marks >=75 and marks<=90:
#     print('grade B')
# elif marks >=50 and marks<=75:
#     print('grade C')
# else:
#     print("fail")

# 9️⃣ Write a program to check whether a year is a leap year.










# 🔟 Write a program to check whether a character is a vowel or consonant.
# a = input().lower()
# vowels = 'aeiou'
# if a in vowels :
#     print("vowel")
# else:
#     print('consonant') 

# 🔹 Level 3 – Logical Operators in Conditions
# 1️⃣1️⃣ Write a program to check if a number is between 10 and 50.

# n = int(input())
# if n>=10 and n<=50:
#     print(f"no is  b/w  10 to 50 {n} ")
# else:
#     print(f"number is not b/w 10 to 50 -- {n}")

# 1️⃣2️⃣ Write a program to check if a person can apply for a job:
# Age ≥ 21

# age = int(input())
# if age >=21:
#     print('u can apply for job')
# else:
#     print(f" cannot apply for the job. age is  {age}") 


# 1️⃣3️⃣ Write a program to check if a triangle is valid (sum of angles = 180).
# a,b,c = list(map(int,input().split()))
# if a+b+c==180:
#     print("valid triangle")
# else:
#     print("not a valid  triangle")

# l = list(map(int,input().split()))
# # m = list(map(int,input().split()))
# n = len(l)
# n2 = len(m)
# for i in range(n-1):
#     ch = l[i]
# for j in range(n2-1):
#     ch = m[j]
# if l[i]== m[j]:
#     print("sd")
# else:
#     print("pd")

l = [1,2,1,3,2,4]
m = {}
n = len(l)
for i in range(n):
    if l[i] not in m:
        m[l[i]]=1
    else:
        m[l[i]]+=1    
print(m)
        
