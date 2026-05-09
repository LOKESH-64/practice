# print 1 to 10
# n=1
# while n<=10:
#     print(n) 
#     n+=1

#print 10 to 1
# n= 10
# while n>=1:
#     print(n)
#     n-=1 

# Print all even numbers from 1 to 20
# n= 2 
# while n<=20:
#     print(n,end=' ')
#     n+=2

# Print all odd numbers from 1 to 20
# n= 1 
# while n<=20:
#     print(n,end=' ')
#     n+=2


# Print numbers from 1 to N (take N as input)
# x= int(input("enter a number: "))
# n = 1
# while n<=x:
#     print(n)
#     n+=1 

#Find the sum of first N numbers
# n = int(input("enter a number:"))
# i=1
# total=0
# while i<=n:
#     total+=i 
#     i+=1
# print("sum",total)

#Find the factorial of a number
# n = int(input("enter a number:"))
# i =1
# fact = 1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#Count how many numbers are divisible by 3 between 1 and N

# n = int(input("enter a number:"))
# i = 1 
# count = 0
# while i<=n:
#     if i%3==0:
#         count+=1
#     i+=1
# print(count)

#Find the sum of even numbers from 1 to N
# n = int(input("enter a number :"))
# i = 2 
# total = 0
# while i <=n:
#     total+=i
#     i+=2
# print(total)


#Print the multiplication table of a number

# n = int(input("enter a number :"))
# i =1 
# while i<=10:
#     print(f"{n}x{i}={n*i}") 
#     i+=1


#Count the number of digits in a number

# n= int(input("number :"))
# count =0
# while n>0:
#     count+=1
#     n//=10
# print(count)


#12. Reverse number
# n = int(input("enter a number :"))
# rev = 0
# while n>0:
#     digit = n%10
#     rev = re


# 13.Find the sum of digits

# n= int(input("enter a number :"))
# t=0
# while n>0:
#     s=n%10
#     t+=s
#     n=n//10
# print(t)


# 14.Check if a number is palindromeExample: 121 → Yes

# n= int(input("number:"))
# o = n 
# rev = 0
# while n>0:
#     rev =rev*10+(n%10)
#     n//=10
# if o==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# 15.Find the largest digit in a number
# n= int(input("number:"))
# large=0
# while n>0:
#     d=n%10
#     if d>large:
#         large=d
#     n//=10
# print(large)

# 16.Stop when user enters 0
# while True:
#     n= int(input())
#     if n==0:
#         break

#17.skip the multiples of 5 
# i = 1 
# while i<=20:
#     if i% 5 ==0 :
#         i+=1
#         continue 
#     print(i)
#     i+=1

# 18. First number divisible by 3 and 7
# i = 1 
# while i<=100:
#     if i%3==0 and i%7==0:
#         print(i)
#         break
#     i+=1

#19.guessing game 
# n = 7 
# while True:
#     g=int(input())
#     if g==n:
#         print("correct")
#         break
#     else:
#         print("incorrect")


#20.prime number 
