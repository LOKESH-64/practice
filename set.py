''' Set:
   A  set is a mutable, unordered collection of unique and imutable elements enclosed in
   curly parantheses  
   
s={1,2.34,False,'python',(1,2,3)}
print(s)     
 # set input():
l=[1,2,3]
print(set(l))
# string elements 
s=set(input().split()) # space seperated
s=set(input().split(','))# comma seperated 
# integer elements 
s=map(int,input().split()) # space seperated     
s=map(int,input().split(',')) # comma seperated     
# write a program to find the number of distinct characters in a given word 
# i/p: codegnan
# o/p:7 
s=set(input())
print(len(s))
set=set()
print(type(set)) 

n=int(input())
all_scores=list(map(int,input().split()))
a=int(input())
total_score=n*a
sum=sum(all_scores)
lastsum=total_score-sum
print(lastsum)'''


#m,a,b,p=tuple(map(int,input().split()))
#first_dis=(a//100)*m
#after_dis=m-first_dis
#second_dis=(b//100)*after_dis
#after_sdis=after_dis-second_dis
#total=first_dis+second_dis
#print(total)
#print(after_sdis)
#print(b>=after_sdis)

#a=int(input())
#b=int(input())
#c=int(input())
#print(b,c,a)


#a=[1,'lokesh']
#b=[1,'lokesh']
#a==b
#print(id(a))
#print(id(b))
#print(a is b)
#print(a==b)


#s1=eval(input())=="True"
#s2=eval(input())=="True"
#print(id(s1))
#print(id(s2))
#print(s1 is s2)
#print(s1 is not s2)

a=5
b=5
print(id(a))
print(id(b))
print(a is b)