class cl_1():
    def __init__(self):
        self.name="lokesh" # public instance variable 
        self.__password="s1234" # private instance variable 
        self._friends=["babu","chinnu","guddu"] # protected instance variable 


    def method_call(self):
        print("name=",self.name)
        print("password=",self.__password)
        print("friends=",self._friends)         

c1=cl_1()
# c1.method_call()
# c1.method_call()
# print("name =",c1.name)
# print("friends=",c1._friends)   
# print("password=",c1.__password)

class cl_2():
    def method_cl_2(self):
        print("name=",c1.name)
        print("friends=",c1._friends)  
        print("friends=",c1._friends)  
        print("password=",c1.__password)

c2=cl_2()
c2.method_cl_2()