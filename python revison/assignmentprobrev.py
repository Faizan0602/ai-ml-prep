# Q1. Write a program that takes as input. Using conditional statements,
# calculate the finaltax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary = int(input("enter the salary : "))  
if salary<30000:
        tax = (salary*5)/100
        print(tax)
elif salary>=30000 and salary<=70000:
        tax = (salary*15)/100
        print(tax)
else:
        tax=(salary*25)/100
        print(tax)

