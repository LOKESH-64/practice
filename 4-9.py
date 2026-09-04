# def demo (name,age):
#     print(f"my name is {name} and age is {age} ")
# demo ("lokesh",21)


# 2. Variable Length of Arguments (*args)
# Practice Problem: Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.

# def func1(*n):
#     for i in n:
#         print(i)

# func1(15,20,30,40,50)

# Exercise 3. Return Multiple Values from a Function
# Practice Problem: Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.


# def calculation (a,b):
#     return a+b,a-b

# print(calculation(40,10))



# Exercise 4. Function with Default Argument
# Practice Problem: Create a function show_employee() that accepts an employee’s name and salary. If the salary is not provided in the function call, the function should automatically assign a default value of 9000.

# def show_emp(name,salary=9000):
#     print(f"Name:{name},salary:{salary}")

# show_emp("lokesh")
# show_emp("lokesh",30000)
          
# Exercise 5. Create an Inner Function
# Practice Problem: Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates the addition of a and b. The outer function should then add 5 to that sum and return the final result.



# def out(a,b):
#     def inn(a,b):
#         return a+b
#     inn=inn(a,b)
#     return inn+5
# res = out(5,10)
# print(res)





# 6. Create a Recursive Function
# Practice Problem: Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a function that calls itself to solve smaller instances of the same problem.


# def rec(n):
#     if n :
#         return n+rec(n-1)
#     else:
#         return 0


# print(rec(10))