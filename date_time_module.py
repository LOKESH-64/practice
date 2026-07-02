# from datetime import datetime


# # print(date.today())
# # a = date.today()
# # print(a.year)
# # print(a.month)
# # print(a.day)


# b=datetime.now()
# print(b)


# # x =b.strftime("%I:%M %p %n%m/%d/%Y %A")
# # print(x)

# y = b+timedelta(days=50)


import json

# javascript object notation
x=["sasa","ewew"]
print("py=",x,x[0])

y = json.dumps(x)
print("json =",y,y[0])


a={"name":"lokesh","role":"developer"}
z=json.dumps(a)
q=json.loads(z)
print("py=",q,q["name"])

# with open("first.json","w") as json_file:
#     json.dump(y,json_file)
#     json.dump(z,json_file)


with open("first.json","r") as retriv:
   
    r = json.load(retriv)
    print("json",r,r[0])