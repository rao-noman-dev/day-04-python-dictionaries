# Day_4 Mini Project
# Student Profile Manager

print("=" * 35)
print("Student Profile Manager")
print("=" * 35)

# Step 1: Get basic student information
name = input("Enter student name: ").strip()
age = int(input("Enter student age: "))
city = input("Enter student city: ").strip()
course = input("Enter enrolled course: ").strip()

# Step 2: Validate required profile fields
if name == "" or city == "" or course == "":
    print("Profile fields cannot be empty.")

else:
    # Step 3: Get student marks
    math_marks = int(input("Enter math marks: "))
    english_marks = int(input("Enter English marks: "))
    computer_marks = int(input("Enter computer marks: "))

    # Step 4: Validate marks range
    if (
        math_marks < 0
        or math_marks > 100
        or english_marks < 0
        or english_marks > 100
        or computer_marks < 0
        or computer_marks > 100
    ):
        print("Marks must be between 0 and 100.")

    else:
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

        # Step 8: Update city and course
        print("\nUpdate Student Profile")
        print("-" * 35)

        updated_city = input("Enter updated city: ").strip()
        updated_course = input("Enter updated course: ").strip()

        if updated_city != "" and updated_course != "":
            student_profile["city"] = updated_city
            student_profile["course"] = updated_course
        else:
            print("Updated fields cannot be empty.")
            print("Previous city and course have been preserved.")

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

        # Step 12: Safely search for a profile field
        print("\nSearch Student Profile")
        print("-" * 35)

        profile_field = input(
            "Enter a profile field name: "
        ).strip().lower()

        field_value = student_profile.get(profile_field)

        if field_value is not None:
            print(profile_field, ":", field_value)
        else:
            print("Profile field not found.")

        # Step 13: Display final student report
        print("\nFinal Student Report")
        print("=" * 35)

        print("Name:", student_profile.get("name"))
        print("Age:", student_profile.get("age"))
        print("City:", student_profile.get("city"))
        print("Course:", student_profile.get("course"))

        print("\nMarks:")

        final_marks = student_profile.get("marks")

        for subject, score in final_marks.items():
            print(subject, ":", score)

        print("\nTotal Marks:", total_marks)
        print("Average Marks:", average_marks)
        print("Result:", result)

        print("=" * 35)