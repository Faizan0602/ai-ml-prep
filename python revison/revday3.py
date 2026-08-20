# conditional statements (if , elif, else) , if a particular condition is true then only program should execute

# check if user can vote or not 

# age = int(input("enter user age : "))

# if age>=18:
#     print("can vote")
# else:
#     print("not adult")

#traffic color check 
# color = input("enter the color : ")

# if color  == "red":
#     print("stop")
# elif color == "yellow" :
#     print("look")
# elif color == "green":
#     print("go")
# else : 
#     print("wrong color entered") 

# check user age and generation 

# age = int(input("enter age : "))

# if (age<13):
#     print("child")
# elif(age>=13 and age<18):
#     print("teen")
# else:
#     print("adult")

#admin password

# username = input("enter username : ")
# password = (input("enter password :"))

# if(username=="admin" and password == "pass"):
#     print("login sucessfull")
# elif(username == "admin" and password!="pass"):
#     print("wrong password")
# else:
#     print("wrong username")

# n is multiple of 5 or not

# n = int(input("enter number : "))

# if (n%5==0):
#     print("n is a multiple of 5")
# else:
#     print("not a multiple of 5")


#ODD EVEN 

# n = int(input("enter the number to be checked : "))
# if(n%2==0):
#     print("even")
# else:
#     print("odd")

#loops (while,for)- for repetetive task 

# i = 1
# while (i<=5):
#     print("hello world")
#     i+=1

#print numbers from 1 to 5

# i = 1
# while(i<=5):
#     print(i)
#     i+=1

# multiplication table of n 

# n = int(input("enter a number : "))

# i = 1
# while(i<=10):
#     print(n*i)
#     i+=1

#break and continiue : break is used to terminate a loop and continiue is used to skip the iteration 

#print number from 1 to 10 but get out of the loop where 6 comes
# i = 1
# while(i<=10):
#     if(i%6==0):
#         break
#     print(i)
#     i+=1
# print("outside loop")


# skip multiple of 3

# i=1
# while(i<=10):
#     if(i%3==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#print odd num between 1 and 10

# i =0
# while(i<10):
#     i+=1
#     if(i%2==0):
#         continue
#     print(i)

# for loop -  used for sequential traversal 

# string = "faizan"

# for var in string:
#     print(var)

# if 'i' in string:       # in is a membership opeerator which checks presence of a particular char or smt in string
#     print("i exist in the given string")


# for loop on number sequence

# for i in range(5):
#     print("hello world")


word = "artificial intelligence"
#count how many times i occured in word

# count = 0
# for ch in word:
#     if(ch=='i'):
#         count+=1
# print("count of i is : " ,count)

# print vowels in a given word 

word = "artificial intelligence"  

count = 0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print("total vowels : " , count)








   


