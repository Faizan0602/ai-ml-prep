# # List = ek container jisme multiple values store hoti hain
# # mutable sequence of values i.e. (values from a particular index can be altered/ changed unlike strings which are mutable)
# # no need to make different variables , rather make one and store all in that

# marks = [99,89,100,65,92]
# print(marks)
# print(len(marks))
# print(marks[2])

# marks[2]=70  # mutable
# print(marks)

# #slicing in list  : sub list is created 

# print(marks[0:3])

# #list methods  :
# # 1 - l.append() : list ke last mai addition of an element

# nums = [1,2,3]
# nums.append(4)
# print(nums)

# # 2 - l.insert(index,value) : insert element at index
# nums.insert(2,10)
# print(nums)

# #3 - l.sort() : arranges in increasing order 

# order = [1,3,2,5,4]
# order.sort()
# print(order)

# # for reverse order : 
# order.sort(reverse=True)
# print(order)

# # 4 - l.reverse() : reverses the order of list 

# rev = [1,2,3,4,5]
# rev.reverse()
# print(rev)

# Loops with lists :

num = [1,2,3,10,4,5]

# for val in num:
#     print(val) 

# find the index of the element 10 

x = 10 # target element
idx = 0 # index init. from 0
for value in num:
    if(value==x):
        print(f"x found at index : {idx}")
        break
    idx+=1

#list completed 

