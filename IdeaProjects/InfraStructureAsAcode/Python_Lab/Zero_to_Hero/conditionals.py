# # # age = 18
# # # #
# # # # if age >= 18:
# # # #     print("You are an adult.")
# # # # ###############################################
# # # # # temperature = 25
# # # # #
# # # # # if temperature > 30:
# # # # #     print("It's a hot day.")
# # # # # elif temperature > 20:
# # # # #     print("It's a pleasant day.")
# # # # # else:
# # # # #     print("It's a bit chilly.")
# # # #
# # # # #Using or and and:
# # # #
# # # # temperature = 25
# # # # is_raining = False
# # # #
# # # # if temperature > 20 and not is_raining:
# # # #     print("It's a nice day to go outside.")
# # # #
# # # # #Using bool in Conditionals:
# # # #
# # # # is_sunny = True
# # # # is_weekend = False
# # # #
# # # # if is_sunny or is_weekend:
# # # #     print("You can go for a walk.")
# # # # else:
# # # #     print("Maybe stay indoors.")
# #
# #
# #
# # # Combining Boolean Expressions:
# # # is_member = True
# # # has_coupon = True
# # # if is_member and has_coupon:
# # #     print("Discount applied.")
# # # else:
# # #     print("No discount.")
# #
# # #Basic match Statement:
# #
# # # day = "Anyday"
# # #
# # # match day:
# # #     case "Monday":
# # #         print("Start of the work week.")
# # #     case "Friday":
# # #         print("Almost the weekend!")
# # #     case "Anyday":
# # #         print("Have a nice day")
# #
# # #Pattern Matching with Patterns:
# # number = 5
# #
# # match number:
# #     case 1 | 2 | 3:
# #       print("Low number")
# #     case 4 | 5 | 6:
# #       print("Medium number")
# #     case 7 | 8 | 9:
# #       print("High number")
# #
# # #Lab 5:Nested if Statements:
# # age = 25
# # has_id = True
# #
# # if age >= 18:
# #     if not has_id:
# #         print("You can enter the club.")
# #     else:
# #         print("ID required to enter.")
# # else:
# #     print("You are too young to enter.")
# #
# # #2.Combining Multiple Conditions:
# # # temperature = 9
# # # is_raining = True
# # #
# # # if temperature >= 10:
# # #     if is_raining:
# # #         print("You can go for a walk.")
# # #     else:
# # #         print("It's raining, bring an umbrella.")
# # # else:
# # #     print("It's too cold for a walk.")
# #
# # #Lab 6: Conditional Expressions
# # # age = 19
# # # message = "Adult" if age >= 18 else "Minor"
# # # print(message)
# #
# # # score = 85
# # # result = "Pass" if score >= 50 else "Fail"
# # # print(result)
# #
# # # Lab 7: Using match with Data Structures
# # numbers = [8, 6, 9]
# #
# # match numbers:
# #     case [1, 2, 3]:
# #         print("Matched the list [1, 2, 3]")
# #     case [x, y, z]:
# #         print(f"Matched a list with three elements: {x}, {y}, {z}")
# #     case _:
# #         print("No match")
# #
# # #2.Pattern Matching with Dictionaries:
# # user = {"adress": "Alice", "zip": 30}
# #
# # match user:
# #     case {"name": name, "age": age}:
# #         print(f"User's name is {name} and age is {age}")
# #     case _:
# #         print("User information is incomplete")
# #
# # ##########################
# # user = {"name": "Alice", "age": 30}
# #
# # match user:
# #     case {"name": name, "age": age}:
# #         print(f"User's name is {name} and age is {age}")
# #     case _:
# #         print("User information is incomplete")
# # #Lab 8: Advanced Logical Operators
# #
# # temperature = 25
# # is_raining = False
# # is_snowing = False
# #
# # if (temperature > 20 and not is_raining) or is_snowing:
# #     print("Weather is suitable for outdoor activities.")
# # else:
# #     print("Weather conditions are not ideal.")
# #
# #
# # ###############################
# # is_weekend = False
# # is_holiday = True
# #
# # if not is_weekend and is_holiday:
# #     print("Enjoy your day off!")
# # else:
# #     print("It's a regular workday.")
# #
# # ######Lab 9: Matching with Patterns and Guards
# # number = 18
# #
# # match number:
# #     case x if x % 2 == 0:
# #         print(f"{x} is even")
# #     case x if x % 2 != 0:
# #         print(f"{x} is odd")
# #
# # ########Matching with Multiple Conditions:
# #
# # user_input = "error"
# #
# # match user_input:
# #     case "error" | "warning":
# #         print("Alert: Check the system.")
# #     case "success":
# #         print("Operation completed successfully.")
# #     case _:
# #         print("Unknown status.")
# #
# # ################Lab 1: Basic Conditionals with if, elif, and else
# #
# # number = int(input("Enter a number: "))
# #
# # if number > 0:
# #     print("The number is positive.")
# # elif number < 0:
# #     print("The number is negative.")
# # else:
# #     print("The number is zero.")
# #
# # ##################################Problem: Create a program that determines the type of a/
# # # day based on a given temperature: Freezing, Cold, Mild, or Hot.
# #
# # temperature = float(input("Enter the temperature in degrees Celsius: "))
# #
# # if temperature <= 0:
# #     print("It's Freezing.")
# # elif 0 < temperature <= 10:
# #     print("It's Cold.")
# # elif 10 < temperature <= 25:
# #     print("It's Mild.")
# # else:
# #     print("It's Hot.")
# #
# # ###########f a person is eligible to vote based on their age. If they are 18 or older, print "Eligible to vote"; otherwise, print "Not eligible to vote".
# # age = int(input("Enter your age: "))
# #
# # if age >= 18:
# #     print("Eligible to vote.")
# # else:
# #     print("Not eligible to vote.")
# #
# # ##Problem:if a person should stay at home or go outside based on the weather. The conditions are: temperature > 20, not raining, and not snowing.
# # temperature = float(input("Enter the temperature in degrees Celsius: "))
# # raining = input("Is it raining? (yes/no): ").strip().lower() == 'yes'
# # snowing = input("Is it snowing? (yes/no): ").strip().lower() == 'yes'
# #
# # if temperature > 20 and not raining and not snowing:
# #     print("You can go outside.")
# # else:
# #     print("It's better to stay at home.")
# #
# # ###Problem: Implement a program to check if a student has passed an exam. The student passes if their score is at least 50 or if they have a teacher’s recommendation.
# # score = int(input("Enter the student's score: "))
# # teacher_recommendation = input("Does the student have a teacher's recommendation? (yes/no): ").strip().lower() == 'yes'
# #
# # if score >= 50 or teacher_recommendation:
# #     print("The student has passed the exam.")
# # else:
# #     print("The student has not passed the exam.")
# #
# # ###########if a person is eligible for a discount. The criteria are: being a member or having a coupon.
# is_member = input("Is the person a member? (yes/no): ").strip().lower() == 'yes'
# has_coupon = input("Does the person have a coupon? (yes/no): ").strip().lower() == 'yes'
#
# if is_member or has_coupon:
#     print("The person is eligible for a discount.")
# else:
#     print("The person is not eligible for a discount.")
#
# #Lab 3: Boolean Values, if a user is logged in and has a premium subscription. Print "Access Granted" if both conditions are true; otherwise, print "Access Denied".
# is_logged_in = input("Is the user logged in? (yes/no): ").strip().lower() == 'yes'
# has_premium_subscription = input("Does the user have a premium subscription? (yes/no): ").strip().lower() == 'yes'
#
# if is_logged_in and has_premium_subscription:
#     print("Access Granted")
# else:
#     print("Access Denied")
#
# #Problem: Create a program that determines if a user can access a restricted area based on their role and membership status.
# role = input("Enter the user's role (admin/user): ").strip().lower() =='admin'
# is_member = input("Is the user a member? (yes/no): ").strip().lower() == 'yes'
#
# if role or is_member:
#     print("Access to restricted area granted.")
# else:
#     print("Access to restricted area denied.")

