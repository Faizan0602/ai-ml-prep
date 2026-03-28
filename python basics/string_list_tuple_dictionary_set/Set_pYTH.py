# 👉 Set = unique elements ka collection
# 👉 Duplicate values allow nahi hoti ❌

s = {1,2,3,4}
print(s)

# Duplicate remove ho jata hai:

s = {1,2,2,3,3,4}
print(s)

# 📌 Features:
# Unordered (index nahi hota ❗)
# Mutable (add/remove kar sakte ho)
# Unique elements only

# empty_set = set() #creates empty set 

# set methods
s.add(5) # adds a value
s.remove(2)  # removes vale , error dega agar element nahi mila
print(s)

s.pop() # removes random value 
print(s)

#Union (combine):
set1 = {1,2,3,4,5}
set2 = {2,4,5} 
x = set1.union(set2)
print(x)

# Intersection (common):
set3 = {10,20,30,40}
set4 = {10,20,50,60}
y = set3.intersection(set4)
print(y)

