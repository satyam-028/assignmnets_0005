# Create a dictionary with student names as keys and their marks as values
student_marks = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Eve": 91
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student {student_name} not found in the records.")
