
# 14. N-th Character Removal
# Practice Problem: Write a program to remove the character at index i from a string.
# str1 = "Python" 

# i = 2
# s=""
# for i_ in range(len(str1)) :
#     if i_ !=i :
#         s+=str1[i_]
# print(s)

        
# 15. String Partitioning
# Practice Problem:
# Use the .partition() method to split a string into three parts: the part before a separator, 
# the separator itself, and the part after it.

# str1 = "username@company.com"
# sep = "@"

# print(str1.partition(sep))


# 16. Extract File Extension
# Practice Problem: Given a filename as a string, extract only the file extension (e.g., .png or .pdf).

# file_name = "report_final_v2.pdf"
# r = file_name.split(".")
# print(r[-1])



# 17. Lowercase First
# Practice Problem: 
# Write a program to arrange string characters such that all lowercase letters come first, 
# followed by all uppercase letters.

# str1 = "PyNaTive"
# s =[]
# c =[]
# for ch in str1:
#     if ch.isupper():
#         c.append(ch)
#     else:
#         s.append(ch)
# print("".join(s+c))

# 18. Count all letters, digits, and special symbols from a given string
# Practice Problem: 
# Write a program to
#  count all letters, digits, and special symbols from a given string.

# str1 = "P@#yn26at^&i5ve"

# ss = 0
# d = 0
# l= 0

# for i in str1:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         ss+=1

# print(l,d,ss)

#19. Create a mixed string using alternating characters
#Practice Problem: Given two strings, s1 and s2,
#create a third string made of the first char of s1, then the last char of s2, 
#Next, the second char of s1 and the second-to-last char of s2, and so on. 
#Any left-over chars go at the end of the result.

# s1 = "Abc" 
# s2 = "Xyz"
# r = ""
# if len(s1)>len(s2):
#     l = s1
# else:
#     l =s2
# s2 = s2[::-1]
# for i  in  range(l) :
#     if i < len(s1):
#         r +=s1[i]
#     else:
#         r +=s2[i]
# print(r)



# l = [1,2,3,4,5,6]
# r = []
# for i in range(len(l)-1,-1,-1) :
#     r.append(l[i])
# print(r)
    

