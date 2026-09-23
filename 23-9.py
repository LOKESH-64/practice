# list comprehension

# print([i*i for i in range(1,6)])
# l = ["lokesh","sai","hari", "babu"]
# r =[i.upper()for i in l]
# print(r)



# r = [ i for i in range(1,11) if i%2==0]
# print(r)

# l = [10,20]
# print(list(enumerate(l)))

# stocks = [True,False,True,False,True,False]
# # r = [i for i in stocks if i ==True]
# # print(list(enumerate(r)))
# r = [x for x,y in enumerate(stocks) if y]
# print(r)



# p = [("laptop",20000),("mobile",22000),("tab",15000)]
# r  =[item for item,price in p if price>15000]
# print(r) 

p = [{"name":"laptop","price":20000,"color":["red","green"]},
     {"name":"mobile","price":30000,"color":["blue","orange"]},
     {"name":"tab","price":20000,"color":["husiyapink","light paleplue"]}]

# # for i in p:

# #  if i['stocks']>0:
# #      print(i["name"])
    

# r= [i['name'] for i in p if i['stocks']>0]        
# print(r)

# r = [pro_color for product in p 
#       for pro_color in product['color']]
# print(r)

# for i in  range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print("Hello")


# Practice Problem: Write a script to perform the following three operations on given list

# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty
# numbers = [10, 20, 30, 40, 50]
# print(numbers[2])
# print(len(numbers))
# lis_emp = len(numbers)==0
# print(f"is the list empty,{lis_emp}")


# Exercise 2. Perform List Manipulation
# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.


# l = [100, 50, 400, 500]

# l[1]=200
# print(l)
# l.append(600)
# print(l)
# l.insert(3,600)
# print(l)
# l.remove(600)
# print(l)
# l.pop(0)
# print(l)

# Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

# Exercise Purpose: Aggregation is the heart of data science. This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.



# n= [10, 20, 30, 40, 50]
# s=sum(n)
# avg=len(n)
# print(s)
# print(s/avg)



# Exercise 4. Find Maximum and Minimum from List
# Practice Problem: Identify the largest and smallest numerical values within a provided list.

# Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, or detecting “outlier” data points in a dataset.

# l =  [45, 12, 89, 2, 67]

# # print(max(l))
# # print(min(l))

# h= l[0]

# # s=0
# for i in l:
# #     print(l[i])
#    if i > h:
#       h = i
# print(h)


# l = [45, 12, 89, 2, 67]
# s = l[0] 

# for i in range(len(l)):
#     if l[i] < s:
#         s = l[i]
# print(s)

# for i in l :
#     if i >s:
#         s= i 
# print(s)





# Exercise 5. Calculate the Product of All Elements
# Practice Problem: Multiply every number in a list together to find the total product.


# f = [2,3,5,7] 

# m =1

# for i in f :
#    m= i*m
# print(m)


# Exercise 6. Count Even and Odd Numbers
# Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

# n = [10, 21, 4, 45, 66, 93, 11]


# e = 0 
# o = 0

# for i in n :
#     if i %2==0:
#         e+=1
#     else:
#         o+=1
# print(o,e)

# Exercise 7. Reverse a List
# Practice Problem: Take a list and reverse the order of its elements.
# l =[100, 200, 300, 400, 500]
# r=[]
# for i in range(len(l)-1,-1,-1) :
#     r.append((l[i]))
# print(r)


# Exercise 8. Sort a List of Numbers
# Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

# l= [56, 12, 89, 3, 22]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


# Exercise 9. Create a Copy of a List
# Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.


# o = ["a","b"]
# n = o.copy()
# print(n)


# Exercise 10. Combine Two Lists
# Practice Problem: Merge two separate lists into a single, unified list.


l  = ["physics",'chemistry']
l2 = ['maths','biology']
n=[]
for i in range(len(l)):
    