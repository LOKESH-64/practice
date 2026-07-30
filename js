java script is a free open source scripting language  which is used to send the data to back end using API  

but first of all we need to save the data by using a variable 

variable is created using var  
there are  variables rules:
1)variable must start with a character alphabet 
2)no special symbols are allowed except $ and _
case sensitive :
keywords are not allowed 

Data types in js :
number     34 3 56 -66 -77
string      " or ''
boolean    True or False 
undefined   garbage value 
null       not a garbage either 0 or null word 
bigint     large intger with letter n at the end 
            123453453453453453453533455n
symbol     creates a unique reference even same value 

object    combination of all the above mentioned datatypes :


Types of Js :
1)internal 
    writing in the same html file using script tag
2)external 
    writimg in the .js extension file and giving src inside script tag as attribute 

operators in js :
1) arithematic   + - * % / 
2) assignment    =, += , -= , /= , %= , *=
3) logical       && || !
4) relational    < <= > >= == !=
5) conditional or ternary  condition?(valid):(invalid)

note :
the relational anf logical operators are going to work  based on the conditional statements .



in JS we are going to use 2 types of comments 
single line comment  //
multiline comment /* ------------- */




we are going to pass an expression to the conditional statements 
the expression is going to be created using relational operators and logical operations 
these conditional statements are going to return a boolean value 

1)if 
2)else
3)else if 
4)switch 

 * we use curly braces as a block 

Looops in JS:
-------------
A loop is going to help us to execute a block of code multiple times .
It carries intilization condition and iteration.
we are having 3 types of loops  
1) while 
2) do while 
3) for 
In JS we are going to carry 



functions in JS:
syntax:
function function name (arguments){
    statements;
}

we use return keyword  to geta response 

-------------------------------------------

Arrays in JS :
--------------
Arrays  is a comibination of multiple values of different data types 
Array starts from 0 th position and ends at n-1 position   
There ara few pre defined methods in array 
push            inserts multiple values at the end  
pop             deletes one value at the end     
shift           deletes one value at the start
unshift         inserts multiple values at the start 
splice          inserts,delete,updates,multipple values at any position
                splice(position,no of values to delete ,values you want to add)
length          calculates the count of an array 