"""
Analyzer Engine — Data Adapter for Student Marks Analyzer GUI

This module wraps the NumPy-based analysis logic into functions
that return structured Python dictionaries/lists instead of printing
to the console. The original main.py remains completely untouched.

Author: Jitesh Nepalia
"""

import numpy as np


class StudentMarksEngine:
    """
    Core engine that holds student data and provides
    all analysis operations as pure-data return functions.
    """

    PASS_MARKS = 40
    FULL_MARKS = 100

    def __init__(self):
        # Subject names
        self.subjects = np.array([
            "Maths", "Physics", "Chemistry", "English", "Computer"
        ])

        # Admin credentials
        self.admin_username = "admin"
        self.admin_password = "admin@123"

        # Student roll numbers
        self.roll_numbers = np.arange(101, 111)

        # Student names
        self.names = np.array([
            "Jitesh", "Aman", "Priya", "Rahul", "Anjali",
            "Arjun", "Sakshi", "Karan", "Neha", "Riya"
        ])

        # Marks matrix: rows = students, columns = subjects
        # Subject order: Maths, Physics, Chemistry, English, Computer
        self.marks = np.array([
            [95, 91, 88, 93, 97],   # Jitesh
            [82, 76, 85, 80, 79],   # Aman
            [91, 94, 89, 95, 92],   # Priya
            [68, 72, 70, 66, 74],   # Rahul
            [98, 96, 97, 99, 100],  # Anjali
            [78, 81, 76, 83, 80],   # Arjun
            [87, 89, 91, 88, 90],   # Sakshi
            [73, 69, 75, 71, 72],   # Karan
            [64, 67, 65, 70, 68],   # Neha
            [93, 90, 94, 92, 95]    # Riya
        ])

    # -------------------- Authentication -------------------- #

    def authenticate_admin(self, username: str, password: str) -> bool:
        """Verify admin credentials."""
        return (
            username == self.admin_username
            and password == self.admin_password
        )

    def authenticate_student(
        self, name: str, roll_number: int
    ) -> tuple[int, str, int] | None:
        """
        Verify student credentials.

        Returns:
            (index, name, roll_number) on success, None on failure.
        """
        capitalized = name.strip().capitalize()

        if capitalized not in self.names:
            return None

        index = int(np.where(self.names == capitalized)[0][0])

        if roll_number != self.roll_numbers[index]:
            return None

        return (index, self.names[index], int(self.roll_numbers[index]))

    # -------------------- Data Retrieval -------------------- #

    def get_all_student_names(self) -> list[str]:
        """Return list of all student names."""
        return self.names.tolist()

    def get_all_subjects(self) -> list[str]:
        """Return list of all subject names."""
        return self.subjects.tolist()

    def get_student_data(self) -> dict:
        """Return all student data as a structured dict."""
        rows = []
        for i in range(self.names.size):
            row = {
                "roll_number": int(self.roll_numbers[i]),
                "name": self.names[i],
            }
            for j, subj in enumerate(self.subjects):
                row[subj] = int(self.marks[i, j])
            rows.append(row)
        return {"students": rows, "subjects": self.subjects.tolist()}

    def get_dataset_info(self) -> dict:
        """Return metadata about the marks array."""
        return {
            "shape": self.marks.shape,
            "ndim": int(self.marks.ndim),
            "dtype": str(self.marks.dtype),
            "size": int(self.marks.size),
        }

    def get_dataset_overview(self) -> dict:
        """Return high-level overview of the dataset."""
        return {
            "total_students": int(self.names.size),
            "total_subjects": int(self.marks.shape[1]),
            "first_student": {
                "name": self.names[0],
                "marks": self.marks[0].tolist(),
            },
            "last_student": {
                "name": self.names[-1],
                "marks": self.marks[-1].tolist(),
            },
        }

    # -------------------- Marks -------------------- #

    def get_student_marks(self, student_name: str) -> dict | None:
        """Return marks of a specific student."""
        cap = student_name.strip().capitalize()
        if cap not in self.names:
            return None
        idx = int(np.where(self.names == cap)[0][0])
        return {
            "name": self.names[idx],
            "marks": {
                subj: int(self.marks[idx, j])
                for j, subj in enumerate(self.subjects)
            },
        }

    def get_subject_marks(self, subject_name: str) -> dict | None:
        """Return marks of all students for a subject."""
        cap = subject_name.strip().capitalize()
        if cap not in self.subjects:
            return None
        j = int(np.where(self.subjects == cap)[0][0])
        return {
            "subject": self.subjects[j],
            "students": [
                {"name": self.names[i], "marks": int(self.marks[i, j])}
                for i in range(self.names.size)
            ],
        }

    def get_student_subject_mark(
        self, student_name: str, subject_name: str
    ) -> dict | None:
        """Return mark of a specific student in a specific subject."""
        s_cap = student_name.strip().capitalize()
        sub_cap = subject_name.strip().capitalize()
        if s_cap not in self.names or sub_cap not in self.subjects:
            return None
        si = int(np.where(self.names == s_cap)[0][0])
        sj = int(np.where(self.subjects == sub_cap)[0][0])
        return {
            "student": self.names[si],
            "subject": self.subjects[sj],
            "marks": int(self.marks[si, sj]),
        }

    def get_students_range(
        self, start_name: str, end_name: str
    ) -> dict | None:
        """Return marks of students in a name range."""
        s = start_name.strip().capitalize()
        e = end_name.strip().capitalize()
        if s not in self.names or e not in self.names:
            return None
        si = int(np.where(self.names == s)[0][0])
        ei = int(np.where(self.names == e)[0][0])
        if si > ei:
            return None
        sliced_names = self.names[si: ei + 1]
        sliced_marks = self.marks[si: ei + 1]
        students = []
        for i in range(sliced_names.size):
            students.append({
                "name": sliced_names[i],
                "marks": {
                    subj: int(sliced_marks[i, j])
                    for j, subj in enumerate(self.subjects)
                },
            })
        return {"students": students}

    def get_subject_range(
        self, start_subject: str, end_subject: str
    ) -> dict | None:
        """Return marks of all students for a range of subjects."""
        s = start_subject.strip().capitalize()
        e = end_subject.strip().capitalize()
        if s not in self.subjects or e not in self.subjects:
            return None
        si = int(np.where(self.subjects == s)[0][0])
        ei = int(np.where(self.subjects == e)[0][0])
        if si > ei:
            return None
        sel_subjects = self.subjects[si: ei + 1].tolist()
        sel_marks = self.marks[:, si: ei + 1]
        students = []
        for i in range(self.names.size):
            students.append({
                "name": self.names[i],
                "marks": {
                    sel_subjects[j]: int(sel_marks[i, j])
                    for j in range(len(sel_subjects))
                },
            })
        return {"subjects": sel_subjects, "students": students}

    def get_student_subject_range(
        self,
        start_subject: str, end_subject: str,
        start_student: str, end_student: str,
    ) -> dict | None:
        """Return marks for a range of students × subjects."""
        ss = start_subject.strip().capitalize()
        es = end_subject.strip().capitalize()
        sst = start_student.strip().capitalize()
        est = end_student.strip().capitalize()

        if ss not in self.subjects or es not in self.subjects:
            return None
        if sst not in self.names or est not in self.names:
            return None

        ssi = int(np.where(self.subjects == ss)[0][0])
        esi = int(np.where(self.subjects == es)[0][0])
        ssti = int(np.where(self.names == sst)[0][0])
        esti = int(np.where(self.names == est)[0][0])

        if ssi > esi or ssti > esti:
            return None

        sel_subjects = self.subjects[ssi: esi + 1].tolist()
        sel_names = self.names[ssti: esti + 1]
        sel_marks = self.marks[ssti: esti + 1, ssi: esi + 1]

        students = []
        for i in range(sel_names.size):
            students.append({
                "name": sel_names[i],
                "marks": {
                    sel_subjects[j]: int(sel_marks[i, j])
                    for j in range(len(sel_subjects))
                },
            })
        return {"subjects": sel_subjects, "students": students}

    # -------------------- Statistics -------------------- #

    def get_student_statistics(self, student_name: str) -> dict | None:
        """Return statistical info for a specific student."""
        cap = student_name.strip().capitalize()
        if cap not in self.names:
            return None
        idx = int(np.where(self.names == cap)[0][0])
        sm = self.marks[idx]
        return {
            "name": self.names[idx],
            "marks": {
                subj: int(sm[j])
                for j, subj in enumerate(self.subjects)
            },
            "total": int(np.sum(sm)),
            "average": round(float(np.mean(sm)), 2),
            "highest": int(np.max(sm)),
            "lowest": int(np.min(sm)),
            "median": float(np.median(sm)),
            "std_dev": round(float(np.std(sm)), 2),
            "variance": round(float(np.var(sm)), 2),
        }

    def get_subject_statistics(self, subject_name: str) -> dict | None:
        """Return statistical info for a specific subject."""
        cap = subject_name.strip().capitalize()
        if cap not in self.subjects:
            return None
        j = int(np.where(self.subjects == cap)[0][0])
        sm = self.marks[:, j]
        return {
            "subject": self.subjects[j],
            "marks": {
                self.names[i]: int(sm[i])
                for i in range(self.names.size)
            },
            "total": int(np.sum(sm)),
            "average": round(float(np.mean(sm)), 2),
            "highest": int(np.max(sm)),
            "lowest": int(np.min(sm)),
            "median": round(float(np.median(sm)), 2),
            "std_dev": round(float(np.std(sm)), 2),
            "variance": round(float(np.var(sm)), 2),
        }

    def get_class_statistics(self) -> dict:
        """Return overall class statistics."""
        return {
            "total_students": int(self.marks.shape[0]),
            "total_subjects": int(self.marks.shape[1]),
            "overall_average": round(float(np.mean(self.marks)), 2),
            "highest_mark": int(np.max(self.marks)),
            "lowest_mark": int(np.min(self.marks)),
            "median": round(float(np.median(self.marks)), 2),
            "std_dev": round(float(np.std(self.marks)), 2),
            "variance": round(float(np.var(self.marks)), 2),
        }

    # -------------------- Rankings -------------------- #

    def get_student_ranking(self) -> list[dict]:
        """Return all students ranked by total marks descending."""
        totals = np.sum(self.marks, axis=1)
        ranking = np.argsort(totals)[::-1]
        return [
            {
                "rank": rank + 1,
                "name": self.names[idx],
                "total": int(totals[idx]),
                "percentage": round(
                    float(totals[idx]) / (self.subjects.size * 100) * 100, 2
                ),
            }
            for rank, idx in enumerate(ranking)
        ]

    def get_topper_and_lowest(self) -> dict:
        """Return the topper and lowest-scoring student."""
        totals = np.sum(self.marks, axis=1)
        top_idx = int(np.argmax(totals))
        low_idx = int(np.argmin(totals))
        return {
            "topper": {
                "name": self.names[top_idx],
                "total": int(totals[top_idx]),
            },
            "lowest": {
                "name": self.names[low_idx],
                "total": int(totals[low_idx]),
            },
        }

    def get_subject_toppers(self) -> list[dict]:
        """Return the topper of each subject."""
        topper_indices = np.argmax(self.marks, axis=0)
        topper_marks = np.max(self.marks, axis=0)
        return [
            {
                "subject": self.subjects[j],
                "student": self.names[topper_indices[j]],
                "marks": int(topper_marks[j]),
            }
            for j in range(self.subjects.size)
        ]

    # -------------------- Pass/Fail Analysis -------------------- #

    def get_passed_students(self) -> dict:
        """Return students who passed all subjects (≥40 in each)."""
        passed = np.all(self.marks >= self.PASS_MARKS, axis=1)
        indices = np.where(passed)[0]
        return {
            "students": [self.names[i] for i in indices],
            "total": int(np.sum(passed)),
        }

    def get_failed_students(self) -> dict:
        """Return students who failed in at least one subject (<40)."""
        failed = np.any(self.marks < self.PASS_MARKS, axis=1)
        indices = np.where(failed)[0]
        return {
            "students": [self.names[i] for i in indices],
            "total": int(np.sum(failed)),
        }

    def get_above_average(self) -> dict:
        """Return students whose total is above class average."""
        totals = self.marks.sum(axis=1)
        avg = totals.mean()
        indices = np.where(totals > avg)[0]
        return {
            "class_average": round(float(avg), 2),
            "students": [
                {"name": self.names[i], "total": int(totals[i])}
                for i in indices
            ],
            "total_count": int(indices.size),
        }

    def get_below_average(self) -> dict:
        """Return students whose total is below class average."""
        totals = self.marks.sum(axis=1)
        avg = totals.mean()
        indices = np.where(totals < avg)[0]
        return {
            "class_average": round(float(avg), 2),
            "students": [
                {"name": self.names[i], "total": int(totals[i])}
                for i in indices
            ],
            "total_count": int(indices.size),
        }

    def get_full_marks_students(self) -> dict:
        """Return students who scored 100 in any subject."""
        result = []
        for i in range(self.names.size):
            sm = self.marks[i]
            if np.any(sm == self.FULL_MARKS):
                subj_indices = np.where(sm == self.FULL_MARKS)[0]
                result.append({
                    "name": self.names[i],
                    "subjects": [
                        {
                            "subject": self.subjects[j],
                            "marks": int(self.FULL_MARKS),
                        }
                        for j in subj_indices
                    ],
                })
        return {"students": result, "total": len(result)}

    def get_failed_subjects(self) -> dict:
        """Return students with subjects they failed (<40)."""
        result = []
        for i in range(self.names.size):
            sm = self.marks[i]
            if np.any(sm < self.PASS_MARKS):
                subj_indices = np.where(sm < self.PASS_MARKS)[0]
                result.append({
                    "name": self.names[i],
                    "subjects": [
                        {
                            "subject": self.subjects[j],
                            "marks": int(sm[j]),
                        }
                        for j in subj_indices
                    ],
                })
        return {"students": result, "total": len(result)}

    # -------------------- Report -------------------- #

    def generate_report(self, student_name: str) -> dict | None:
        """Generate a full report card for a student."""
        cap = student_name.strip().capitalize()
        if cap not in self.names:
            return None

        idx = int(np.where(self.names == cap)[0][0])
        sm = self.marks[idx]
        total = int(np.sum(sm))
        max_marks = int(self.subjects.size * 100)
        percentage = round((total / max_marks) * 100, 2)

        # Grade
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

        # Pass / Fail
        status = "PASS" if np.all(sm >= self.PASS_MARKS) else "FAIL"

        # Rank
        all_totals = np.sum(self.marks, axis=1)
        rank = int(np.sum(all_totals > total) + 1)

        return {
            "name": self.names[idx],
            "roll_number": int(self.roll_numbers[idx]),
            "subjects": {
                subj: int(sm[j])
                for j, subj in enumerate(self.subjects)
            },
            "total": total,
            "max_marks": max_marks,
            "percentage": percentage,
            "grade": grade,
            "rank": rank,
            "status": status,
        }
