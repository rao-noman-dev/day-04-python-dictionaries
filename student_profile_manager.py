# Day 4 Mini Project
# Student Profile Manager

print("=" * 35)
print("Student Profile Manager")
print("=" * 35)

# Step 1: Get basic student information
name = input("Enter student name: ").strip()
age_input = input("Enter student age: ").strip()
city = input("Enter student city: ").strip()
course = input("Enter enrolled course: ").strip()

# Step 2: Validate basic profile information
profile_is_valid = True
age = None

if name == "":
    print("Name cannot be empty.")
    profile_is_valid = False

if age_input == "":
    print("Age cannot be empty.")
    profile_is_valid = False
else:
    try:
        age = int(age_input)
    except ValueError:
        print("Age must be a whole number.")
        profile_is_valid = False
    else:
        if age <= 0:
            print("Age must be greater than 0.")
            profile_is_valid = False

if city == "":
    print("City cannot be empty.")
    profile_is_valid = False

if course == "":
    print("Course cannot be empty.")
    profile_is_valid = False

if profile_is_valid:
    # Step 3: Get student marks
    math_input = input("Enter math marks: ").strip()
    english_input = input("Enter English marks: ").strip()
    computer_input = input("Enter computer marks: ").strip()

    # Step 4: Validate marks input
    marks_are_valid = True
    math_marks = None
    english_marks = None
    computer_marks = None

    if (
        math_input == ""
        or english_input == ""
        or computer_input == ""
    ):
        print("Marks cannot be empty.")
        marks_are_valid = False
    else:
        try:
            math_marks = int(math_input)
            english_marks = int(english_input)
            computer_marks = int(computer_input)
        except ValueError:
            print("Marks must be whole numbers.")
            marks_are_valid = False

    if marks_are_valid:
        if (
            math_marks < 0
            or math_marks > 100
            or english_marks < 0
            or english_marks > 100
            or computer_marks < 0
            or computer_marks > 100
        ):
            print("Marks must be between 0 and 100.")
            marks_are_valid = False

    if marks_are_valid:
        # Step 5: Create nested marks dictionary
        marks = {
            "math": math_marks,
            "english": english_marks,
            "computer": computer_marks,
        }

        # Step 6: Create student profile dictionary
        student_profile = {
            "name": name,
            "age": age,
            "city": city,
            "course": course,
            "marks": marks,
        }

        # Step 7: Display initial student profile
        print("\nInitial Student Profile")
        print("-" * 35)

        for key, value in student_profile.items():
            if key == "marks":
                print("Marks:")

                for subject, score in value.items():
                    print(subject, ":", score)

            else:
                print(key, ":", value)

        print("Email:", student_profile.get("email", "Not provided"))

        # Step 8: Update either city or course
        print("\nUpdate Student Profile")
        print("-" * 35)

        update_field = input(
            "Enter field to update (city/course): "
        ).strip().lower()

        if update_field == "city" or update_field == "course":
            updated_value = input(
                "Enter updated " + update_field + ": "
            ).strip()

            if updated_value == "":
                print("Updated value cannot be empty.")
                print("Previous profile data has been preserved.")
            else:
                student_profile[update_field] = updated_value
                print(update_field, "updated successfully.")
        else:
            print("Unsupported update field.")
            print("Only city or course can be updated.")
            print("Previous profile data has been preserved.")

        # Step 9: Calculate total marks
        total_marks = (
            marks["math"]
            + marks["english"]
            + marks["computer"]
        )

        # Step 10: Calculate average marks
        average_marks = total_marks / len(marks)

        # Step 11: Determine pass or fail result
        if average_marks >= 50:
            result = "Pass"
        else:
            result = "Fail"

        # Step 12: Display final student report
        print("\nFinal Student Report")
        print("=" * 35)

        print("Name:", student_profile.get("name"))
        print("Age:", student_profile.get("age"))
        print("City:", student_profile.get("city"))
        print("Course:", student_profile.get("course"))
        print("Email:", student_profile.get("email", "Not provided"))

        print("\nMarks:")

        final_marks = student_profile.get("marks")

        for subject, score in final_marks.items():
            print(subject, ":", score)

        print("\nTotal Marks:", total_marks)
        print("Average Marks:", average_marks)
        print("Result:", result)

        print("=" * 35)
