# # dun dum methods  __keyword__
# """
# dun dum methods are pre defined methods whose method name inclated between __prefix and 
# postfix__
# ex: __keyword__ :__init__ __mul__,__str__
# """
# # constructors 
# """
# > A constructor is a special method which is called as instantaneous of the class used to declare instance variables , in python we have a constructor which is 

# > As constructor is amethod itself it should be called to execute its functionality .
# >By defualt 
#   > constructor calling:In python no need of calling of constructor of the class manually  it calls itself whenever the object of the class is created 
#   > Rules:
#    *In a class there should be only one constructor which is decleared as first method of the class for the accesbility of instance variables throught all methods in the class .
#    A constructor should  contain only  instance varibles and constructer should not return any values.
#    If needed the constructor method should accept parameters in it . 

   

# Types of constructors:
# 1) zero parmeterised constructor or empty constructor 
# 2) parmetarised constructor 

# """

# class cl_1():
#     x="class Variable"
#     def __init__(self): # zero parametrized constructor 
#         self.name ="pavan" #instance varibles
#         self.desg ="dev"

#     def m_1(self):    # call with self with in class
#         print("name=",self.name)
#         print("desg=",self.desg)

#     def m_2(self,s):   # call with object with in class
#         print("name=",s.name)
#         print("desg=",s.desg)
# c1=cl_1() #object creation and constructor calling 
# c1.m_1()
# print("out of clqss name =",c1.name)
# print("out of clqss desg =",c1.desg)

# c1.m_2(c1)


# class cl_2():# independent class 
#     def m_4(self):
#         print("method-4 of class-2")
#         print("name=",c1.name)
#         print("desg=",c1.desg)
        
# c2=cl_2()
# c2.m_4()



class cl_1():
    x="class Variable"
    def __init__(self,x,y): #  parametrized constructor 
        self.name =x #instance varibles
        self.desg =y
        self.loc= "hyd"

c1=cl_1("ram",'qa') # object creation & constructor calling

print("out of class c1 name =",c1.name)
print("out of class c1 desg =",c1.desg)
print("out of class c1 loc =",c1.loc)


c2=cl_1("srinu","admin")
print("out of class c1 name =",c2.name)
print("out of class c1 desg =",c2.desg)
print("out of class c1 loc =",c2.loc)

print(cl_1.x)