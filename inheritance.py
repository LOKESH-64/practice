"""
parent class --  child class 

super class --  sub class 

base class -- derived class 

types :
1) single or simple inheritance 
2) multi-level inheritance
3) multiple inheritance
4) hierarical inheritance
5)mixed or hybrid inhertance 
"""
"""
class data():  # parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("name =",self.name)
        print("age =",self.age)

    def m_1(self,x):
        print("this is method od parent class")
        print("x=",x)
    
        

class data1 (data): #child class
    def __init__(self,number,name,age):
        self.mobile = number
        super().__init__(name,age)

    def full_info(self):
        super().info()
        print("mobile=",self.mobile)

    def m_2(self):
        print("this is child class")

# d1 = data1(103928479,"rak",23)
# # d1.full_info()
# d1.info()

# d1.m_1("lokesh")


d = data("lakshman ",30)
# d.info()
# d.m_1("value given with parent class")

"""
#multi level inheritance

class grandfather ():
    def __init__(self):
        self.name="pavan"
    def m_gf(self):
        print("this is grand father class method ")

class father (grandfather):
    def m_f(self):
        print("this is father class method ")

class child (father):
    def __init__(self):
        self.desg="dev"
        self.__init__()

    def m_c(self):
        print("this is child class method")
        super().m_gf()
    
    def details(self):
        print()
    

# ch = child()
# ch.m_c()
# ch.m_f()
# ch.m_gf()

# f = father()
# f.m_f()
# f.m_gf() 
# f.m_c()

ch1=child()
ch1.m_c()