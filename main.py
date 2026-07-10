"""
Student Marks Analyzer using NumPy

Author: Jitesh Nepalia
Version: 1.0.0

Description:
A beginner-friendly NumPy project for analyzing
student performance using statistical operations.
"""

import numpy as np

# creating subject array
SUBJECTS = np.array([
    "Maths",
    "Physics",
    "Chemistry",
    "English",
    "Computer"
])

def main():
    """
    Main entry point of the Student Marks Analyzer project.

    Creates sample student data including roll numbers,
    student names, and marks, then displays the dataset
    and basic information about the marks array.
    """

    # Create an array of student roll numbers.
    roll_numbers = np.arange(101, 111)

    # Create an array of student names.
    names = np.array([
        "Jitesh",
        "Aman",
        "Priya",
        "Rahul",
        "Anjali",
        "Arjun",
        "Sakshi",
        "Karan",
        "Neha",
        "Riya"
    ])

    # Subject order:
    # Maths, Physics, Chemistry, English, Computer
    marks = np.array([
        [95, 91, 88, 93, 97],  # Jitesh
        [82, 76, 85, 80, 79],  # Aman
        [91, 94, 89, 95, 92],  # Priya
        [68, 72, 70, 66, 74],  # Rahul
        [98, 96, 97, 99, 100], # Anjali
        [78, 81, 76, 83, 80],  # Arjun
        [87, 89, 91, 88, 90],  # Sakshi
        [73, 69, 75, 71, 72],  # Karan
        [64, 67, 65, 70, 68],  # Neha
        [93, 90, 94, 92, 95]   # Riya
    ])

    display_student_data(roll_numbers, names, marks)

    display_dataset_info(marks)

    explore_dataset(names, marks)

    show_student_marks(names, marks, "jitesh".capitalize())

    show_subject_marks(SUBJECTS, names, marks, "chemistry".capitalize())

    show_student_subject_mark(names, SUBJECTS, marks, "Sakshi".capitalize(), "chemistry".capitalize())

    show_students_range(names, marks, "jitesh".capitalize(), "Sakshi".capitalize())

    show_subject_range(SUBJECTS, names, marks, "Physics".capitalize(), "English".capitalize())

    show_student_subject_range(names, SUBJECTS, marks, "Physics".capitalize(), "English".capitalize(), "jitesh".capitalize(), "sakshi".capitalize())

    show_student_statistics(names, marks, "Jitesh".capitalize())

    show_subject_statistics(SUBJECTS, marks, "maths".capitalize())

    show_class_statistics(marks)

def display_student_data(
        roll_numbers: np.ndarray,
        names: np.ndarray,
        marks: np.ndarray
        ) -> None:
    """
    Display the complete student dataset.

    Parameters:
        roll_numbers (numpy.ndarray):
            A 1D array containing the roll numbers of all students.

        names (numpy.ndarray):
            A 1D array containing the names of all students.

        marks (numpy.ndarray):
            A 2D array containing the marks of all students.

    Displays:
        - Roll numbers
        - Student names
        - Marks matrix
    """
    
    print("\n========== STUDENT DATA ==========\n")
    print(f"Roll Numbers:\n{roll_numbers}\n")
    print(f"Student Names:\n{names}\n")
    print(f"Marks:\n{marks}")

def explore_dataset(
        names: np.ndarray,
        marks: np.ndarray
        ) -> None:
    """
    Explore the student dataset by displaying basic information.

    Parameters:
        names (numpy.ndarray):
            A 1D array containing the names of all students.

        marks (numpy.ndarray):
            A 2D array containing the marks of all students.

    Displays:
        - Total number of students
        - Total number of subjects
        - First student's name and marks
        - Last student's name and marks
    """
    
    print("\n========== DATASET OVERVIEW ==========\n")
    print(f"Total Students: {names.size}")
    print(f"Total Subjects: {marks.shape[1]}\n")

    print("First Student:")
    print(f"Name: {names[0]}")
    print(f"Marks: {marks[0]}\n")

    print("Last Student:")
    print(f"Name: {names[-1]}")
    print(f"Marks: {marks[-1]}")
    

