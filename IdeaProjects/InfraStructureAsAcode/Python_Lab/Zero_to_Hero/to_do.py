# Dict - Dictionary
student_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "courses": [
        {"course_name": "DevOps",
         "start_date": "1234"
         },
        {"course_name": "DataAnalytics",
         "start_date": "0712"
         }
    ]
}





student_name = student_info["name"]
print(student_name)

student_course = student_info["courses"]

student_course[0]= True
print(student_course[0])

alice_courses = student_info["courses"]
# How many course Alice?
total_courses = len(alice_courses)
print(total_courses)
print(alice_courses)

# course_name = input("Enter your course_name: ")
# print("Hello, you are enrolled in " + course_name + "!")

# To do Small Problem
# Find out the start_date value of DevOps course for Alice from student_info dictionary ,
# your code should also ensure there is DevOps Course.