class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Use the sorted function with a custom key function to sort by CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with sample student data
if __name__ == "__main__":
    # Sample student objects
    students = [
        Student("Alice", "A101", 3.8),
        Student("Bob", "B102", 3.9),
        Student("Charlie", "C103", 3.5),
        Student("David", "D104", 3.7),
    ]

    # Sort the students by CGPA
    sorted_students = sort_students(students)

    # Print the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
