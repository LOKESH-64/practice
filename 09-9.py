# 1. Create a string made of the first, middle, and last character

# s = "james"
# m = int(len(s)/2)
# print(s[0]+s[m]+s[-1])



# 2. Create a string made of the middle three characters
# Practice Problem: 
# Write a program to create a new string made of the middle three characters of an input string of odd length.

# s = "lokesh_tata"
# mid = int(len(s)//2)
# if   mid %2==0:
#      False
# else:
#     print(s[mid:mid+3])


# 3. Append new string in the middle of a given string
# Practice Problem:
#  Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.
# s1 = "Ault" 
# s2 = "Kelly"
# m=int(len(s1)//2)
# print(s1[:m]+s2+s1[m:])

#Exercise 4.Create a new string made of the first, middle, and last characters of each input string
# s1 = input()
# s2 = input() 
# f = s1[0]+s2[0]
# m =s1[int(len(s1)//2)] +s2[int(len(s2)//2)]
# e = s1[-1]+s2[-1]

# print(f+m+e)

# 5. Reverse a given string
# Practice Problem: Write a program to reverse a given string.
# s = "LOKESHTATA"
# s1= s.split()

# print((s1[-1]+s1[0]))
# print(s1[::-1])

# # 6. Find the last position of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# f = str1.rfind("Emma")
# print(f)

# 7. Split a string on hyphens
# Practice Problem: Write a program to split a given string on hyphens and display each substring.

# str1 = "Emma-is-a-data-scientist"
# s = str1.split("-")
# for i in s :
#     print(i)

# 8. Find all occurrences of a substring in a given string by ignoring the case
# Practice Problem: Write a program to find the total count of the substring “USA” in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).
# str1 = "Welcome to USA. usa awesome, isn't it?"
# s = str1.strip().lower()
# print(s.count("usa"))

# 9.String characters balance test
#Practice Problem: Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character’s position doesn’t matter.

# s1 = "yNl"
# s2 = "PyNative"
# # s = "ynf"
# # ss = "PyNative"


# f = True
# for i in s1:
#     if i in s2 :
#        continue
#     else:
#         f= False
#         break
# print(f)

# 10. Vowel Counter
# Practice Problem:
#  Write a program to count the total number of vowels (a, e, i, o, u) in a given string.

# str1 = "Hello World"

# v = "aeiouAEIOU"

# c = 0

# for i in str1 :
#     if i in v:
#         c+=1
# print(c)

# 11. Prefix/Suffix Check
# Practice Problem: Check if a given URL starts with “https” and ends with “.com”.

# str1 = "https://google.com"
# if str1.startswith("http")and str1.endswith(".com"):
#     print("valid url")
# else:
#     print("not valid url")



# 12. Swap Case
# Practice Problem: Write a program to toggle the case of all characters in a string (uppercase becomes lowercase and vice versa).

# Exercise Purpose: This demonstrates Case Transformation. Though simple, it is often used in search algorithms to normalize data or in text editors to provide “Toggle Case” functionality.

# Given Input: str1 = "PyThOn"


# str1="PyThOn"
# r = ""
# for i in str1:
#     if i.isupper():
#         r+=i.lower()
#     else:
#         r+=i.upper()
# print(r)



#  13. Remove Whitespace
# Practice Problem: 
# Remove every single space from a given string, including spaces between words.
# Exercise Purpose: This highlights the difference between Trimming and Filtering.
# While .strip() only removes leading/trailing spaces, .replace() can reach inside a string to remove characters globally.

# str1 = " P y t h o n "
# s= str1.replace(" ","")
# print(s)


# str1 = " p y t h o n "
# r = ""
# for i in str1 :
#     if i =="":
#         r+=i
# print(r)


# 14. N-th Character Removal
# Practice Problem: Write a program to remove the character at index i from a string.
str1 = "Python" 