def display_dataset_info(marks: np.ndarray) -> None:
    """
    Display basic information about the marks array.

    Parameters:
        marks (numpy.ndarray): A 2D NumPy array containing
        student marks for all subjects.

    Displays:
        - Shape
        - Number of dimensions
        - Data type
        - Total number of elements
    """
    # printing marks shape, dimension, datatype, size(number of items)
    print("\n========== DATASET INFORMATION ==========\n")

    print(f"Shape of marks    : {marks.shape}")
    print(f"Dimension of marks: {marks.ndim}D")
    print(f"DataType of marks : {marks.dtype}")
    print(f"Size of marks     : {marks.size}")

def show_student_marks(
        names: np.ndarray,
        marks: np.ndarray,
        name_of_student: str
) -> None:
    """
    Display the marks of a student by searching for their name.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        name_of_student (str):
            The name of the student whose marks are to be displayed.

    Displays:
        - Student name
        - Marks obtained in all subjects

    If the student name does not exist in the dataset, an error message is displayed.
    """
     
    # Check whether the student exists in the dataset.
    if name_of_student in names:

        # Find the index of names and marks
        index = np.where(names == name_of_student)[0][0]

        print("\n========== STUDENT MARKS ==========\n")
        print(f"Student : {names[index]}\n")
        print(f"Marks:\n{marks[index]}")

    else:
        print("\nInvalid student.")
        
def show_subject_marks(
        subjects: np.ndarray,
        names: np.ndarray,
        marks: np.ndarray,
        subject_name: str
) -> None:
    """
    Display the marks of all students for a given subject.

    Parameters:
        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        subject_name (str):
            The name of the subject whose marks are to be displayed.

    Displays:
        - Subject name
        - Marks of every student in the selected subject

    If the subject does not exist in the dataset, an error message is displayed.
    """
    
    # Check whether the subject exists in the dataset.
    if subject_name in subjects:

        # Find the column index of the selected subject.
        subject_index = np.where(subjects == subject_name)[0][0]

        print("\n========== SUBJECT MARKS ==========\n")
        print(f"Subject: {subjects[subject_index]}\n")

        for i in range(marks.shape[0]):
            print(f"{names[i] : <10} : {marks[i, subject_index]}")

    else:
        print("Invalid subject.")

def show_student_subject_mark(
        names: np.ndarray,
        subjects: np.ndarray,
        marks: np.ndarray,
        name_of_student: str,
        subject_name: str
) -> None:
    """
    Display the marks obtained by a specific student in a specific subject.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        name_of_student (str):
            The name of the student.

        subject_name (str):
            The name of the subject.

    Displays:
        - Student name
        - Subject name
        - Marks obtained in the selected subject

    If the student or subject does not exist in the dataset, an error message is displayed.
    """

    # Check whether the student exists.
    if name_of_student not in names:
        print("Student not found.")
        return
    
    if subject_name not in subjects:
        print("Subject not found.")
        return
    
    # Find the index of names and marks
    student_index = np.where(names == name_of_student)[0][0]

    # Find the column index of the selected subject.
    subject_index = np.where(subjects == subject_name)[0][0]

    print("\n========== STUDENT SUBJECT MARK ==========\n")
    print(f"Student : {names[student_index]}")
    print(f"Subject : {subjects[subject_index]}")
    print(f"Marks   : {marks[student_index, subject_index]}")

def show_students_range(
        names: np.ndarray,
        marks: np.ndarray,
        start_student_name: str,
        end_student_name: str
) -> None:
    """
    Display the marks of a range of students.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        start_student_name (str):
            The name of the first student in the range.

        end_student_name (str):
            The name of the last student in the range.

    Displays:
        - Student names within the specified range
        - Marks obtained by each student in all subjects

    If either student does not exist in the dataset or the start student
    comes after the end student, an appropriate error message is displayed.
    """
    
    # Check whether the student exists.
    if start_student_name not in names:
        print("Start student not found.")
        return
    
    # Check whether the student exists.
    if end_student_name not in names:
        print("End student not found.")
        return
    
    # Find the indices
    start_student_index = np.where(names == start_student_name)[0][0]
    end_student_index = np.where(names == end_student_name)[0][0]

    # Validate the order
    if start_student_index > end_student_index:
        print("The start student must come before the end student.")
        return
    
    # Slice the arrays
    names_of_students = names[start_student_index : end_student_index + 1]
    marks_of_students = marks[start_student_index : end_student_index + 1]

    print("\n========== STUDENT RANGE ==========\n")

    for i in range(marks_of_students.shape[0]):
        print(f"Student : {names_of_students[i]}")
        print(f"Marks   : {marks_of_students[i]}\n")