##Lab 4: Pattern Matching with match
# a day of the week and prints a message indicating whether it is a weekend or a weekday.

def day_of_week(day):
    match day:
        case "Saturday" | "Sunday":
            print("It's the weekend!")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("It's a weekday!")
        case _:
            print("Invalid day")

# Test the function
# day_of_week("Monday")    # Output: It's a weekday!
# day_of_week("Saturday")  # Output: It's the weekend!
day_of_week("Holiday")   # Output: Invalid day

#categorize numbers into Positive, Negative, or Zero using pattern matching.

def categorize_number(num):
    match num:
        case num if num > 0:
            print("The number is positive")
        case num if num < 0:
            print("The number is negative")
        case 0:
            print("The number is zero")

# Test the function
# categorize_number(10)   # Output: The number is positive
categorize_number(-5)   # Output: The number is negative
# categorize_number(0)    # Output: The number is zero

##Type of Input
# def type_of_input(value):
#     match value:
#         case str():
#             print("This is a string")
#         case list():
#             print("This is a list")
#         case dict():
#             print("This is a dictionary")
#         case _:
#             print("Unknown type")
#
# # Test the function
# # type_of_input("Hello")         # Output: This is a string
# # type_of_input([1, 2, 3])       # Output: This is a list
# type_of_input({"key": "value"})# Output: This is a dictionary
# # type_of_input(42)              # Output: Unknown type

###########################################################################
credit_score = int(input("Enter your credit score: "))
income = int(input("Enter your annual income: "))

if credit_score >= 700:
    if income >= 50000:
        print("Eligible for a loan")
    else:
        print("Not eligible for a loan due to insufficient income")
else:
    print("Not eligible for a loan due to low credit score")

#################################
# Exercise 2:
# Problem: Create a program that determines the shipping cost based on the weight of a package and whether it's express delivery.
