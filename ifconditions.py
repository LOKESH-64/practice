"""conditions and if statements 
#equals a==b
#not equals a!=b
less than:a<b
grater than: a>b
less than or equalto:a<=b
greater than or eqaulto:a>=b """

# writing simple if statements
a=25
b=34
if(a<b):
  print("a is small",a)

a=23
b=33
if b > a:
    print("b is greter than a")
elif a==b:
    print("a and b are equal")

score=int(input("enter the marks that you have got:"))
if score>90:
    print("grade:A")
elif score>=80:
    print("grade:B")
elif score>=70:
    print("grade:C")
elif score>=60:
    print("grade:D")
else:
    print("fail...")

age=int(input("enter your age: "))
if age<12:
    print("your are child")
elif age<20:
    print("you are teenager")
elif age<50:
    print("you are middle aged person")
elif age<75:
    print("your age senior citizen")
elif age<90:
    print("you are oldage person")

    