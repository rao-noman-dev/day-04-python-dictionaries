# Python Day 4 — Dictionaries and Student Profile Manager

## Overview

This repository documents Day 4 of a structured Python Backend Development roadmap. The focus is Python dictionaries: representing data as key-value pairs, safely retrieving values, updating structured records, iterating through dictionary content, and working with nested dictionaries.

These concepts are directly relevant to backend development because dictionaries are commonly used to model request data, response data, configuration, and JSON-like records. The repository is intentionally beginner-level and educational. It focuses on clear procedural Python rather than production architecture.

## Repository Files

The public repository contains exactly four tracked files:

- `dictionary_basics.py` — dictionary fundamentals and focused demonstrations
- `practice_questions.py` — exactly 20 numbered dictionary exercises
- `student_profile_manager.py` — command-line mini project
- `README.md` — verified project documentation

## Dictionary Concepts Demonstrated

The runnable code demonstrates:

- Dictionary syntax and key-value pairs
- Direct access with square brackets: `dictionary["key"]`
- Safe access with `get()`
- Adding new keys
- Updating values directly
- Updating values with `update()`
- Removing values with `pop()`
- Storing and printing the value returned by `pop()`
- Removing keys with `del`
- Clearing safe temporary data with `clear()`
- Reading keys with `keys()`
- Reading values with `values()`
- Reading key-value pairs with `items()`
- Membership checks with `in`
- Looping through keys
- Looping through values
- Looping through key-value pairs
- Nested dictionaries
- Nested subject marks
- Total and average calculations
- Pass/Fail evaluation using an average boundary of 50
- A basic comparison between Python dictionaries and JSON objects

Python dictionaries and JSON objects both represent structured key-value data. Python uses values such as `True`, `False`, and `None`, while JSON uses `true`, `false`, and `null`.

## Exactly 20 Practice Exercises

`practice_questions.py` contains exactly 20 numbered exercises:

1. Create a student profile dictionary.
2. Access a value through its key.
3. Add a new key-value pair.
4. Update an existing value.
5. Remove a value with `pop()` and retain the removed value.
6. Check whether a key exists.
7. Display all dictionary keys.
8. Display all dictionary values.
9. Display all dictionary items.
10. Loop through dictionary keys.
11. Loop through dictionary values.
12. Loop through dictionary key-value pairs.
13. Create a product dictionary.
14. Increase a product price by 10 percent.
15. Create a subject-marks dictionary.
16. Calculate total marks.
17. Calculate average marks.
18. Determine Pass or Fail from the average.
19. Create a nested dictionary containing three students.
20. Safely retrieve a student record by ID with `get()`.

The demonstrations in `dictionary_basics.py` are supporting examples and are not counted as additional official exercises.

## Student Profile Manager

`student_profile_manager.py` is a command-line program that applies dictionary concepts to a structured student record.

Verified behavior includes:

- Collecting name, age, city, course, and marks
- Checking that the required text fields—name, city, and course—are not blank
- Storing subject marks inside a nested dictionary
- Validating that all marks remain within the inclusive range of 0 to 100
- Building a student profile dictionary from the accepted input
- Printing a readable initial student profile
- Updating city and course together
- Preserving the previous city and course when either update field is blank
- Safely searching for a profile field with `get()`
- Reporting a missing profile field without a key-access crash
- Calculating total marks
- Calculating average marks
- Returning `Pass` when the average is greater than or equal to 50
- Returning `Fail` when the average is below 50
- Printing a readable final student report

## Validation and Regression Coverage

The following scenarios were executed during Day 4:

### Fundamentals and exercises

- Dictionary fundamentals script executed successfully
- Safe lookup of a missing `email` key returned the configured fallback
- The valid nested `marks` key was accessed successfully
- All 20 practice exercises executed
- Exercise 20 returned an existing student for valid ID `3`
- Exercise 20 returned `Student not found` for missing ID `99`

### Student Profile Manager

- A complete valid workflow executed successfully
- Boundary marks `0`, `100`, and `50` produced total `150`, average `50.0`, and `Pass`
- Marks `40`, `45`, and `49` produced total `134`, an average below `50`, and `Fail`
- A mark of `101` triggered the marks-range validation message
- An empty required name triggered the required-fields validation message
- Blank city/course update input preserved the previous values
- A missing profile field such as `email` was handled safely
- A valid profile field such as `marks` was retrieved successfully
- All three Python files passed the final compilation check

### Independent repetition

A separate local-only repetition exercise also verified:

- Dictionary creation and update
- Salary increase from `5000` to `10000`
- Addition of a department
- Iteration through key-value pairs
- Successful employee lookup for valid ID `1`
- Safe missing-record handling for ID `3`

The independent repetition file is intentionally not part of the public repository.

## Running the Files

Run each file from the repository root:

```powershell
python dictionary_basics.py
python practice_questions.py
python student_profile_manager.py
```

Run the final compilation check:

```powershell
python -m py_compile dictionary_basics.py practice_questions.py student_profile_manager.py
```

## Known Limitations

This is an educational command-line project and does not claim production readiness.

Current limitations include:

- Age is converted to an integer but is not validated against an allowed range
- Non-numeric age or marks input is not caught and can raise `ValueError`
- Only city and course are supported in the update step
- Arbitrary profile-field updates are not supported
- No persistent storage
- No database
- No API
- No graphical user interface
- No classes
- No external packages
- No authentication
- No multi-user system
- Data resets whenever the program restarts
