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


s1= input("enter numbers : ")
list1 = []
s1.split()
for x in s1:
    list1.append(int(x))
s2 = input ("enter numbers : ")
list2=[]
s2.split()
for x in s2:
    list2.append(int(x))

result = list1+list2
result.sort()
print(result)

