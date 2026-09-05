# 1. Write a program to find all the even numbers in a list.  
#    *Input*: [1, 2, 3, 4, 5, 6]  
#    *Output*: [2, 4, 6]  
# s=[1,2,3,4,5,6]
# r=[]
# for i in s:
#     if i % 2==0:
       
#         r.append(i)
# print(r)


# 2. Write a program to count the number of elements in a list that are greater than 10 and less than 50.  
#    *Input*: [15, 3, 55, 22, 10, 49]  
#    *Output*: 3  

l = [15,3,55,22,10,49]
c = 0 
for i in l:
    if i>10 and i<50:
        c+=1
print(c)



