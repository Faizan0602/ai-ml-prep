#Tuple = list jaisa hi hota hai but immutable (change nahi kar sakte)

t = (1, 2, 3, 4)
print(t)

t = (10, 20, 30)

print(t[0])   # 10
print(t[-1])  # 30

t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)

t = (5,)   # comma important hai

t = (1, 2, 3)

for i in t:
    print(i)

t = (1, 2, 2, 3)

print(t.count(2))   # 2 count total occurence 
print(t.index(3))   # 3 returns first occurence of index