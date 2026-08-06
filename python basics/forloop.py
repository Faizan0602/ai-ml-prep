# string = "faizan"
# for var in string:
#     print(var)


# string = "hello" # o  exist ?
# if 'o' in string  :
#     print("o exists in string")

# for i in range(5): # range function gives numbers from zero to n-1
#     print(i)

# word = "artificial intelligence"
# # count the number of times i occured

# count = 0
# for ch in word :
#     if(ch=='i'):
#         count +=1
# print("i occured : ",count, "times")

# word = "artificial"
# count = 0
# for ch in word :
#     if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count+=1
# print("number of vowels : ", count)

#range function 

# range(start,stop,step)

# for i in range(5):
#     print(i, end=" ")

# print()  # line break

# for i in range(1,6):
#     print(i, end=" ")

# print()

# for i in range(1,10,2):
#     print(i, end=" ")

# print sum of first n natural numbers

n = int(input("enter the number : "))
sum = 0

for i in range(1,n+1):
    sum = sum+i
print(sum)
