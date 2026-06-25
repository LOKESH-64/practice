# def fn_1(a="a",b="b"):               # required  , default , arbitrary* , keyword args 
#     x = a 
#     y = b
#     return a,b

# print(fn_1(100,200)) 

# print(fn_1(b=20,a=10))

# print(fn_1(100 , b=200))



# def fn_2(a,b=200):
#     print("a =",a)
#     print("b =",b)


# fn_2(b=10,a=200)


# a,*b,c = 10,20,30,40,50
# print(a,b,c)


# def fn_1(*a):                                    
#     print("x=",a)
# fn_1(24234,4434) 



# key word arguments or kwargs  or variable length arguments
# def fn(**a):
#     print("a =",a)

# fn(x=10,y=20,s ='hello')


def fn_4(x,y="defualt",*z,**d):
    print('x=',x)
    print('y=',y)
    print('z=',z)
    print('d=',d)

fn_4(100,200,300,400,500,a="fsad",b="jkh",c='sadf') 