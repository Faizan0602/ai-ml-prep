# class Myclass :
#     x = 5
# p1=Myclass()
# p2=Myclass()
# p3=Myclass()

# print(p1.x)
# print(p2.x)
# print(p3.x)



# class Person : 
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
        
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
        

# p1 = Person("John",30)

# # Call the greet method
# p1.greet()


# Inside the editor, complete the following steps:
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

# class Dog :
#     def __init__(self,name,age):
#         self.name = name
#         self.age=age
#     def bark(self):
#         print(f"{self.name} says Woof")

# # d1 = Dog("Buddy",3)

# # d1.bark()

# Question

# Create a class named Car with the following requirements:

# Define a constructor (__init__) that accepts:
# brand
# model
# year
# Store these values as instance attributes.

# Create a method named display_info() that prints the car details in the format:

# 2020 Toyota Corolla
# Create an object named car1 with:
# Brand: "Toyota"
# Model: "Corolla"
# Year: 2020
# Call the display_info() method to display the car's information.

# Expected Output:

# 2020 Toyota Corolla
# Bonus Challenge

# Create another object:

# Brand: "Honda"
# Model: "City"
# Year: 2023

# and display its information using the same method.

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def display_info(self):
#         print(f"{self.brand} {self.model} {self.year}")

# car1 = Car("Toyota","Corolla",2020)
# car2 = Car("Honda","City",2023)

# car1.display_info()
# car2.display_info()

# Inside the editor, complete the following steps:
# Create a class Student with an __init__ that takes name and grade, and stores them as properties
# Create an object s1 with name "Anna" and grade "A"
# Print the grade of s1
# Change the grade of s1 to "B"
# Print the updated grade

# class Student : 
#     def __init__(self,name,grade):
#         self.name = name 
#         self.grade = grade
# s1 = Student("Anna","A")
# print(s1.grade)
# s1.grade = "B"
# print(s1.grade)

# Create a class named Playlist with the following requirements:

# Define a constructor (__init__) that accepts:
# name
# Store the playlist name as an instance attribute.
# Create an empty list called songs to store song names.

# Create a method named add_song(song) that adds a song to the playlist and prints:

# Added: Song Name

# Create a method named remove_song(song) that removes a song from the playlist if it exists and prints:

# Removed: Song Name

# Create a method named show_songs() that displays all songs in the playlist in the format:

# Playlist 'Favorites':
# - Bohemian Rhapsody
# - Stairway to Heaven
# Create an object named my_playlist with:
# Name: "Favorites"
# Add the following songs:
# "Bohemian Rhapsody"
# "Stairway to Heaven"
# Call the show_songs() method to display all songs.

# Expected Output:

# Added: Bohemian Rhapsody
# Added: Stairway to Heaven
# Playlist 'Favorites':
# - Bohemian Rhapsody
# - Stairway to Heaven

# class Playlist:
    
#     def __init__(self,name):
#         self.name=name
#         self.songs = []
    
#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"Added : {song}")
   
#     def remove_song(self,song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"Removed :{song}")
    
#     def show_songs(self):
#         print(f"Playlist '{self.name}': ")
#         for song in self.songs:
#             print(f"-{song}")
            
# my_playlist = Playlist("Favourites")
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()
# my_playlist.remove_song("Bohemian Rhapsody")
# my_playlist.show_songs()


# Inside the editor, complete the following steps:
# Create a class called Rectangle
# Add an __init__ method with width and height, and store them as properties
# Add a method called area that returns the width multiplied by the height
# Create an object r1 with width 5 and height 3
# Print the area of r1


# class Rectangle : 
    
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
    
#     def area(self):
#         return self.width*self.height

# r1 = Rectangle(5,3)
# print(r1.area())

        
            
