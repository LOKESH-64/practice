# 21. Downward Half-Pyramid Pattern
# Practice Problem: Print a downward half-pyramid pattern using stars (*).

# Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.

# Given Input: Rows: 5


# n = 5 
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")




# 22. Custom Exponentiation Function
# Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

# Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version shows how repeated multiplication works and how functions return results to the main program.

# Given Input: base = 2, exp = 5

# Expected Output: 2 raises to the power of 5: 32


# def expo(b,e):
#     num=e
#     r =1
#     while num > 0:
#         r = r*b
#         num-=1
#     print(r)
# expo(2,5)



# 24. Generate Fibonacci Series
# Practice Problem: Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

# Exercise Purpose: The Fibonacci sequence is a classic way to learn about state management in loops. You keep track of two changing variables at once to find the next number, which helps you see how data moves through each step.

# Given Input: Terms = 15

# Expected Output: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377



# str1 = "123"
# str2="xyz"

# for i in range(len(str1)):
#     print(str1[i]+str2[i],end="")

    
# Word Length Analysis
# Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

# Exercise Purpose: This exercise introduces “Metadata Extraction.” Often, you aren’t just interested in the data itself, but in its properties. In web development, this logic is used to validate if a user’s password or username meets specific length requirements.

# Given Input: words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Expected Output:/

# Apple - 5 Banana - 6 Cherry - 6 Date - 4 Elderberry - 10

# l =["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# for i in l :
#     le= len(i)
#     print(i,"-",le )
    


# Exercise 30. Word Frequency Counter (The Histogram)
# Practice Problem: Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.

# Exercise Purpose: This is a classic “Natural Language Processing” (NLP) task. It teaches you how to map data to occurrences, which is the logic used by search engines to index web pages or by social media platforms to identify trending hashtags.

# Given Input: text = "apple banana apple cherry banana apple"

# Expected Output: {'apple': 3, 'banana': 2, 'cherry': 1}


text = "apple banana apple cherry banana apple"
t  = text.split()
f = {}

for i in t :
    if i  not in f:
        
    
print(f)

    