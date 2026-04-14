# Q1. Write a program that takes as input. Using conditional statements,
# calculate the finaltax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

# salary = int(input("enter the salary : "))  
# if salary<30000:
#         tax = (salary*5)/100
#         print(tax)
# elif salary>=30000 and salary<=70000:
#         tax = (salary*15)/100
#         print(tax)
# else:
#         tax=(salary*25)/100
#         print(tax)

# Q2. Write a function that takes two integers a and b and prints all even
# numbers between them (inclusive).

# def even(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)
#         i+=1
       
# result =  even(2,20)
# print("even numbers are : " , result)



# Q3. Write a function that prints the digits of a number n


# def print_digits(n):
#     while n>0:
#         digit = n%10
#         print(digit)
#         n=n//10
# print_digits(312)

# Write a function to return the count the number of digits in a number n 

# def count(n):
#     count =0
#     while n>0:
#         n=n//10
#         count+=1
#     return count
# print(count(1234))

# Write a function to return the sum of digits of a number n 

# def calc(n):
#     sum =0
#     while n>0:
#         digit = n%10
#         sum+=digit
#         n=n//10
#     return sum

# ans = print(calc(123))


# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
# 3 and 5.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
        i+=1




