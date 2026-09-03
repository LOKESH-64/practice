# 4 Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

# Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.


# def ss(nam, n):
#     print(nam[n:])


# a = input()
# b = int(input())
# ss(a,b)


# 5Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

# Exercise Purpose: This exercise will help you learn about memory efficiency and Python’s special tuple unpacking feature. In other languages like C or Java, you need a temporary variable to swap values safely. In Python, you can swap values in one line without risking data loss.

# a= int(input())
# b= int(input())
# print("before swap a=",a,"b=",b)
# a,b=b,a
# print(f"after swap a={a},b={b}")


# Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

# Exercise Purpose: This exercise explores “Mathematical Accumulation.” A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing.


# a = int(input())

# f = 1 
# if a ==0:
#     print(f"0 fact is {f}")
# else:

#   for i in range(1,a+1):
#       f= f*i

#   print(f)



# Exercise 7. List Manipulation: Add and Remove
# Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

# Exercise Purpose: This exercise teaches “Dynamic Collection Management.” Lists are rarely static; being able to modify, expand, and prune them is essential for handling data like shopping carts, user lists, or inventory systems.


# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# x = input("add fruit name :")

# fruits.append(x)

# fruits.pop(1)
# print(fruits)




# Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

# Exercise Purpose: This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences, and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 lines of code in other languages.

# a = input()
# # print(a[::-1])
# rev = ""

# for ch in range(len(a)-1,-1,-1)  :
#     rev+=a[ch]

# print(rev)


# Exercise 9. Vowel Frequency Counter
# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

# Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters.



# x= input().strip().lower()
# v = "aeiou"

# c = 0

# for i in x:
#     if i in v:
#         c+=1
# print(c)




# Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

# Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

# Given Input: nums = [45, 2, 89, 12, 7]

# Expected Output: Largest: 89 Smallest: 2


# nums = [45, 2, 89, 12, 7]

# # print(max(nums),min(nums))


# l = nums[0]
# s = nums[0]

# for i in nums :
#     if i > l:
#         l=i
#     if i<s:
#         s=i

# print(l,s)



# Exercise 11. Removing Duplicates from a List
# Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

# data = [1, 2, 2, 3, 4, 4, 4, 5]

# r = []

# for i in data:
#     if i not in r:
#         r.append(i)
# print(r)



#  12. List Comparison and Boolean Logic

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# if numbers_x[0]==numbers_x[-1]:


#  print("result is True ")
# def cmpr(x):
#     if x[0]==x[-1]:
#         return True
#     else:
#         return False

# a = list(map(int,input().split()))

# print(cmpr(a))


# 13. Filtering Lists with Conditional Logic
# Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

# num_list = [10, 20, 33, 46, 55]
# res = []
# for i in num_list:
#     if i %5==0:
#      res.append(i)

# print(res)

#  14. Substring Frequency Analysis
# Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

# Exercise Purpose: Text analysis and pattern matching are core pillars of programming. This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools.


# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))
# print(str_x)
    

# Exercise 15. Nested Loops for Pattern Generation
# Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# a = 5
# for i in range(1,a+1):
#     for j in range(i):
#      print(i,end = " ")

#     print("\n")



for i in range(1,6):
    for j in range(i):
        print(i,end = " ")
    print("\n")

     

