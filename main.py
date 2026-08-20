# a = "hello faizan"

# print(a[0:5:1])

# print(a[::])

# a = "12"

# a = int(a)

# print(type(a))

# name = input("enter your name : ")

# print(f"hello, {name} , welcome to python")

# a = 10
# b = 20

# print(a+b)
# print(a-b)
# print(a*b)
# print(b/a)
# print(a%b)

# num1 = int(input("enter your first num : "))
# num2 = int(input("enter your second num : "))

# if (num1>num2):
#     print(f"{num1} is greater than {num2}")
# elif (num2>num1):
#     print(f"{num2} is greater than {num1}")
# else:
#     print("both numbers are same")


# a = int(input("enter first num : "))
# b = int(input("enter second num : "))

# if a > b :
#     print(f"{a} is the greatest")
# else:
#     print(f"{b} is the greatest")
    
    
# gen = input("enter the gender : ")

# if gen == 'Male':
#     print("good morning sir")
# else:
#     print("good morning mam")


# a = int(input("enter a num : "))

# if(a%2==0):
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

# name = input("enter name : ")
# age = int(input("enter the age :"))

# if (age>=18):
#     print(f"{name} is eligible to vote")
# else:

#     print(f"{name} is not eligible to vote")

# for i in range(1,11):
#     print(5*i)
    
    #or
# n = int(input("enter the number for the table you want"))    
# for i in range(n,(n*10)+1,n):
#     print(i)

# n = int(input("enter the number hello world wants to be printed : "))

# for i in range(n):
#     print("hello world")
    
# n = int(input("enter the number upto which numbers needs to be generated"))

# for i in range(n,0,-1):
#     print(i)
    
# n = int(input("enter the number : "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# n = int(input("enter the number : "))
# sum =0

# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n = int(input("enter the number : "))
# fact=1

# for i in range(1,n+1):
#     fact*=i
# print("factor of" , n , "is :", fact)

# s = input("enter a string : ")
# rev= ""
# for i in range(len(s)-1,-1,-1):
#     rev = rev+s[i]
# print(rev)
    
    
# a = input("enter a string to be checked if palindrome or not : ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b+a[i]
# if(a==b):
#     print("palindrome")
# else:
#     print("not palindrome")
    
# a = 1234
# while a >0:
#     print(a%10)
    
#     a=a//10
    
# n = int(input("enter a number : "))
# rev =0
# while n>0:
#     rev = rev*10+n%10
#     n=n//10
# print(rev)

# n = int(input("enter a number to be checked if its palindromic or not : "))
# rev = 0
# copy=n

# while n>0:
#     rev = rev*10+n%10
#     n=n//10

# if (copy==rev):
#     print("palindromic number")
# else:
#     print("not palindromic")

# import random 
# num = random.randint(1,100)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 100 : "))
#     if num == guess:
#         tries+=1
#         print(f"you have guessed the right number in {tries} tries")
#         break
#     elif num < guess:
#         tries+=1
#         print("go a little lower")
#     elif num>guess:
#         tries+=1
#         print("go a little higher")
#     else: 
#         tries+=1
#         print("sorry you are wrong")
        
        
# def check_palindrome(a):
    
#     b = ""
#     for i in range(len(a)-1,-1,-1):
#         b = b+a[i]
#     if a ==b:
#         print("String is palindrome")
#     else:
#         print("not palindrome")

# a = input("enter a string for which palindrome to be checked")
# check_palindrome(a)


# l = [1,2,-1,-5,3]

# for i in l:
#     if(i>=0):
#         print(f"positive numbers : {i}" )
# for i in l :
#     if(i<0):
#         print(f"negative numbers : {i}")
        
# l = [10,20,30,40,50]
# sum = 0
# for i in l :
#     sum = sum+i
# print(sum/len(l))
    
# l = [20,30,10,50,40]

# greatest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i]>greatest:
#         greatest=l[i]
#         index=i
# print(f"your largest element is {greatest} at {i} index")


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# merged_dict = {}

# for i in d2 :
#     d1[i]=d2[i]

# print(d1)

# d1 = {10:100,20:200,40:300}
# sum = 0
# for i in d1 :
#     sum+=d1[i]
# print(sum)


# a = [1,1,1,1,2,2,2,3,3,4,4,4,5,5]
# d = {}

# for i in a : 
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# a = int(input("enter a number : "))

# try : 
#     print(10/a)
# except Exception as err:
#     print(f"Sorry there is and err as {err}")
# else:
#     print("good there is no error")
# finally :
#     print("i will run no matter what XD")

# print("okay div was don successfully")


r = open('superman.txt','a')

# r.write("hello this is a file created by write func (it can creat a file if it doesnot exist/ if it exist it overwrites the file)")
r.write("the 'a' appends in the existing file")
r.close

