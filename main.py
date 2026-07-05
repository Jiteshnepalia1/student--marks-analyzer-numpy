"""
Student Marks Analyzer using NumPy

Author: Jitesh Nepalia
Version: 1.0.0

Description:
A beginner-friendly NumPy project for analyzing
student performance using statistical operations.
"""

import numpy as np


def main():
    """
    Main entry point of the Student Marks Analyzer project.

    Creates sample student data including roll numbers,
    student names, and marks, then displays the dataset
    and basic information about the marks array.
    """

    # creating array rooll_numbers
    roll_numbers = np.arange(101, 111)

    # Creating roll numbers array
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
    
    print("========== STUDENT DATA ==========")
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
    
    print("========== DATASET OVERVIEW ==========\n")
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
    print(f"Shape of marks: {marks.shape}")
    print(f"Dimension of marks: {marks.ndim}D")
    print(f"DataType of marks: {marks.dtype}")
    print(f"Size of marks: {marks.size}")

if __name__ == "__main__":
    main()

