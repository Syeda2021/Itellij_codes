#Lab 1: Basic File Reading with open():basics of file handling, focusing on reading text files and processing their contents.
#Reading a File Line by Line:

# file = open("sample.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()

#####################################################
# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()
#############################################################
#Lab 2: Writing to Files with open()
# data = ["Line 1", "Line 2", "Line 3"]
# file = open("sample.txt", "w")
# for line in data:
#     file.write(line + "\n")
# file.close()

###########################################################
# file = open("output.txt", "a")
# file.write("This is a new line.\n")
# file.close()

###########################################################

#Lab 3: Using with for File Handling:Learn how to use the with statement to handle files more safely and efficiently. This lab covers how with ensures files are properly closed, even if an error occurs.
#Reading a File with with:

# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())
#################################################################################
#Writing to a File with with:

# with open("output.txt", "w") as file:
#     file.write("Hello,\n world!")

################################################################
#Lab 4: Sorting Data from Files,This lab focuses on reading data from files, sorting it, and then writing the sorted data back to a file. You'll learn how to use the sorted() function to achieve this.
#Sorting Lines in a File:
# with open("unsorted.txt", "r") as file:
#     lines = file.readlines()
#
# sorted_lines = sorted(lines)
#
# with open("sorted.txt", "w") as file:
#     for line in sorted_lines:
#         file.write(line)
#################################################
#2. Sorting Numbers from a File:
# with open("numbers.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file]
#
# sorted_numbers = sorted(numbers)
#
# with open("sorted_numbers.txt", "w") as file:
#     for number in sorted_numbers:
#         file.write(str(number) + "\n")

###################################################################################################
#Lab 5: Working with CSV Files
#Learn how to read and write CSV files using Python('s built-in csv module. This lab covers reading data into dictionaries and writing lists of dictionaries to CSV files.Reading a CSV File into a List of Dictionaries:)
# import csv
#
# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     data = [row for row in reader]
#
# print(data)
###################################################
#2. Writing a List of Dictionaries to a CSV File:
# import csv
#
# data = [
#     {"Name": "Alice", "Age": 25, "City": "New York"},
#     {"Name": "Bob", "Age": 30, "City": "Chicago"},
#     {"Name": "John", "Age": 38, "City": "Philadelphia"}
# ]
#
# with open("output.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
#     writer.writeheader()
#     writer.writerows(data)

#######################################################################################
# Lab 6: Using dict with CSV Files
# Explore how to utilize dictionaries when working with CSV files. This lab involves reading CSV data into dictionaries and performing operations like filtering and aggregating.
#1. Filtering CSV Data Using a Dictionary:

# import csv
#
# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     filtered_data = [row for row in reader if row["Age"] > "25"]
#
# print(filtered_data)
########################################################################################
#2.Aggregating Data from a CSV File:

# import csv
#
# age_sum = 0
# with open("data.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         age_sum += int(row["Age"])
#
# print("Total Age:", age_sum)

###############################################################
# Lab 7: Basic Image Handling with PIL
# Learn how to handle images using the Python Imaging Library (PIL). This lab introduces basic image operations like opening, resizing, and saving images.
# 1.Opening and Displaying an Image:
# from PIL import Image
#
# img = Image.open("example.jpg")
# img.show()

#######################################################
#2.Resizing and Saving an Image:

# from PIL import Image
#
# img = Image.open("example.jpg")
# img_resized = img.resize((200, 200))
# img_resized.save("resized_example.jpg")

#################
