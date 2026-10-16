# Student Information Dictionary

# Storing student details
students = {
    101: {"name": "Kiran", "age": 23, "course": "MCA", "marks": 85},
    102: {"name": "Ravi", "age": 22, "course": "MCA", "marks": 90},
    103: {"name": "Priya", "age": 21, "course": "MCA", "marks": 88}
}

# Display student details
def display_students():
    print("Student Details:")
    for sid, info in students.items():
        print("ID:", sid, "| Details:", info)

# Search for a student using ID
def search_student(sid):
    if sid in students:
        print("Student details found:", students[sid])
    else:
        print("Student not found.")

# Add a new student
def add_student(sid, name, age, course, marks):
    if sid in students:
        print("This student ID already exists.")
    else:
        students[sid] = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }
        print("New student added successfully.")

# Update student details
def update_student(sid, field, value):
    if sid in students:
        if field in students[sid]:
            students[sid][field] = value
            print("Student details updated successfully.")
        else:
            print("Please enter a valid field name.")
    else:
        print("Student not found.")

# Performing the operations
display_students()

print("\nSearch Operation:")
search_student(101)

print("\nAdd Operation:")
add_student(104, "Suresh", 22, "MCA", 82)

print("\nUpdate Operation:")
update_student(104, "marks", 90)

print("\nUpdated Student List:")
display_students()
