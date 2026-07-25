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

# ---------------- LOGIN CREDENTIALS ---------------- #

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin@123"

MAX_LOGIN_ATTEMPTS = 3

# ---------------- LOGIN SCREEN ---------------- #

def show_login_screen() -> str:
    """
    Display the login screen and return the user's role choice.

    Returns:
        str: The user's choice ('1' for Student, '2' for Admin, '0' for Exit).
    """

    print("\n" + "=" * 50)
    print("     STUDENT MARKS ANALYZER - LOGIN".center(42))
    print("=" * 50)
    print(" 1. Login as Student")
    print(" 2. Login as Admin")
    print(" 0. Exit")
    print("=" * 50)

    return input("\nEnter Your Choice: ").strip()

def admin_login() -> bool:
    """
    Authenticate the admin using username and password.

    Allows up to MAX_LOGIN_ATTEMPTS attempts before
    returning to the login screen.

    Returns:
        bool: True if login is successful, False otherwise.
    """

    print("\n" + "=" * 50)
    print("             ADMIN LOGIN")
    print("=" * 50)

    for attempt in range(1, MAX_LOGIN_ATTEMPTS + 1):

        username = input("Enter Admin Username : ").strip()
        password = input("Enter Admin Password : ").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            print("\nWelcome, Admin!")
            return True

        remaining = MAX_LOGIN_ATTEMPTS - attempt

        if remaining > 0:
            print(f"\nInvalid credentials. {remaining} attempt(s) remaining.\n")
        else:
            print("\nMaximum attempts reached. Returning to login screen.")

    return False

# ---------------- MENUS ---------------- #

def show_admin_menu() -> None:
    """Display the admin menu with full access to all features."""

    print("\n" + "=" * 50)
    print("      ADMIN - STUDENT MARKS ANALYZER")
    print("=" * 50)

    print(" 1. Display Student Data")
    print(" 2. Display Dataset Information")
    print(" 3. Explore Dataset")
    print(" 4. Show Student Marks")
    print(" 5. Show Subject Marks")
    print(" 6. Show Student Subject Mark")
    print(" 7. Show Students Range")
    print(" 8. Show Subject Range")
    print(" 9. Show Student Subject Range")
    print("10. Show Student Statistics")
    print("11. Show Subject Statistics")
    print("12. Show Class Statistics")
    print("13. Show Student Ranking")
    print("14. Show Topper & Lowest Student")
    print("15. Show Subject Toppers")
    print("16. Show Passed Students")
    print("17. Show Failed Students")
    print("18. Show Students Above Average")
    print("19. Show Students Below Average")
    print("20. Show Students With Full Marks")
    print("21. Show Failed Subjects")
    print("22. Generate Student Report")
    print(" 0. Logout")

    print("=" * 50)

def show_student_menu() -> None:
    """Display the student menu with limited access to own data only."""

    print("\n" + "=" * 50)
    print("     STUDENT - MARKS ANALYZER")
    print("=" * 50)

    print(" 1. Show My Marks")
    print(" 2. Show My Subject Mark")
    print(" 3. Show My Statistics")
    print(" 4. Show My Ranking")
    print(" 5. Generate My Report")
    print(" 0. Logout")

    print("=" * 50)
    
# ---------------- AUTHENTICATION ---------------- #

