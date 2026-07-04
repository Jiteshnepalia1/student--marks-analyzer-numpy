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
    print(f"Roll Numbers: {roll_numbers}")

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
    print(f"Student Names: {names}")

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
    print(marks)
    display_dataset_info(marks)

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