def show_subject_range(
        subjects: np.ndarray, 
        names: np.ndarray, 
        marks: np.ndarray, 
        start_subject_name: str, 
        end_subject_name: str
) -> None:
    """
    Display the marks of all students for a selected range of subjects.

    Parameters:
        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        start_subject_name (str):
            The name of the first subject in the range.

        end_subject_name (str):
            The name of the last subject in the range.

    Displays:
        - The selected subject range
        - Marks of every student for the selected subjects

    If either subject does not exist in the dataset or the start subject
    comes after the end subject, an appropriate error message is displayed.
    """
    
    # Check whether the subject exists.
    if start_subject_name not in subjects:
        print("Start subject not found.")
        return
    
    # Check whether the subject exists.
    if end_subject_name not in subjects:
        print("End subject not found.")
        return
    
    # Find the indices
    start_subject_index = np.where(subjects == start_subject_name)[0][0]
    end_subject_index = np.where(subjects == end_subject_name)[0][0]

    # Validate the order
    if start_subject_index > end_subject_index:
        print("The start subject must come before the end subject.")
        return
    
    # Slice the arrays
    selected_subjects = subjects[start_subject_index : end_subject_index + 1]

    # Sliced marks array
    marks_of_subjects = marks[:, start_subject_index : end_subject_index + 1]

    print("\n========== SUBJECT RANGE ==========\n")

    print(f"Subjects:\n{selected_subjects}\n")

    for i in range(names.shape[0]):
        print(f"{names[i] : <10} : {marks_of_subjects[i]}")

def show_student_subject_range(
        names: np.ndarray,
        subjects: np.ndarray,
        marks: np.ndarray,
        start_subject_name: str,
        end_subject_name: str,
        start_student_name: str,
        end_student_name: str
) -> None:
    """
    Display the marks of a selected range of students for a selected range of subjects.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        start_student_name (str):
            The name of the first student in the range.

        end_student_name (str):
            The name of the last student in the range.

        start_subject_name (str):
            The name of the first subject in the range.

        end_subject_name (str):
            The name of the last subject in the range.

    Displays:
        - The selected subject range
        - The selected student range
        - Marks of the selected students in the selected subjects

    If either student or subject does not exist in the dataset, or if
    the start value comes after the end value, an appropriate error
    message is displayed.
    """
    
    # Check whether the subject exists.
    if start_subject_name not in subjects:
        print("Start subject not found.")
        return
    
    # Check whether the subject exists.
    if end_subject_name not in subjects:
        print("End subject not found.")
        return
    
    # Check whether the student exists.
    if start_student_name not in names:
        print("Start student not found.")
        return
    
    # Check whether the student exists.
    if end_student_name not in names:
        print("End student not found.")
        return
    
    # Find the indices
    start_subject_index = np.where(subjects == start_subject_name)[0][0]
    end_subject_index = np.where(subjects == end_subject_name)[0][0]

    # Find the indices
    start_student_index = np.where(names == start_student_name)[0][0]
    end_student_index = np.where(names == end_student_name)[0][0]

    # Validate the order
    if start_subject_index > end_subject_index:
        print("The start subject must come before the end subject.")
        return
    
    # Validate the order
    if start_student_index > end_student_index:
        print("The start student must come before the end student.")
        return
    
    # Slice the arrays
    selected_subjects = subjects[start_subject_index : end_subject_index + 1]

    # Slice the student names.
    names_of_students = names[start_student_index : end_student_index + 1]

    # Slice both rows (students) and columns (subjects).
    selected_marks = marks[
        start_student_index : end_student_index + 1,
        start_subject_index : end_subject_index + 1
    ]

    print("\n========== STUDENT & SUBJECT RANGE ==========\n")

    print(f"Subjects:\n{selected_subjects}\n")

    for i in range(names_of_students.shape[0]):
        print(f"{names_of_students[i] :<10} : {selected_marks[i]}")

