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

def devops_start_date(student_info):
    for course in student_info["courses"]:
        if course["course_name"] == "DevOps":
            return course["start_date"]
        else: print("course name DevOps is not present")

start_date = devops_start_date(student_info)
print("DevOps Start Date: " + start_date)


# # your code should also ensure there is DevOps Course.

def devops(student_info):
    for course in student_info["courses"]:
        if course["start_date"] == "1234":
            return course["course_name"]

name = devops(student_info)
print("Course name " + name + " is present")

# print(student_info["course_name"])