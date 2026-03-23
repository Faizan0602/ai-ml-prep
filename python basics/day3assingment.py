# #Q1. Write a program that takes as input. Using conditional statements,
# #calculate the finaltax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

# salary = int(input("enter your salary : "))

# if salary < 30000:
#     tax = (salary*5)/100
#     print("final tax is : " , tax)
# elif salary >=30000 and salary<=70000:
#     tax = (salary*15)/100
#     print("final tax is : " , tax)
# else:
#     tax = (salary*25)/100
#     print("your final tax is : " , tax)


# Q2. Write a function that takes two integers and and prints all even
# numbers between them 

# def print_even(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)

# print_even(2,10)

# Q3. Write a function that prints the digits of a number, .
# For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them.

# [Hint - The right most digit of a number N is N%10.
# And to remove the right most digit from a number, we can do N = N / 10.]


def print_digits(n):
    while n > 0:
        digit = n % 10
        print(digit)
        n = n //10

print_digits(312)
