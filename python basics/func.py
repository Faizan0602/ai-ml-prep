# function defination 

# def hello():
#     print("hello")
#     print("from faizan")

# #func call
# hello()

# #func defination
# def sum(a,b):    #(a,b)=>parameters
#     s = a+b
#     return s

# #func call 
# ans1 = sum(4,7)
# ans2 = sum(3,6)
# print(ans1)
# print(ans2)


#make a function that takes 3 numbers as input and calculte its avg

#fun defination
# def avg(a,b,c):
#     calc = (a+b+c)/3
#     return calc

# #func call 
# print(avg(1,2,3))

    

# #lambda func (for simple work)
# sum = lambda a,b : a+b
# print(sum(4,5))

#waf to print factorial of n 
def calc_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

n = int(input("enter a number : "))
ans = calc_factorial(n)
print("factorial of entered number is : " , ans)



