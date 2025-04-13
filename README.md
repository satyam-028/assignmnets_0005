task 1 

Create a dictionary with student names as keys and their marks as values
student_marks = { "John": 85, "Alice": 92, "Bob": 78, "Eve": 91 }

Ask the user to input a student's name
student_name = input("Enter the student's name: ")

Retrieve and display the corresponding marks
if student_name in student_marks: print(f"{student_name}'s marks: {student_marks[student_name]}") else: print(f"Student {student_name} not found in the records.")


task 2 

Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Extract the first five elements from the list
first_five = numbers[:5]

Reverse the extracted elements
reversed_first_five = first_five[::-1]

Print both the extracted list and the reversed list
print("Extracted first five elements:", first_five) print("Reversed extracted elements:", reversed_first_five)
