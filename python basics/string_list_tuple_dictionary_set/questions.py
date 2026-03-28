# given a list of tuples with info(name,subject):
#     list all unique course 
#     list student enrolled in english
#     create dict (student , set of course )

info = [
    ("alice","math"),
    ("bob","science"),
    ("alice","science"),
    ("charlie","math"),
    ("bob","math"),
    ("alice","english"),
    ("charlie","english")
   
]
# list all unique course 

unique_course = set()
for tup in info:
    unique_course.add(tup[1]) # course at 1st index added into empty set 
print(unique_course)

# list student enrolled in english
for name,course in info:
    if(course=="english"):
        print(name) 









