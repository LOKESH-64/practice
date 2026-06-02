""" 
Function is a block of code which  only runs when it is called .

types of functions :

1) user defines function  :
2) pre defined function   :

user defined fucntion:
----------------------
Function which is defined by user  to perform the specific task is known as user defined function.
In python a function is defined with def keyword .
the main use of the function concept is reusability 

how to create a function :
-------------------------
def functionname (parmeters):   ----------> called function  
    block of code 

how to call function :
----------------------
we can call function by using functionname(arguments) ---> i.e, calling function 

arguments are also called positional arguments 

> we can call the the functions in deiifern=ent ways 
 1)calling function with arguments and with returntype
 2)calling function with arguments and without return type 
 3)calling function without arguments with return type 
 4)calling function without arguments and without return type 

""" 
# write a python function message to disp;ay o/p as hello world 

# def  F123(): # called function
    
#     return "hello world"
# print(F123()) # calling function





# calling function with arguments and with returntype:
# write a python function that is sum of 2 numbers 
# def Sum(a,b):
#     c = a+b 
#     return c
# print(Sum(3,6))


# print("start")
# def s (a,b):
#     c = a+b 
#     return c 
# print("middle ")
# a = int(input())
# b = int(input())
# print("first call",s(a,b))
# print("end")
# print("second call")
# print(s(a,b))

# calling function with arguments and without returntype:
# def sub (a,b):
#     s = a-b
#     print(s)
# sub(10,1)

# calling function without arguments and without return type :

# def Welcome():
#     x = int(input())
#     n = input()
#     city = input()
#     print(f"hello my name is {n}, i am  from {city}, i am {x} years old thank you!! ")

# Welcome()  

# calling function without arguments with return type :
# def greet():
#     x = input()
#     return f"wish you a very good luck to you {x}"

# o=greet()
# print(o)
# print(greet())


# def f() :
#     return "welcome to hyd "
#     print("end") # unreachable 

# r =f() 
# print(r)
# print("hey")


""" Defualt Parameter Value :
------------------------------
 Here we will assign defualt value to parameter and it will be used by the function , when we call the function  without any arguments.
   """
# def message (c="India"):
#     print("my country name is",c)
# message('usa')
# message()


"""pass statement :
---------------------
If we dont know what code will write inside the function definition in that cases we will use pass statement
When we want to create the function placeholder without any code then we will use pass statement """ 

# def m():
    # pass 


""" arguments are also called positional arguments  """
# 
def n(fname,lname):
    print(fname)
    print(lname)

n("lokesh","T")


""" key word arguments 
"""