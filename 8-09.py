# l = [10,20,30,40,50]
# s= 0
# for i in l:
#     s+=i
# a=s//len(l)
# print(a)

# Use for loop to generate a list of numbers from 9 to 50 divisible by 2.
# for i in range(9,51):
#     if i %2==0 :
#         print(i)


# Example: break the loop if number a number is greater than 15
# numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
# for i in numbers:
#     if i > 15 :
#         break
#     print(i)
    
# name = "mariya mennen"
# c = 0 

# for ch in name:
#     if ch=="m":
#         c+=1
#     else:
#         continue
    
# print(c)

# n = [10,20,30,40,50,60,70,80]
# g = n[0]
# for i in n:
#    if i> g:
#       g=i
# print(g)



# def fun (n):
#     if n<5:
#         return "HIGH"
#     if n>5:
#         return "LOW"
# print(fun(5))



# s =lambda n :n*n
# print(s(5))
# s = lambda a,b:a+b
# print(s(10,30))


d ={ "a":1,"b":2,"c":3,"d":4}
print(tuple(d.items()))