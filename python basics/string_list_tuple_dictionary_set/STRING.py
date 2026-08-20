word = "python"
print(len(word))

word1 = "i love"
word2 = "java"
sentence = word1+" "+word2
print(sentence)

word3 = "Faizan"
print(word3[3])

# slicing string (string ke tukde karke sub string bnana)

# syntax 
# str = python (lets say we have to extract th as a substring)

#=> str[starting index : ending index(not including) +1]

str = "python"
print(str[2:4])

str1 = "i am faizan"
print(str1[:4])
print(str1[0:len(str1)])

#string formatting

a = 5
b = 10
sum = a+b

# normal formatting 
print ("sum of {} & {} is {}".format(a,b,sum))

# #example 2 
print("language is {}".format("python"))

# #index based formatting 
print ("sum of {0} & {1} is {2}".format(a,b,sum))

# f-strings => f"your text {variable}"
# example 1
name = "Faizan"
age = 21
print(f"My name is {name} and I am {age} years old")

a = 10
b = 5

#example 2 
print(f"Sum is {a + b}")
# add this line anywhere
print("Day 4 completed 🚀")

