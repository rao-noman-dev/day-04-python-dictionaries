# Day 4 - Python Dictionary Practice Exercises


# Exercise 1
# Create a student profile dictionary
student_profile = {
    "name": "Noman",
    "age": 18,
    "city": "Lahore",
}
print("Student profile:", student_profile)


# Exercise 2
# Access a value using its key
print("Student name:", student_profile["name"])


# Exercise 3
# Add a new key-value pair
student_profile["email"] = "raonoman@example.com"
print("Profile after adding email:", student_profile)


# Exercise 4
# Update an existing value
student_profile.update({"age": 20})
print("Profile after updating age:", student_profile)


# Exercise 5
# Remove a key-value pair using pop()
removed_city = student_profile.pop("city")
print("Removed city:", removed_city)
print("Profile after removing city:", student_profile)


# Exercise 6
# Check whether a key exists
print("Does the name key exist?", "name" in student_profile)


# Exercise 7
# Display all dictionary keys
print("Profile keys:", student_profile.keys())


# Exercise 8
# Display all dictionary values
print("Profile values:", student_profile.values())


# Exercise 9
# Display all dictionary items
print("Profile items:", student_profile.items())


# Exercise 10
# Loop through dictionary keys
print("Profile keys:")
for key in student_profile.keys():
    print(key)


# Exercise 11
# Loop through dictionary values
print("Profile values:")
for value in student_profile.values():
    print(value)


# Exercise 12
# Loop through dictionary keys and values
print("Profile details:")
for key, value in student_profile.items():
    print(key, "=", value)


# Exercise 13
# Create a product dictionary
product = {
    "name": "Biscuits",
    "price": 10,
    "stock": 100,
}
print("Product:", product)


# Exercise 14
# Increase the product price by 10%
current_price = product["price"]
price_increase = current_price * 0.10
product["price"] = current_price + price_increase

print("Product after price increase:", product)


# Exercise 15
# Create a marks dictionary
marks = {
    "math": 70,
    "english": 80,
    "computer": 90,
}
print("Subject marks:", marks)


# Exercise 16
# Calculate total marks
math_marks = marks["math"]
english_marks = marks["english"]
computer_marks = marks["computer"]

total_marks = math_marks + english_marks + computer_marks
print("Total marks:", total_marks)


# Exercise 17
# Calculate average marks
average_marks = total_marks / len(marks)
print("Average marks:", average_marks)


# Exercise 18
# Determine pass or fail status
if average_marks >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")


# Exercise 19
# Create a nested dictionary for three students
students = {
    1: {
        "name": "Usama",
        "age": 20,
    },
    2: {
        "name": "Noman",
        "age": 18,
    },
    3: {
        "name": "Raza",
        "age": 22,
    },
}
print("Students:", students)


# Exercise 20
# Safely retrieve a value by entering a dictionary key
profile_data = {
    "name": "Noman",
    "course": "Python Backend",
    "city": "Lahore",
}

dictionary_key = input("Enter a dictionary key: ").strip().lower()
dictionary_value = profile_data.get(dictionary_key)

if dictionary_value is not None:
    print("Value:", dictionary_value)
else:
    print("Key not found")
