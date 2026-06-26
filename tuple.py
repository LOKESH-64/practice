'''Tuple: A tuple is an immutble , ordered collection of hertogenous elements
        enclosed in round paranthses.
Diffenernce between list and tuple :
List is mutable and tuple is immutable 
Tupels are faster compared to lists because of immutability 

t=(1,2.3,True,'lokesh',[1,2,3],(1,2,3),{1,2,3},{1:'q'})
print(t)
# tuple input 
# tuple input with string elements
tup=tuple(map(int,input().split())) 
tup=tuple(map(int,input().split(','))) 
inp=tuple(input().split())# for space seperated elements 
inpt=tuple(input().split(','))# for comma seperated elements  

# if a tuple is a single element 
a=(9,) 
# operations on Tuples
# operators - + can be used for tuple concatination
#             * can be used for repetation 
#these work on tuples as they are creating a new tuple object,not modifying the orginal object
t1=(1,2)
t2=(3,4,5)
new=t1+t2 
print(new)
print(id(t1)) 
print(id(t2))
print(id(new)) 
''' 
'''
# Builtin functions -functions that work on iterables 
# Example - min(), max(),sorted(), etc
# Indexing can be used on tuples also similar to other iterables 
# tuple methods- Tuple class functions 
    #>count()
    #>index() only 2 methods are present because tuple is immutable
a=(1,2,3,1,2,3)
print(a.count(1))
print(a.index(2))
# immutability behaviour of tuple 
t=(1,[2,3])
#t[1]=[10] # not support
t[1][0]=20 # it will support 
print(t)
#Tuple  does not support item assignmentt but if it is having mutable elements as members
#then the elements in them can be changed
'''