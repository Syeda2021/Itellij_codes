# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     print("Factorial:", result)
#
# # Example usage
# factorial(5)  # Output: Factorial: 120
#####################################################
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost the weekend!")
    case _:
        print("Have a nice day!")