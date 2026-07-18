# Day 4 - Python Dictionary Fundamentals

print("=== DICTIONARY SYNTAX AND DIRECT ACCESS ===")

student = {
    "name": "Usama",
    "age": 20,
    "city": "Lahore"
}

print("Complete student dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("City:", student["city"])


print("\n=== SAFE ACCESS USING get() ===")

print("Existing name:", student.get("name"))
print("Missing email:", student.get("email", "Not provided"))


print("\n=== ADD AND UPDATE OPERATIONS ===")

student["course"] = "Python Backend"
print("After adding course:", student)

student["age"] = 21
print("After direct age update:", student)

student.update({"city": "Islamabad"})
print("After update() city change:", student)


print("\n=== REMOVE USING pop() ===")

removed_course = student.pop("course")

print("Removed course:", removed_course)
print("After pop():", student)

print("\n=== REMOVE USING del ===")

student["course"] = "Python Backend"
print("Before del:", student)

del student["course"]

print("After del:", student)


print("\n=== SAFE clear() ON TEMPORARY DICTIONARY ===")

temporary_student = {
    "name": "Rao",
    "age": 18
}

print("Before clear():", temporary_student)

temporary_student.clear()

print("After clear():", temporary_student)

print("\n=== MEMBERSHIP CHECKS ===")

print("Does name key exist?", "name" in student)
print("Does email key exist?", "email" in student)


print("\n=== DICTIONARY METHODS ===")

print("All keys:", student.keys())
print("All values:", student.values())
print("All items:", student.items())


print("\n=== LOOP THROUGH KEYS ===")

for key in student.keys():
    print(key)


print("\n=== LOOP THROUGH VALUES ===")

for value in student.values():
    print(value)


print("\n=== LOOP THROUGH KEY-VALUE PAIRS ===")

for key, value in student.items():
    print(key, "=", value)

print("\n=== NESTED DICTIONARY ===")

students = {
    1: {
        "name": "Usama",
        "marks": {
            "math": 80,
            "english": 70,
            "computer": 90
        }
    }
}

print("Complete student record:", students[1])
print("Student name:", students[1]["name"])
print("Complete marks:", students[1]["marks"])
print("Computer marks:", students[1]["marks"]["computer"])


print("\n=== TOTAL, AVERAGE, AND RESULT ===")

math_marks = students[1]["marks"]["math"]
english_marks = students[1]["marks"]["english"]
computer_marks = students[1]["marks"]["computer"]

total_marks = math_marks + english_marks + computer_marks
average_marks = total_marks / 3

print("Total marks:", total_marks)
print("Average marks:", average_marks)

if average_marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

print("\n=== LIST INDEX VS DICTIONARY KEY ===")

student_list = ["Usama", 20, "Lahore"]

student_dictionary = {
    "name": "Usama",
    "age": 20,
    "city": "Lahore"
}

print("List value using index 0:", student_list[0])
print("Dictionary value using name key:", student_dictionary["name"])


print("\n=== BACKEND JSON-LIKE DATA ===")

api_response = {
    "status": "success",
    "student": {
        "name": "Usama",
        "course": "Python Backend"
    }
}

print("API-style dictionary:", api_response)
print("Nested student name:", api_response["student"]["name"])

print("Python dictionaries and JSON objects both use key-value data.")
print("Python uses True, False, and None; JSON uses true, false, and null.")
