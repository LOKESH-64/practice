# An ATM allows a withdrawal only if:

# the amount is a multiple of 5

# the balance is enough to cover the amount plus service charge

# Question:
# What decision should the ATM take if the amount is valid but the balance is insufficient?
# Which block (if or else) runs, and why?

# amount = 1500.10 
# balance = 100.0
# if amount%5 == 0 and balance >=amount+0.5:
#     print("cash withdrwal")
# else:
#     print("balance insufficient ") 


# 2️⃣ Classroom Attendance — (continue)

# A teacher takes attendance from roll number 1 to 10.
# Roll number 6 is absent.

# Question:
# What should the teacher do at roll number 6 so that attendance continues normally for the rest of the students?

# for roll in range(1, 7):
#     if roll == 4:
#         continue
#     print("Present:", roll)


# 3️⃣ Searching a Name in a List — (break)

# You are checking names one by one in a list to find a specific student.
# Once the student is found, no further checking is needed.

# Question:
# Which keyword should be used, and what happens to the loop after it is used?
# names = ["A", "B", "C", "D"]

# for name in names:
#     if name == "C":
#         print("Found")
#         break
#     print("Checking", name)


# 4️⃣ Online Order Processing — (continue)

# An online store processes orders.
# Orders below ₹500 should be ignored, but higher-value orders must still be handled.

# Question:
# When a low-value order appears, should the loop stop or skip?
# Which keyword correctly represents this behavior?

# l = [200,300,400,500,1000,2000,4000,5000]
# for i in l:
#     if i<=500:
#         continue
#     print('processed',i)

n = 1234
num=n
result = 0
while num>0:
    id =num%10
    result = result*10 +id
    num = num//10
print(result) 

