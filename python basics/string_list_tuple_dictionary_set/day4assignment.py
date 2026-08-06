# Ask the user for a string and check whether it is a palindrome or not.
# A is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc.
# palindrome

# [A palindrome string is equal to the reversed version of the string. We can
# use a loop to reverse the string manually.]

# n = input("enter a string : ")
# rev = ""
# for ch in n :
#     rev = ch+rev
# if(n==rev):
#     print("palindrome")
# else:
#     print("not palindrome")


# Q2. Given a list of integers compute the average of all numbers in the list.

# list = [1,2,3,4,5]
# sum = 0
# for i in list:
#     sum+=i
# print(sum)


# s1= input("enter numbers : ")
# list1 = []
# s1.split()
# for x in s1:
#     list1.append(int(x))
# s2 = input ("enter numbers : ")
# list2=[]
# s2.split()
# for x in s2:
#     list2.append(int(x))

# result = list1+list2
# result.sort()
# print(result)


# Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

# tup = (1,2,3,4,5,6,7,8,9,10)

# even = []
# odd = []

# for i in tup :
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)

# even_tuple = (tuple(even))
# odd_tuple = tuple(odd)

# print(even_tuple)
# print(odd_tuple)

#------------------------------------STARTING AGAIN-----------------------------------------------------------------------------------
# Ask the user for a string and check whether it is a palindrome or not.
# A is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc.
# palindrome


# n = input("enter a string : ")
# rev = ""
# for ch in n :
#     rev = ch+rev

# if(n==rev):
#     print("palindrome")
# else:
#     print("not palindrome")


# Given a list of integers compute the average of all numbers in the list.

# list = [5,10,15,20]
# sum =0
# for i in list:
#     sum+=i

# avg = (sum)/len(list)
# print(avg)

# num1=[1,2,7]
# num2=[2,4,5]

# final = num1+num2
# final.sort()
# print(final)

# tup = (1,2,3,4,5,6,7,8,9,10)
# even = []
# odd = []

# for i in tup:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)

# even_tuple = (tuple(even))
# odd_tuple = (tuple(odd))

# print(even_tuple)
# print(odd_tuple)

# Create a dictionary where: 
# • Keys = student names 
# • Values = marks (integer) 
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’) 
# depending on the operation they want to perform on the dictionary: 
# 1. A - Add a student 
# 2. B - Update marks 
# 3. C - Search for a student 
# 4. D - Display all students and marks
students = {}
while True:
    print("\n---MENU----")
    print("A-add student")
    print("B-Update marks")
    print("C-Search students")
    print("D-Display all")
    print("E-EXIT")

    choice = input("Enter choice : ").upper()

    if choice =='A':
        name =input("enter name : ")
        marks = int(input("enter marks : "))
        students[name]=marks
        print("student added successfully")
    elif choice =='B':
        name = input("enter name of student whose marks is to be updated :")
        if name in students:
            marks = int(input("enter marks to be updated :"))
            students[name]=marks
            print("marks updated")
        else:
            print("student not found")

    elif choice == 'C':
        name = input("enter name : ")
        if name in students:
            print(f"{name} has {students[name]}marks")
        else:
            print("student not found")
    elif choice =='D':
        if(len(students))==0:
            print("NO RECORD")
        else:
            print("\n student records :")
            for name, marks in students.items():
                print(name ,":" , marks)
    elif choice == 'E':
        print("Exiting Program")
        break
    else:
        print("Invalid Choice , Try Again")