def show_student_statistics(
        names: np.ndarray,
        marks: np.ndarray,
        student_name: str
) -> None:
    """
    Display statistical information for a specific student.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        student_name (str):
            The name of the student whose statistics are to be displayed.

    Displays:
        - Student name
        - Marks in all subjects
        - Total marks
        - Average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance

    If the student does not exist in the dataset, an error message is displayed.
    """
    
    # Check whether the student exists.
    if student_name not in names:
        print("Student not found")
        return
    
    # Find the index of names and marks
    student_index = np.where(names == student_name)[0][0]

    # Marks of a student
    student_marks = marks[student_index]

    print("\n========== STUDENT STATISTICS ==========\n")

    print(f"Student : {names[student_index]}\n")
    print(f"Marks    : {student_marks}")

    print(f"Total    : {np.sum(student_marks)}")
    print(f"Average  : {np.mean(student_marks):.2f}")
    print(f"Highest  : {np.max(student_marks)}")
    print(f"Lowest   : {np.min(student_marks)}")
    print(f"Median   : {np.median(student_marks)}")
    print(f"Std Dev  : {np.std(student_marks):.2f}")
    print(f"Variance : {np.var(student_marks):.2f}")

def show_subject_statistics(
        subjects: np.ndarray,
        marks: np.ndarray,
        subject_name: str
) -> None:
    """
    Display statistical information for a specific subject.

    Parameters:
        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

        subject_name (str):
            The name of the subject whose statistics are to be displayed.

    Displays:
        - Subject name
        - Marks of all students in the subject
        - Total marks
        - Average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance

    If the subject does not exist in the dataset, an error message is displayed.
    """
    
    # Check whether the subject exists.
    if subject_name not in subjects:
        print("Subject not found.")
        return
    
    # Find the index of subject.
    subject_index = np.where(subjects == subject_name)[0][0]

    # Marks of subject.
    subject_marks = marks[:, subject_index]

    print("\n========== SUBJECT STATISTICS ==========\n")

    print(f"Subject : {subjects[subject_index]}\n")
    print(f"Marks      : {subject_marks}\n")

    print(f"Total      : {np.sum(subject_marks)}")
    print(f"Average    : {np.mean(subject_marks):.2f}")
    print(f"Highest    : {np.max(subject_marks)}")
    print(f"Lowest     : {np.min(subject_marks)}")
    print(f"Median     : {np.median(subject_marks):.2f}")
    print(f"Std Dev    : {np.std(subject_marks):.2f}")
    print(f"Variance   : {np.var(subject_marks):.2f}")

def show_class_statistics(marks: np.ndarray) -> None:
    """
    Display overall statistical information for the entire class.

    Parameters:
        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Total number of students
        - Total number of subjects
        - Overall average marks
        - Highest mark
        - Lowest mark
        - Median
        - Standard deviation
        - Variance
    """

    # Finding total students.
    total_students = marks.shape[0]

    # Finding total subjects.
    total_subjects = marks.shape[1]

    print("\n========== CLASS STATISTICS ==========\n")

    print(f"Total Students : {total_students}")
    print(f"Total Subjects : {total_subjects}\n")

    print(f"Overall Average    : {np.mean(marks):.2f}\n")
    print(f"Highest Mark       : {np.max(marks)}\n")
    print(f"Lowest Mark        : {np.min(marks)}\n")
    print(f"Median             : {np.median(marks):.2f}\n")
    print(f"Standard Deviation : {np.std(marks):.2f}\n")
    print(f"Variance           : {np.var(marks):.2f}")

if __name__ == "__main__":
    main()