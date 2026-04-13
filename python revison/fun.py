#range()function - range(start,stop,step)  here step is increment value 
                                            #by defualt start value is 0 and step value is +1

#sum of first n natural numbers

# n = int(input("enter a number : "))

# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# def hello():
#     print("hello world")
#     print("welecome to python")

# hello()

# def sum(a,b):
#     sum = a+b
#     return sum 

# result = sum(5,10)
# print(result) 

def average(a,b,c):
    avg = (a+b+c)/3
    return avg

a = int(input("enter first num : "))
b = int(input("enter second num :"))
c = int(input("enter third num : "))
result = average(a,b,c)
print("average of three numbers is : ", result)
