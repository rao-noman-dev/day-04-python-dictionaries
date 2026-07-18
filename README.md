# Python Day 4 — Dictionaries and Student Profile Manager

## Overview

This repository documents Day 4 of a structured Python Backend Development roadmap. The focus is Python dictionaries: key-value storage, direct and safe access, dictionary updates, removal methods, iteration, nested structures, and practical validation.

These concepts are relevant to backend development because dictionaries are commonly used to represent request data, response data, configuration, and JSON-like records. The project remains beginner-friendly and educational, using procedural Python without custom functions, classes, databases, APIs, or external packages.

## Repository Files

The public repository tracks exactly four files:

- `dictionary_basics.py` — dictionary fundamentals and executable demonstrations
- `practice_questions.py` — exactly 20 numbered dictionary exercises
- `student_profile_manager.py` — command-line mini project
- `README.md` — verified documentation

Local evidence files such as `notes.md`, `DAY_4_HANDOFF.md`, the regression script, transcripts, screenshots, and the LinkedIn infographic are intentionally not tracked.

## Dictionary Concepts Demonstrated

The runnable code demonstrates:

- Dictionary syntax and key-value pairs
- Direct access with square brackets
- Safe access with `get()`
- Adding keys
- Direct value updates
- `update()`
- `pop()` and its returned value
- `del`
- `clear()` on temporary data
- `keys()`
- `values()`
- `items()`
- Membership checks
- Loops over keys
- Loops over values
- Loops over key-value pairs
- Nested dictionaries
- Nested subject marks
- Total and average calculations
- Pass/Fail evaluation at an average boundary of 50
- List index versus dictionary key
- Python dictionary versus JSON-object comparison

Python dictionaries and JSON objects both represent structured key-value data. Python uses values such as `True`, `False`, and `None`, while JSON uses `true`, `false`, and `null`.

## Exactly 20 Practice Exercises

`practice_questions.py` contains exactly 20 numbered exercises and no Exercise 21:

1. Create a student profile dictionary.
2. Access a value using a key.
3. Add a new key-value pair.
4. Update an existing value.
5. Remove a key with `pop()` and retain the removed value.
6. Check whether a key exists.
7. Display all keys.
8. Display all values.
9. Display all items.
10. Loop through keys.
11. Loop through values.
12. Loop through key-value pairs.
13. Create a product dictionary.
14. Increase product price by 10 percent.
15. Create a marks dictionary.
16. Calculate total marks.
17. Calculate average marks.
18. Determine Pass or Fail.
19. Create a nested dictionary for three students.
20. Ask for a dictionary key and safely return the matching value or a not-found result.

Exercise 20 uses `get()` with a simple dictionary. It does not ask for a student ID.

## Student Profile Manager

`student_profile_manager.py` applies dictionary concepts to a structured student record.

Implemented behavior includes:

- Reading name, age, city, course, and three subject marks
- Stripping surrounding whitespace from text input
- Rejecting blank name, age, city, and course
- Safely handling non-numeric age
- Rejecting zero and negative age
- Accepting a positive integer age
- Safely handling blank and non-numeric marks
- Accepting marks from 0 through 100
- Rejecting marks below 0 or above 100
- Preventing invalid marks from entering total and average calculations
- Storing valid marks in a nested dictionary
- Printing an initial student profile
- Displaying a missing email as `Not provided`
- Asking whether to update `city` or `course`
- Normalizing the selected update target with `strip()` and `lower()`
- Updating only the selected field
- Rejecting blank or spaces-only updated values
- Rejecting unsupported update targets
- Preserving the original dictionary when the update target or value is invalid
- Keeping the non-selected field unchanged
- Calculating total and average marks
- Returning `Pass` when average is greater than or equal to 50
- Returning `Fail` when average is below 50
- Printing a readable final report

## Validation and Regression Coverage

The corrected implementation was executed through an automated PowerShell regression script.

### Compilation and structure

- All three Python files compiled successfully
- Compilation exit code was `0`
- Exercise heading count was exactly `20`
- Exercise 21 was absent

### Exercise 20

- Existing key `city` returned `Value: Lahore`
- Missing key `email` returned `Key not found`

### Profile validation

- Valid positive age was accepted
- Blank name was rejected
- Spaces-only name was rejected
- Blank age was rejected
- Age `0` was rejected
- Negative age was rejected
- Non-numeric age was rejected without crashing
- Blank city was rejected
- Blank course was rejected

### Marks validation

- Normal valid marks completed successfully
- Blank marks input was rejected
- Non-numeric marks input was rejected without crashing
- A mark below `0` was rejected
- A mark above `100` was rejected
- Marks `0`, `100`, and `50` were accepted
- Average exactly `50.0` returned `Pass`
- Marks `40`, `45`, and `49` produced total `134` and `Fail`
- Marks `80`, `70`, and `90` produced total `240`, average `80.0`, and `Pass`

### Update behavior

- Valid city update changed only city
- Valid course update changed only course
- Blank updated value preserved the original profile
- Spaces-only updated value preserved the original profile
- Unsupported target was rejected
- Invalid updates preserved city and course
- Valid updates appeared in the final profile
- The non-selected field remained unchanged

### Integrated workflow

A successful complete workflow verified:

- Initial profile output
- Nested marks
- Missing email fallback: `Not provided`
- Valid city update
- Total marks
- Average marks
- Pass result
- Final updated profile

Regression evidence is stored locally and is not part of the public repository.

## Running the Files

From the repository root:

```powershell
python dictionary_basics.py
python practice_questions.py
python student_profile_manager.py
```

Final compilation command:

```powershell
python -m py_compile dictionary_basics.py practice_questions.py student_profile_manager.py
```

## Known Limitations

This is an educational command-line project and does not claim production readiness.

Current limitations:

- No persistent storage
- No database
- No API
- No graphical user interface
- No custom functions
- No classes
- No external packages
- No authentication
- No multi-user architecture
- No complex menu system
- Data resets when the program restarts
