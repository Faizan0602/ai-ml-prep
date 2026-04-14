# #string in python (sequence of characters)
# word1 = "i love"
# word2 = "python" #(sequence of characters : 'p','y','t','h','o','n')

# print(len(word1))
# sentence = word1+" " +word2 #(concatenation)
# print(sentence)

# #indexing 

# word3 = "faizan"   #accessing a particular charac of string
# print(word3[2])

# for ch in word3:   #for loops to print characters of string
#     print(ch)

# # word[2] = 'z'   (not possible to change , strings are immutable)


# slicing in strings - string ke tukde karke sub string banana 

#str[starting index : ending index(not included)]

# word = "python" # we have to print only "th"
# print(word[2:4]) #-output 'th'

#string formatting 

#1 .format()

#normal formatting
a = 5
b = 10
sum = a+b
# print("sum of {} and {} is {}".format(a,b,sum))
# print("language is {}".format("python"))


#index based formatting
# print("sum of {1} and {0} is {2}".format(a,b,sum))

#value based formatting - we can assign values to variable 

# print("value of vars {a} and {b} is ".format(a=2,b=3))


# #f-strings()

# a =5
# b=10
# print(f"sum of {a} and {b} is {a+b}")

#-------------------------------END OF STRING------------------------------------------------




#list 

marks =[99,89,59,69,79]
# print(len(marks))
# print(marks[2])
# marks[3]=70
# print(marks)

#slicing 

# print(marks[0:4])

#methods

# marks.append(100)
# print(marks)

# marks.insert(3,81)
# print(marks)

# marks.sort()
# print(marks)

# marks.sort(reverse=True)
# print(marks)

# rev = [1,2,3,4,5]
# rev.reverse()
# print(rev)


# num = [1,2,3,10,4,5]

# for val in num:
#     print(val)


# # find the index of the element 10 

# x = 10
# idx=0
# for value in num :
#     if value ==x:
#         print(f"x found at index :{idx}")
#         break
#     idx+=1
#--------------------------------------------END OF LIST --------------------------------------------------------------------------------
info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]
# unique=set()
# for tup in info:
#     unique.add(tup[1])    #.add function used to add courses in empty set 
# print(unique)  

# for name,course in info:
#     if(course=="English"):
#         print(name)

dict ={}       #print name with their set of courses

for name, course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)

