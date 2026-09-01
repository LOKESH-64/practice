# Exercise 16. Numerical Palindrome Check
# Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
# Case 1: number = 121

# n= int(input())
# ori=n
# rev =0
# while n >0:
#     d= n%10
#     rev = rev*10+d
#     n//=10
# if ori==rev:
#     print("palindrome num")
# else:
#     print("not a palindrome")


# n=int (input())
# ori = str(n)
# if ori[::-1]==ori:
#     print("palindrome")
# else:
#     print("not a palindrome")

# 17. Merging Lists with Parity Filtering
# Practice Problem: Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second 

# l1 = [10, 20, 25, 30, 35]
# l2 = [40, 45, 60, 75, 90]
# new= []
# for i in  l1 :
#     if i %2!=0:
#        new.append(i)
# for i in l2:
#     if i %2==0:
#         new.append(i)

# print(new)


#  18. Integer Digit Extraction and Reversal
# Practice Problem: Write a program to extract each digit from an integer in the reverse order.

# number = 7536
# Expected Output: 6 3 5 7


# n = int(input())
# d= 0
# while n>0:
#     d=n%10
#     n= n//10
#     print(d,end="")




# 19. Multi-Tiered Income Tax Calculation
# Practice Problem: Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax
# Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

# i = int(input())

# if i <=10000:
#     t = 0

# elif i<=20000:
#     t= (i-10000)*10//100
# else:
#     t= 10000 *10//100
#     t=t+(i-20000)*20//100
# print(t)

#  Print a multiplication table from 1 to 10 in a formatted grid

# for i in range(1,11):
#     for j in range(1,11):
#         print(j*i,end=" \t")
#     print("\n")




