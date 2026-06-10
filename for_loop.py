# 🔹 1. BASIC LOOPING PROBLEMS
# 1. Print numbers from 1 to 10

# for i in range(1,11):
#     print(i,end=' ')
"------------------------------------"
# 2. Print even numbers (1–50)
# for i in range(1,51):
#     if i%2==0:
#         print(i,end=' ')
# for i in range(2,51,2):
#     print(i,end=' ')
"--------------------------------------"
# 3. Sum of first N numbers
# n = int(input())
# sum=0
# for i in range(1,n+1):
#     sum = sum +i
# print(sum)
"----------------------------------------"
# 4. Multiplication table
# n =int(input())
# for i in range(1,11):
#     print(f"{n} X {i} =",n*i)
"----------------------------------------"
# 5.Reverse counting from N to 1 5,4,3,2,1.
# n= int(input())
# for i in range(n,0,-1):
#     print(i)
"--------------------------------------------"
# 6. Print each character of a string
# n = input()
# for i in n:
#     print(i,end=' ')
"--------------------------------------------"
# 7.Find factorial of a number
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
"----------------------------------------------"
# 8.Count digits in a number
# n= int(input())
# c=0
# while n>0:
#     n=n//10
#     c+=1
# print(c)
# n= int(input())
# c = 0 
# for i in range(len(str(n))):
#     c+=1
# print(i)

# n= int(input())
# s=len(str(n))
# print(s)
"-----------------------------------------------"
# 9.Sum of digits of a number
# n=int(input())
# c=0
# while n>0:
#     d=n%10
#     c=c+d
#     n=n//10
# print(c)
"--------------------------------------------------"
# 10.Check if a number is prime
# n= int(input())
# if n<=1:
#     print("Not a prime")
# else:
#     for i in range(2,n):
#         if n%i==0:
#             print("not a prime")
#             break
#     else:
#      print("prime")
"---------------------------------------------------"     

    

x = input().strip()
pass_five=x[:5]
# d= False
# for i in x:
#     if i.isdigit():
#         d=True:
print(pass_five)


    