def student_login(
        names: np.ndarray,
        roll_numbers: np.ndarray
) -> tuple[int, str, int] | None:
    """
    Authenticate a student using their name and roll number.

    Allows up to MAX_LOGIN_ATTEMPTS attempts before
    returning to the login screen.

    Parameters:
        names (numpy.ndarray):
            Array containing student names.

        roll_numbers (numpy.ndarray):
            Array containing student roll numbers.

    Returns:
        tuple | None:
            (student_index, student_name, student_roll_number)
            on success, or None on failure.
    """

    print("\n" + "=" * 50)
    print("             STUDENT LOGIN")
    print("=" * 50)

    for attempt in range(1, MAX_LOGIN_ATTEMPTS + 1):

        username = input("Enter Student Name : ").strip().capitalize()

        try:
            password = int(input("Enter Roll Number  : "))
        except ValueError:
            print("\nRoll number must be a number.")
            remaining = MAX_LOGIN_ATTEMPTS - attempt
            if remaining > 0:
                print(f"{remaining} attempt(s) remaining.\n")
            else:
                print("\nMaximum attempts reached. Returning to login screen.")
            continue

        # Check whether the student exists.
        if username not in names:
            remaining = MAX_LOGIN_ATTEMPTS - attempt
            if remaining > 0:
                print(f"\nInvalid Student Name. {remaining} attempt(s) remaining.\n")
            else:
                print("\nMaximum attempts reached. Returning to login screen.")
            continue

        # Find student index.
        student_index = np.where(names == username)[0][0]

        # Verify roll number.
        if password != (roll_numbers[student_index]):
            remaining = MAX_LOGIN_ATTEMPTS - attempt
            if remaining > 0:
                print(f"\nInvalid Roll Number. {remaining} attempt(s) remaining.\n")
            else:
                print("\nMaximum attempts reached. Returning to login screen.")
            continue

        print(f"\nWelcome, {username}!")

        return (
            student_index,
            names[student_index],
            roll_numbers[student_index]
        )

    return None

# ---------------- SESSION HANDLERS ---------------- #

def student_session(
        names: np.ndarray,
        roll_numbers: np.ndarray,
        marks: np.ndarray,
        logged_in_student: str,
) -> None:
    """
    Handle the student session with limited menu access.

    Students can only view their own data:
    marks, subject marks, statistics, ranking, and report.

    Parameters:
        names (numpy.ndarray): Array of student names.
        roll_numbers (numpy.ndarray): Array of roll numbers.
        marks (numpy.ndarray): 2D array of marks.
        student_index (int): Index of the logged-in student.
        logged_in_student (str): Name of the logged-in student.
        logged_in_roll (int): Roll number of the logged-in student.
    """

    while True:

        show_student_menu()

        choice = input("\nEnter Your Choice: ").strip()

        if choice == "1":
            show_student_marks(names, marks, logged_in_student)

        elif choice == "2":
            subject = input("Enter Subject Name: ").strip().capitalize()
            show_student_subject_mark(
                names, SUBJECTS, marks, logged_in_student, subject
            )

        elif choice == "3":
            show_student_statistics(names, marks, logged_in_student)

        elif choice == "4":
            show_student_ranking(names, marks)

        elif choice == "5":
            generate_student_report(
                names, roll_numbers, SUBJECTS, marks, logged_in_student
            )

        elif choice == "0":
            print(f"\nGoodbye, {logged_in_student}!")
            break

        else:
            print("\nInvalid Choice. Please try again.")

        input("\nPress Enter to continue...")

