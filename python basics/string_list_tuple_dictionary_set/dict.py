# 💡 Dictionary kya hota hai ?
# 👉 Dictionary = key-value pairs ka collection
# 👉 Har value ek key se access hoti hai

# key must be unique (duplication not allowed)

student = {
    "name":"faizan",
    "age": 24,
    "course" : "python",
     3.14 : "pi"
}
print(student)

# Access values:
print(student["name"])
print(student["age"])

# Update value:
student["age"]=23  #muatable
print(student["age"])

# Add new key:
student["city"] = "Delhi"
print(student)

# Remove key:
student.pop("age")
print(student)

