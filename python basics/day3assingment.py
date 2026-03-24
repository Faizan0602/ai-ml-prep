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


# def print_digits(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n //10

# print_digits(312)

# Q4. Write a function to return the count the number of digits in a number n 


# def count_digits(n):
#     count = 0
    
#     while n > 0:
#         n = n // 10
#         count += 1
        
#     return count
# print(count_digits(312))

# Write a function to return the sum of digits of a number n 

# def sum_digits(n):
#     addition = 0

#     while n > 0:
#         digit = n%10
#         addition+=digit
#         n = n//10
#     return addition

# print(sum_digits(123))

# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3
# and 5.

# count = 0
# for i in range(1,100):
#      if i%3==0 or i%5==0:
#         print(i)

# Q7. Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit”.

# def check_number():
#     while True:
#         user_input = input("Enter a number (or Quit to exit): ")
        
#         if user_input == "Quit":
#             print("Program ended")
#             break
        
#         num = int(user_input)
        
#         if num > 0:
#             print("Positive")
#         elif num < 0:
#             print("Negative")
#         else:
#             print("Zero")

# check_number()

# Q8. Letʼs create a Simple Calculator that performs arithmetic operations. Create
# a function calculator(a, b, operation) that performs addition, subtraction,
# multiplication, or division based on the operation parameter.
# [ parameter can have values +,-,*,/]
       

def calculator(a,b,operation):
    ans = 0
    if operation == '+':
        ans = a+b
    elif operation == '-':
        ans = a-b
    elif operation == '*':
        ans = a*b
    else :
        ans = a/b   
    return ans 

print(calculator(20,10,'*'))


        
        