def admin_session(
        names: np.ndarray,
        roll_numbers: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Handle the admin session with full menu access.

    Admin can access all features and view any student's data
    by entering student/subject names interactively.

    Parameters:
        names (numpy.ndarray): Array of student names.
        roll_numbers (numpy.ndarray): Array of roll numbers.
        marks (numpy.ndarray): 2D array of marks.
    """

    while True:

        show_admin_menu()

        choice = input("\nEnter Your Choice: ").strip()

        if choice == "1":
            display_student_data(roll_numbers, names, marks)

        elif choice == "2":
            display_dataset_info(marks)

        elif choice == "3":
            explore_dataset(names, marks)

        elif choice == "4":
            student = input("Enter Student Name: ").strip().capitalize()
            show_student_marks(names, marks, student)

        elif choice == "5":
            subject = input("Enter Subject Name: ").strip().capitalize()
            show_subject_marks(SUBJECTS, names, marks, subject)

        elif choice == "6":
            student = input("Enter Student Name: ").strip().capitalize()
            subject = input("Enter Subject Name: ").strip().capitalize()
            show_student_subject_mark(names, SUBJECTS, marks, student, subject)

        elif choice == "7":
            start = input("Enter Start Student Name: ").strip().capitalize()
            end = input("Enter End Student Name  : ").strip().capitalize()
            show_students_range(names, marks, start, end)

        elif choice == "8":
            start = input("Enter Start Subject Name: ").strip().capitalize()
            end = input("Enter End Subject Name  : ").strip().capitalize()
            show_subject_range(SUBJECTS, names, marks, start, end)

        elif choice == "9":
            start_sub = input("Enter Start Subject Name: ").strip().capitalize()
            end_sub = input("Enter End Subject Name  : ").strip().capitalize()
            start_stu = input("Enter Start Student Name: ").strip().capitalize()
            end_stu = input("Enter End Student Name  : ").strip().capitalize()
            show_student_subject_range(
                names, SUBJECTS, marks,
                start_sub, end_sub, start_stu, end_stu
            )

        elif choice == "10":
            student = input("Enter Student Name: ").strip().capitalize()
            show_student_statistics(names, marks, student)

        elif choice == "11":
            subject = input("Enter Subject Name: ").strip().capitalize()
            show_subject_statistics(SUBJECTS, marks, subject)

        elif choice == "12":
            show_class_statistics(marks)

        elif choice == "13":
            show_student_ranking(names, marks)

        elif choice == "14":
            show_topper_and_lowest_student(names, marks)

        elif choice == "15":
            show_subject_toppers(names, SUBJECTS, marks)

        elif choice == "16":
            show_passed_students(names, marks)

        elif choice == "17":
            show_failed_students(names, marks)

        elif choice == "18":
            show_students_above_average(names, marks)

        elif choice == "19":
            show_students_below_average(names, marks)

        elif choice == "20":
            show_students_with_full_marks(names, SUBJECTS, marks)

        elif choice == "21":
            show_failed_subjects(names, SUBJECTS, marks)

        elif choice == "22":
            student = input("Enter Student Name: ").strip().capitalize()
            generate_student_report(
                names, roll_numbers, SUBJECTS, marks, student
            )

        elif choice == "0":
            print("\nAdmin logged out.")
            break

        else:
            print("\nInvalid Choice. Please try again.")

        input("\nPress Enter to continue...")

# ---------------- MAIN ---------------- #

def main():
    """
    Main entry point of the Student Marks Analyzer project.

    Displays a login screen where users can choose to login
    as a Student (limited access) or Admin (full access).
    After logout, returns to the login screen.
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

    # Outer loop: Login screen
    while True:

        role_choice = show_login_screen()

        # --- Student Login ---
        if role_choice == "1":

            result = student_login(names, roll_numbers)

            if result is None:
                continue

            student_index, logged_in_student, logged_in_roll = result

            student_session(
                names, roll_numbers, marks, logged_in_student
            )

        # --- Admin Login ---
        elif role_choice == "2":

            if admin_login():
                admin_session(names, roll_numbers, marks)

        # --- Exit ---
        elif role_choice == "0":
            print("\nThank you for using Student Marks Analyzer!")
            break

        else:
            print("\nInvalid Choice. Please try again.")

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

def show_student_ranking(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display the ranking of all students based on their total marks.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Students ranked from highest to lowest total marks
        - Rank number
        - Student name
        - Total marks

    Ranking is determined by calculating the total marks of each student
    and sorting them in descending order.
    """
    
    # Calculate the total marks of each student.
    student_totals = np.sum(marks, axis=1)

    # Student indices sorted in descending order of total marks.
    ranking = np.argsort(student_totals)[::-1]

    print("\n========== STUDENT RANKING ==========\n")

    for rank, index in enumerate(ranking, start=1):
        print(f"{rank:<2}. {names[index]:<10} : {student_totals[index]}")

def show_topper_and_lowest_student(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display the topper and lowest-scoring student based on total marks.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Topper's name
        - Topper's total marks
        - Lowest-scoring student's name
        - Lowest-scoring student's total marks

    Ranking is determined by calculating the total marks of each student
    and selecting the highest and lowest totals using NumPy functions.
    """
    
    # Calculate the total marks of each student.
    student_totals = np.sum(marks, axis=1)

    # Topper student marks indices.
    topper_index = np.argmax(student_totals)

    # Lowest student marks indices.
    lowest_index = np.argmin(student_totals)

    print("\n========== TOPPER & LOWEST STUDENT ==========\n")

    print("Topper")
    print("-------")
    print(f"Name        : {names[topper_index]}")
    print(f"Total Marks : {student_totals[topper_index]}\n")

    print("Lowest")
    print("------")
    print(f"Name        : {names[lowest_index]}")
    print(f"Total Marks : {student_totals[lowest_index]}")

def show_subject_toppers(
        names: np.ndarray,
        subjects: np.ndarray,
        marks : np.ndarray
) -> None:
    """
    Display the topper of each subject.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Subject name
        - Top-ranked student in each subject
        - Highest marks obtained in that subject

    The topper for each subject is determined using NumPy's
    argmax() function along axis=0.
    """

    # Indices of max marks in subjects 
    topper_indices = np.argmax(marks, axis=0)

    # Maximum marks in subjects
    topper_marks = np.max(marks, axis=0)

    print("\n========== SUBJECT TOPPERS ==========\n")

    for index, i in enumerate(topper_indices, start=0):
        print(f"{subjects[index]}")
        print("-" * len(subjects[index]))
        print(f"Rank 1 : {names[i]}")
        print(f"Marks  : {topper_marks[index]}\n")
    
def show_passed_students(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display the names of students who have passed in all subjects.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Names of students who have passed every subject
        - Total number of passed students

    A student is considered passed only if they score at least
    40 marks in every subject.
    """
    
    # Passing marks = 40
    PASS_MARKS = 40

    # Students pass in subject
    student_pass_subjects = marks >= PASS_MARKS

    # Filter pass students
    passed_students = np.all(student_pass_subjects, axis=1)

    print("\n========== PASSED STUDENTS ==========\n")

    for index in np.where(passed_students)[0]:
        print(names[index])

    print(f"\nTotal passed students : {np.sum(passed_students)}")

def show_failed_students(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
     Display the names of students who have failed in one or more subjects.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Names of students who have failed in at least one subject
        - Total number of failed students

    A student is considered failed if they score less than
    40 marks in any subject.
    """

    # Passing marks = 40
    PASS_MARKS = 40

    # Students failed in one or more subjects
    student_fail_subjects = marks < PASS_MARKS

    # Filter failed students
    failed_students = np.any(student_fail_subjects, axis=1)

    print("\n========== FAILED STUDENTS ==========\n")

    for index in np.where(failed_students)[0]:
        print(names[index])
    
    print(f"\nTotal Failed Students : {np.sum(failed_students)}") 

def show_students_above_average(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display the students whose total marks are above the class average.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Class average total marks
        - Names of students scoring above the class average
        - Total marks of each selected student
        - Total number of students above the class average

    The class average is calculated using the total marks
    obtained by each student.
    """

    # Total marks of each student.
    students_total = marks.sum(axis=1)

    # Average total marks of the class.
    average_total = students_total.mean()

    # checking above average students.
    above_average_students = students_total > average_total

    # Filter the above average students. 
    indices = np.where(above_average_students)[0]
    
    print("\n========== STUDENTS ABOVE AVERAGE ==========\n")

    print(f"Class Average Total : {average_total:.2f}\n")

    for index in indices:
        print(f"{names[index]:<10} : {students_total[index]}")
    
    print(f"Total Students : {indices.size}")

def show_students_below_average(
        names: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display the students whose total marks are below the class average.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Class average total marks
        - Names of students whose total marks are below the class average
        - Total marks of each listed student
        - Total number of students below the class average

    The class average is calculated using the total marks of all students.
    Only students with total marks strictly below the class average are displayed.
    """
    
    # Total marks of each student.
    students_total = marks.sum(axis=1)

    # Average total marks of the class.
    average_total = students_total.mean()
    
    # checking below average students.
    below_average_students = students_total < average_total

    # Filter the below average students.
    indices = np.where(below_average_students)[0]

    print("\n========== STUDENTS BELOW AVERAGE ==========\n")

    print(f"Class Average Total : {average_total:.2f}\n")

    for index in indices:
        print(f"{names[index]:<10} : {students_total[index]}")
    
    print(f"Total Students : {indices.size}")

def show_students_with_full_marks(
        names: np.ndarray,
        subjects: np.ndarray,
        marks: np.ndarray
) -> None:
    """
    Display students who scored full marks in one or more subjects.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Student names who achieved full marks
        - Subjects in which they scored full marks
        - Marks obtained in those subjects
        - Total number of students with at least one full score

    A student is considered a full-mark student if they score
    100 marks in at least one subject.
    """
    
    # Full marks = 100
    FULL_MARKS = 100

    # Counter for students with at least one full mark
    total_students = 0

    print("\n========== STUDENTS WITH FULL MARKS ==========\n")

    # Loop through every student
    for i in range(names.shape[0]):

        # Marks of the current student
        student_marks = marks[i]
        
        # Check whether the student has any full marks
        if np.any(student_marks == FULL_MARKS):

            total_students += 1

            print(f"{names[i]}")
            print("-" * 15)

            # Find all subjects with full marks
            subject_indices = np.where(student_marks == FULL_MARKS)[0]

            for index in subject_indices:
                print(f"{subjects[index]:<10} : {FULL_MARKS}") 
        
            print()

    if total_students == 0:
        print("No student scored full marks.")    

    print(f"Total Students : {total_students}")

def show_failed_subjects(
    names: np.ndarray,
    subjects: np.ndarray,
    marks: np.ndarray
) -> None:
    """
    Display students who failed in one or more subjects.

    Parameters:
        names (numpy.ndarray):
            A 1D NumPy array containing the names of all students.

        subjects (numpy.ndarray):
            A 1D NumPy array containing the subject names.

        marks (numpy.ndarray):
            A 2D NumPy array containing the marks of all students.

    Displays:
        - Student names who failed in any subject
        - Subject names where they failed
        - Marks obtained in failed subjects
        - Total number of students who failed

    A student is considered failed if their marks are below
    the passing marks in at least one subject.
    """

    # Passing_marks = 40
    PASSING_MARKS = 40

    # Counter for students who failed in at least one subject.
    failed_students_count = 0

    print("\n========== FAILED SUBJECTS ==========\n")

    # Loop through every student
    for i in range(names.shape[0]):

        # Marks of the current student
        student_marks = marks[i]

        # Check whether the student failed in any subject. 
        if np.any(student_marks < PASSING_MARKS):

            failed_students_count += 1

            print(f"{names[i]}")
            print("-" * 15)

            # Find the subjects student get failed
            subject_indices = np.where(student_marks < PASSING_MARKS)[0]

            for index in subject_indices:
                print(f"{subjects[index]:<10} : {student_marks[index]}")
            
            print()
    
    if failed_students_count == 0:
        print("No student failed in any subject.")

    print(f"Total Failed Students : {failed_students_count}")

def generate_student_report(
        names: np.ndarray,
        roll_numbers: np.ndarray,
        subjects: np.ndarray,
        marks: np.ndarray,
        student_name: str
) -> None:
    """
    Generate a complete report card for a student.

    Parameters:
        names (numpy.ndarray):
            Array containing student names.

        roll_numbers (numpy.ndarray):
            Array containing student roll numbers.

        subjects (numpy.ndarray):
            Array containing subject names.

        marks (numpy.ndarray):
            2D array containing student marks.

        student_name (str):
            Name of the student whose report is generated.

    Displays:
        - Student name
        - Roll number
        - Subject-wise marks
        - Total marks
        - Percentage
        - Grade
        - Rank
        - Pass/Fail status
    """
    
    PASS_MARKS = 40

    # Checking student exist
    if student_name not in names:
        print("Student not found.")
        return
    
    # Find student index
    student_index = np.where(names == student_name)[0][0]

    # Student marks
    student_marks = marks[student_index]

    # Calculate total and percentage
    total_marks = np.sum(student_marks)

    max_marks = subjects.size * 100

    percentage = (total_marks / max_marks) * 100

    # Grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    
    # Pass/Fail status
    if np.all(student_marks >= PASS_MARKS):
        status = "PASS"
    else:
        status = "FAIL"

    # Calculate rank
    student_total = np.sum(marks, axis=1)

    total_marks = student_total[student_index]

    rank = np.sum(student_total > total_marks) + 1

    # Display report

    print("\n========== STUDENT REPORT ==========")

    print("-" * 40)

    print(f"Name        : {names[student_index]}")
    print(f"Roll No     : {roll_numbers[student_index]}")

    print("-" * 40)

    for index  in range(subjects.size):
        print(
            f"{subjects[index]:<12}: {student_marks[index]}"
        )
    
    print("-" * 40)

    print(f"Total       : {total_marks} / {max_marks}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Rank        : {rank}")
    print(f"Status      : {status}")

    print("-" * 40)

if __name__ == "__main__":
    main()