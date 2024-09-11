# print("Hello, Python!")
# # This program will greet you with your name
#
# name = "Alice"
# print("Hello, " + name + "!")
#
# # This is a single-line comment
# print("This will run.")
#
# """
# This is a multi-line comment
# It can span multiple lines
# """
# print("This will also run.")
#
#
# # Python follows the order of operations (PEMDAS/BODMAS).
# # Addition
# print(3 + 5)
#
# # Subtraction
# print(10 - 2)
#
# # Multiplication
# print(4 * 7)
#
# # Division
# print(15 / 3)
#
# # Exponentiation
# print(2 ** 3)
#
# x = 5        # Integer
# y = 3.14     # Float
# name = "John" # String
# is_active = True  # Boolean
# print(type(x))
# print(type(y))
# print(type(name))
# print(type(is_active))
#
#
# length = 5
# width = 3
# area = length * width
# print(area)
#
# # Dictionaries are collections of key-value pairs
# # Dictionary: Dictionary values can be accessed using keys.
# # person = {"name": "Alice", "age": 30}
# # Dictionary access
# # age = person["age"]
#
# # List operations
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)
#
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
#
#
# # This program prints the first five multiples of 3
# for i in range(1, 6):
#     print(i * 3)  # Multiply the current number by 3
#
# # Addition
# print("3 + 5 =", 3 + 5)
#
# # Subtraction
# print("10 - 2 =", 10 - 2)
#
# # Multiplication
# print("4 * 7 =", 4 * 7)
#
# # Division
# print("15 / 3 =", 15 / 3)
#
# # Exponentiation
# print("2 ** 3 =", 2 ** 3)
#
# # Lab 5: Store Your Birth Year
# age = 40
# current_year = 2024
# birth_year = current_year - age
# print("Your birth year is:", birth_year)
#
# # Lab 6: Calculating the Area of a Rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# print("The area of the rectangle is:", area)
#
#
# # Lab 8: Swap Two Variables
# a = 10
# b = 20
#
# print("Before swapping: a =", a, "b =", b)
#
# # Swapping the values
# a, b = b, a
#
# print("After swapping: a =", a, "b =", b)
#
# # Lab 9: Simple Interest Calculator
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time (in years): "))
#
# simple_interest = (principal * rate * time) / 100
# print("The simple interest is:", simple_interest)
#
# # Lab 10: Data Type Conversion
# # Integer to String
# num = 10
# num_str = str(num)
# print("Integer to String:", num_str)
#
# # Float to Integer
# flt = 5.67
# flt_int = int(flt)
# print("Float to Integer:", flt_int)
#
# # String to Float
# str_num = "12.34"
# str_flt = float(str_num)
# print("String to Float:", str_flt)
#
# # Lab 11: Concatenating Strings
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print("Full name:", full_name)
#
# # Lab 12: List Operations
#
# numbers = [1, 2, 3, 4]
# numbers.append(9)
# print("Updated list:", numbers)

# Lab 13: Accessing List Elements
# fruits = ["apple", "banana", "cherry", "date"]
# print("First fruit:", fruits[0])
# print("Last fruit:", fruits[-1])
#
# Lab 14: Dictionary Basics
# person = {"name": "Alice", "age": 30, "city": "New York"}
#
# print("Name:", person["name"])
# print("Age:", person["age"])
# print("City:", person["city"])
#
# #Lab 15: Adding to a Dictionary
# person["email"] = "alice@example.com"
# print("Updated dictionary:", person)
#
#
# # Lab 16: Basic String Operations
# text = "Hello, World!"
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())
# print("Length:", len(text))

# Lab 17: List Slicing
# numbers = [10, 20, 30, 40, 50]
# print("First three elements:", numbers[:3])
# print("Last two elements:", numbers[-2:])

#Lab 18: String Formatting
name = "Jahan"
age = 35
print("My name is {} and age {}. ".format(name, age))
print(f"My name is {name} and age {age}.")

#Lab 19: Calculating the Perimeter of a Circle
import math

radius = float(input("Enter the radius of the circle: "))
perimeter = 2 * math.pi * radius
print("The perimeter of the circle is:", perimeter)

#Lab 20: Boolean Operations
# a = 10
# b = 5
# c = 20
#
# print("a > b:", a > b)   # True
# print("a < c:", a < c)   # True
# print("a == c:", a == c) # False
# print("a != b:", a != b) # True
# print("a >= 10:", a >= 10) # True
# print("b <= 5:", b <= 5)  # True
#

# height = 175  # in centimeters
# weight = 70   # in kilograms
# print("Height:", height, "cm")
# print("Weight:", weight, "kg")

a = 10
b = 20
c = 30

# Swap a and b
a, b = b, a

# Swap b and c
b, c = c, b

print("Final values:")
print("a =", a)
print("b =", b)
print("c =", c)
#####################################################

favorite_word = input("Enter your favorite word: ")
print(favorite_word * 10)