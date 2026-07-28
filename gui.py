"""
Student Marks Analyzer — Professional GUI

A modern, dark-themed desktop application built with CustomTkinter
that wraps the existing NumPy-based student analysis backend.

Author: Jitesh Nepalia
Version: 2.0.0 (GUI Edition)
"""

import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from datetime import datetime
from analyzer_engine import StudentMarksEngine

# ──────────────────────── Theme Configuration ──────────────────────── #

COLORS = {
    "bg_dark": "#0f0f1a",
    "bg_card": "#1a1a2e",
    "bg_card_hover": "#222240",
    "bg_sidebar": "#12122a",
    "bg_input": "#16213e",
    "border": "#2a2a4a",
    "primary": "#6c5ce7",
    "primary_hover": "#7f70f0",
    "primary_light": "#a29bfe",
    "secondary": "#00d2ff",
    "accent_cyan": "#00d2ff",
    "success": "#00e676",
    "warning": "#ffc107",
    "danger": "#ff5252",
    "text_primary": "#e8e8e8",
    "text_secondary": "#8b8b9e",
    "text_muted": "#5a5a78",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "bronze": "#CD7F32",
    "sidebar_active": "#6c5ce7",
    "sidebar_hover": "#1e1e3a",
    "table_row_even": "#16162e",
    "table_row_odd": "#1a1a34",
    "table_header": "#222244",
}

FONT_FAMILY = "Segoe UI"

# ──────────────────────── Main Application ──────────────────────── #


class StudentMarksApp(ctk.CTk):
    """Root application window."""

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Student Marks Analyzer")
        self.geometry("1280x780")
        self.minsize(1100, 700)
        self.configure(fg_color=COLORS["bg_dark"])

        # Center window on screen
        self.update_idletasks()
        w, h = 1280, 780
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

        # Engine
        self.engine = StudentMarksEngine()

        # Session state
        self.current_role = None       # "admin" or "student"
        self.logged_in_student = None  # student name if student role

        # Container that fills the whole window
        self.container = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"])
        self.container.pack(fill="both", expand=True)

        self.show_login()

    # ───────────── Frame Switching ───────────── #

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login(self):
        self.current_role = None
        self.logged_in_student = None
        self.clear_container()
        LoginFrame(self.container, self)

    def show_admin_dashboard(self):
        self.current_role = "admin"
        self.clear_container()
        DashboardFrame(self.container, self, role="admin")

    def show_student_dashboard(self, student_name: str):
        self.current_role = "student"
        self.logged_in_student = student_name
        self.clear_container()
        DashboardFrame(self.container, self, role="student")


# ──────────────────────── Login Frame ──────────────────────── #


class LoginFrame(ctk.CTkFrame):
    """Login screen with role selection and authentication."""

    def __init__(self, parent, app: StudentMarksApp):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self.pack(fill="both", expand=True)
        self.app = app

        # Background gradient simulation — layered frames
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Centered card
        card = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_card"],
            corner_radius=20,
            border_width=1,
            border_color=COLORS["border"],
            width=440,
            height=560,
        )
        card.grid(row=0, column=0)
        card.grid_propagate(False)

        # ── Logo / Title ──
        logo_frame = ctk.CTkFrame(card, fg_color="transparent")
        logo_frame.pack(pady=(35, 5))

        ctk.CTkLabel(
            logo_frame,
            text="📊",
            font=(FONT_FAMILY, 42),
        ).pack()

        ctk.CTkLabel(
            card,
            text="Student Marks Analyzer",
            font=(FONT_FAMILY, 22, "bold"),
            text_color=COLORS["text_primary"],
        ).pack(pady=(2, 0))

        ctk.CTkLabel(
            card,
            text="Powered by NumPy",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_muted"],
        ).pack(pady=(2, 20))

        # ── Role selector ──
        role_frame = ctk.CTkFrame(card, fg_color="transparent")
        role_frame.pack(pady=(0, 15))

        self.role_var = ctk.StringVar(value="student")

        self.btn_student = ctk.CTkButton(
            role_frame,
            text="🎓  Student",
            font=(FONT_FAMILY, 14, "bold"),
            width=180,
            height=42,
            corner_radius=10,
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=lambda: self._select_role("student"),
        )
        self.btn_student.grid(row=0, column=0, padx=5)

        self.btn_admin = ctk.CTkButton(
            role_frame,
            text="🔑  Admin",
            font=(FONT_FAMILY, 14, "bold"),
            width=180,
            height=42,
            corner_radius=10,
            fg_color=COLORS["bg_input"],
            hover_color=COLORS["sidebar_hover"],
            command=lambda: self._select_role("admin"),
        )
        self.btn_admin.grid(row=0, column=1, padx=5)

        # ── Input fields ──
        input_frame = ctk.CTkFrame(card, fg_color="transparent")
        input_frame.pack(padx=40, fill="x")

        # Student name / Admin username
        self.label_user = ctk.CTkLabel(
            input_frame,
            text="Student Name",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_secondary"],
            anchor="w",
        )
        self.label_user.pack(fill="x", pady=(10, 3))

        self.entry_user = ctk.CTkEntry(
            input_frame,
            height=42,
            corner_radius=10,
            font=(FONT_FAMILY, 14),
            fg_color=COLORS["bg_input"],
            border_color=COLORS["border"],
            placeholder_text="Enter your name",
        )
        self.entry_user.pack(fill="x")

        # Roll number / Password
        self.label_pass = ctk.CTkLabel(
            input_frame,
            text="Roll Number",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_secondary"],
            anchor="w",
        )
        self.label_pass.pack(fill="x", pady=(15, 3))

        self.entry_pass = ctk.CTkEntry(
            input_frame,
            height=42,
            corner_radius=10,
            font=(FONT_FAMILY, 14),
            fg_color=COLORS["bg_input"],
            border_color=COLORS["border"],
            placeholder_text="Enter roll number",
        )
        self.entry_pass.pack(fill="x")

        # Bind Enter key
        self.entry_pass.bind("<Return>", lambda e: self._login())

        # ── Error label ──
        self.error_label = ctk.CTkLabel(
            card,
            text="",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["danger"],
        )
        self.error_label.pack(pady=(10, 0))

        # ── Login button ──
        self.login_btn = ctk.CTkButton(
            card,
            text="Sign In →",
            font=(FONT_FAMILY, 15, "bold"),
            width=360,
            height=46,
            corner_radius=12,
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=self._login,
        )
        self.login_btn.pack(pady=(5, 10))

        # ── Footer ──
        ctk.CTkLabel(
            card,
            text="v2.0  •  By Jitesh Nepalia",
            font=(FONT_FAMILY, 11),
            text_color=COLORS["text_muted"],
        ).pack(pady=(5, 15))

    def _select_role(self, role: str):
        self.role_var.set(role)
        self.error_label.configure(text="")

        if role == "student":
            self.btn_student.configure(fg_color=COLORS["primary"])
            self.btn_admin.configure(fg_color=COLORS["bg_input"])
            self.label_user.configure(text="Student Name")
            self.entry_user.configure(placeholder_text="Enter your name")
            self.label_pass.configure(text="Roll Number")
            self.entry_pass.configure(
                placeholder_text="Enter roll number", show=""
            )
        else:
            self.btn_admin.configure(fg_color=COLORS["primary"])
            self.btn_student.configure(fg_color=COLORS["bg_input"])
            self.label_user.configure(text="Username")
            self.entry_user.configure(placeholder_text="Enter admin username")
            self.label_pass.configure(text="Password")
            self.entry_pass.configure(
                placeholder_text="Enter admin password", show="•"
            )

    def _login(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pass.get().strip()

        if not user or not pwd:
            self.error_label.configure(text="Please fill in all fields.")
            return

        if self.role_var.get() == "admin":
            if self.app.engine.authenticate_admin(user, pwd):
                self.app.show_admin_dashboard()
            else:
                self.error_label.configure(text="Invalid admin credentials.")
        else:
            try:
                roll = int(pwd)
            except ValueError:
                self.error_label.configure(
                    text="Roll number must be a number."
                )
                return
            result = self.app.engine.authenticate_student(user, roll)
            if result:
                _, name, _ = result
                self.app.show_student_dashboard(name)
            else:
                self.error_label.configure(
                    text="Invalid student name or roll number."
                )


# ──────────────────────── Dashboard Frame ──────────────────────── #

# Sidebar menu definitions
ADMIN_MENU = [
    ("section", "OVERVIEW"),
    ("item", "📊", "Dashboard", "dashboard"),
    ("item", "📋", "Student Data", "student_data"),
    ("item", "🗂️", "Dataset Info", "dataset_info"),
    ("item", "🔍", "Explore Dataset", "explore_dataset"),
    ("section", "MARKS"),
    ("item", "📝", "Student Marks", "student_marks"),
    ("item", "📚", "Subject Marks", "subject_marks"),
    ("item", "🎯", "Student Subject Mark", "student_subject_mark"),
    ("item", "👥", "Students Range", "students_range"),
    ("item", "📖", "Subject Range", "subject_range"),
    ("item", "🔀", "Student Subject Range", "student_subject_range"),
    ("section", "STATISTICS"),
    ("item", "📈", "Student Statistics", "student_statistics"),
    ("item", "📉", "Subject Statistics", "subject_statistics"),
    ("item", "🏫", "Class Statistics", "class_statistics"),
    ("section", "RANKINGS"),
    ("item", "🏆", "Student Ranking", "student_ranking"),
    ("item", "⭐", "Topper & Lowest", "topper_lowest"),
    ("item", "🥇", "Subject Toppers", "subject_toppers"),
    ("section", "ANALYSIS"),
    ("item", "✅", "Passed Students", "passed_students"),
    ("item", "❌", "Failed Students", "failed_students"),
    ("item", "📈", "Above Average", "above_average"),
    ("item", "📉", "Below Average", "below_average"),
    ("item", "💯", "Full Marks", "full_marks"),
    ("item", "⚠️", "Failed Subjects", "failed_subjects"),
    ("section", "REPORT"),
    ("item", "📄", "Generate Report", "generate_report"),
]

STUDENT_MENU = [
    ("section", "MY DATA"),
    ("item", "📊", "Dashboard", "dashboard"),
    ("item", "📝", "My Marks", "student_marks"),
    ("item", "🎯", "My Subject Mark", "student_subject_mark"),
    ("item", "📈", "My Statistics", "student_statistics"),
    ("item", "🏆", "My Ranking", "student_ranking"),
    ("item", "📄", "My Report", "generate_report"),
]


class DashboardFrame(ctk.CTkFrame):
    """Main dashboard with sidebar and content area."""

    def __init__(self, parent, app: StudentMarksApp, role: str):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self.pack(fill="both", expand=True)
        self.app = app
        self.role = role
        self.active_key = None
        self.sidebar_buttons = {}

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ── Sidebar ──
        self._build_sidebar()

        # ── Content Area ──
        self.content_wrapper = ctk.CTkFrame(
            self, fg_color=COLORS["bg_dark"]
        )
        self.content_wrapper.grid(row=0, column=1, sticky="nsew")
        self.content_wrapper.grid_rowconfigure(1, weight=1)
        self.content_wrapper.grid_columnconfigure(0, weight=1)

        # Top bar
        self._build_top_bar()

        # Content scroll area
        self.content_area = ctk.CTkScrollableFrame(
            self.content_wrapper,
            fg_color=COLORS["bg_dark"],
            scrollbar_button_color=COLORS["border"],
            scrollbar_button_hover_color=COLORS["primary"],
        )
        self.content_area.grid(row=1, column=0, sticky="nsew", padx=20, pady=(5, 15))

        # Show dashboard by default
        self._navigate("dashboard")

    # ────── Sidebar ────── #

    def _build_sidebar(self):
        sidebar = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_sidebar"],
            width=250,
            corner_radius=0,
        )
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)

        # Sidebar header
        header = ctk.CTkFrame(sidebar, fg_color="transparent", height=70)
        header.pack(fill="x", pady=(10, 5), padx=15)
        header.pack_propagate(False)

        ctk.CTkLabel(
            header,
            text="📊 Marks Analyzer",
            font=(FONT_FAMILY, 16, "bold"),
            text_color=COLORS["text_primary"],
            anchor="w",
        ).pack(fill="x", pady=(12, 0))

        role_text = "Admin Panel" if self.role == "admin" else f"Student: {self.app.logged_in_student}"
        ctk.CTkLabel(
            header,
            text=role_text,
            font=(FONT_FAMILY, 11),
            text_color=COLORS["primary_light"],
            anchor="w",
        ).pack(fill="x")

        # Separator
        ctk.CTkFrame(
            sidebar, fg_color=COLORS["border"], height=1
        ).pack(fill="x", padx=15, pady=5)

        # Scrollable menu area
        menu_scroll = ctk.CTkScrollableFrame(
            sidebar,
            fg_color="transparent",
            scrollbar_button_color=COLORS["border"],
            scrollbar_button_hover_color=COLORS["primary"],
        )
        menu_scroll.pack(fill="both", expand=True, padx=5)

        menu_items = ADMIN_MENU if self.role == "admin" else STUDENT_MENU

        for entry in menu_items:
            if entry[0] == "section":
                ctk.CTkLabel(
                    menu_scroll,
                    text=entry[1],
                    font=(FONT_FAMILY, 10, "bold"),
                    text_color=COLORS["text_muted"],
                    anchor="w",
                ).pack(fill="x", padx=15, pady=(12, 4))
            else:
                _, icon, label, key = entry
                btn = ctk.CTkButton(
                    menu_scroll,
                    text=f"  {icon}  {label}",
                    font=(FONT_FAMILY, 13),
                    anchor="w",
                    height=38,
                    corner_radius=8,
                    fg_color="transparent",
                    text_color=COLORS["text_secondary"],
                    hover_color=COLORS["sidebar_hover"],
                    command=lambda k=key: self._navigate(k),
                )
                btn.pack(fill="x", padx=8, pady=1)
                self.sidebar_buttons[key] = btn

        # Logout button at bottom
        bottom = ctk.CTkFrame(sidebar, fg_color="transparent")
        bottom.pack(fill="x", side="bottom", padx=15, pady=15)

        ctk.CTkFrame(
            bottom, fg_color=COLORS["border"], height=1
        ).pack(fill="x", pady=(0, 10))

        ctk.CTkButton(
            bottom,
            text="🚪  Logout",
            font=(FONT_FAMILY, 13, "bold"),
            height=40,
            corner_radius=10,
            fg_color=COLORS["danger"],
            hover_color="#ff7070",
            command=self.app.show_login,
        ).pack(fill="x")

    # ────── Top Bar ────── #

    def _build_top_bar(self):
        bar = ctk.CTkFrame(
            self.content_wrapper,
            fg_color=COLORS["bg_card"],
            height=55,
            corner_radius=12,
        )
        bar.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 5))
        bar.grid_propagate(False)
        bar.grid_columnconfigure(1, weight=1)

        self.page_title_label = ctk.CTkLabel(
            bar,
            text="Dashboard",
            font=(FONT_FAMILY, 17, "bold"),
            text_color=COLORS["text_primary"],
        )
        self.page_title_label.grid(row=0, column=0, padx=20, pady=12)

        # Time
        self.time_label = ctk.CTkLabel(
            bar,
            text="",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_muted"],
        )
        self.time_label.grid(row=0, column=2, padx=20)
        self._update_time()

    def _update_time(self):
        now = datetime.now().strftime("%I:%M %p  •  %d %b %Y")
        self.time_label.configure(text=now)
        self.after(30000, self._update_time)

    # ────── Navigation ────── #

    def _navigate(self, key: str):
        # Update active sidebar button
        for k, btn in self.sidebar_buttons.items():
            if k == key:
                btn.configure(
                    fg_color=COLORS["sidebar_active"],
                    text_color=COLORS["text_primary"],
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=COLORS["text_secondary"],
                )
        self.active_key = key

        # Clear content
        for w in self.content_area.winfo_children():
            w.destroy()

        # Route
        page_map = {
            "dashboard": self._page_dashboard,
            "student_data": self._page_student_data,
            "dataset_info": self._page_dataset_info,
            "explore_dataset": self._page_explore_dataset,
            "student_marks": self._page_student_marks,
            "subject_marks": self._page_subject_marks,
            "student_subject_mark": self._page_student_subject_mark,
            "students_range": self._page_students_range,
            "subject_range": self._page_subject_range,
            "student_subject_range": self._page_student_subject_range,
            "student_statistics": self._page_student_statistics,
            "subject_statistics": self._page_subject_statistics,
            "class_statistics": self._page_class_statistics,
            "student_ranking": self._page_student_ranking,
            "topper_lowest": self._page_topper_lowest,
            "subject_toppers": self._page_subject_toppers,
            "passed_students": self._page_passed_students,
            "failed_students": self._page_failed_students,
            "above_average": self._page_above_average,
            "below_average": self._page_below_average,
            "full_marks": self._page_full_marks,
            "failed_subjects": self._page_failed_subjects,
            "generate_report": self._page_generate_report,
        }

        handler = page_map.get(key)
        if handler:
            # Update title
            title_map = {
                "dashboard": "Dashboard",
                "student_data": "Student Data",
                "dataset_info": "Dataset Information",
                "explore_dataset": "Explore Dataset",
                "student_marks": "Student Marks",
                "subject_marks": "Subject Marks",
                "student_subject_mark": "Student Subject Mark",
                "students_range": "Students Range",
                "subject_range": "Subject Range",
                "student_subject_range": "Student & Subject Range",
                "student_statistics": "Student Statistics",
                "subject_statistics": "Subject Statistics",
                "class_statistics": "Class Statistics",
                "student_ranking": "Student Ranking",
                "topper_lowest": "Topper & Lowest Student",
                "subject_toppers": "Subject Toppers",
                "passed_students": "Passed Students",
                "failed_students": "Failed Students",
                "above_average": "Students Above Average",
                "below_average": "Students Below Average",
                "full_marks": "Students With Full Marks",
                "failed_subjects": "Failed Subjects",
                "generate_report": "Student Report",
            }
            self.page_title_label.configure(
                text=title_map.get(key, "Dashboard")
            )
            handler()

    # ══════════════════════ Helper Builders ══════════════════════ #

    def _make_card(self, parent, **kwargs) -> ctk.CTkFrame:
        """Create a styled card frame."""
        return ctk.CTkFrame(
            parent,
            fg_color=COLORS["bg_card"],
            corner_radius=14,
            border_width=1,
            border_color=COLORS["border"],
            **kwargs,
        )

    def _make_stat_card(
        self, parent, icon: str, label: str, value, color=None
    ) -> ctk.CTkFrame:
        """Create a small stat card with icon, label, and large value."""
        card = self._make_card(parent)
        card.grid_columnconfigure(0, weight=1)

        top = ctk.CTkFrame(card, fg_color="transparent")
        top.pack(fill="x", padx=18, pady=(16, 4))

        ctk.CTkLabel(
            top,
            text=f"{icon}  {label}",
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_secondary"],
            anchor="w",
        ).pack(fill="x")

        ctk.CTkLabel(
            card,
            text=str(value),
            font=(FONT_FAMILY, 28, "bold"),
            text_color=color or COLORS["text_primary"],
            anchor="w",
        ).pack(padx=18, pady=(0, 16), fill="x")

        return card

    def _make_table(
        self, parent, columns: list[tuple[str, int]], rows: list[list],
        height: int = 12
    ) -> ttk.Treeview:
        """Create a styled treeview table."""
        style = ttk.Style()
        style.theme_use("default")

        style.configure(
            "Custom.Treeview",
            background=COLORS["bg_card"],
            foreground=COLORS["text_primary"],
            fieldbackground=COLORS["bg_card"],
            borderwidth=0,
            font=(FONT_FAMILY, 12),
            rowheight=36,
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=COLORS["table_header"],
            foreground=COLORS["primary_light"],
            font=(FONT_FAMILY, 12, "bold"),
            borderwidth=0,
            relief="flat",
        )
        style.map(
            "Custom.Treeview",
            background=[("selected", COLORS["primary"])],
            foreground=[("selected", "#ffffff")],
        )
        style.map(
            "Custom.Treeview.Heading",
            background=[
                ("active", COLORS["table_header"]),
            ],
        )
        style.layout("Custom.Treeview", [
            ("Custom.Treeview.treearea", {"sticky": "nswe"})
        ])

        col_ids = [c[0] for c in columns]
        tree = ttk.Treeview(
            parent,
            columns=col_ids,
            show="headings",
            height=height,
            style="Custom.Treeview",
        )

        for col_name, col_width in columns:
            tree.heading(col_name, text=col_name, anchor="center")
            tree.column(col_name, width=col_width, anchor="center", minwidth=60)

        # Tag alternating rows
        tree.tag_configure("even", background=COLORS["table_row_even"])
        tree.tag_configure("odd", background=COLORS["table_row_odd"])

        for i, row in enumerate(rows):
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", values=row, tags=(tag,))

        tree.pack(fill="both", expand=True, padx=2, pady=2)
        return tree

    def _make_dropdown(
        self, parent, label: str, values: list[str]
    ) -> ctk.CTkComboBox:
        """Create a labelled dropdown."""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=5)

        ctk.CTkLabel(
            frame,
            text=label,
            font=(FONT_FAMILY, 12),
            text_color=COLORS["text_secondary"],
            anchor="w",
        ).pack(fill="x")

        combo = ctk.CTkComboBox(
            frame,
            values=values,
            font=(FONT_FAMILY, 13),
            dropdown_font=(FONT_FAMILY, 13),
            height=38,
            corner_radius=10,
            fg_color=COLORS["bg_input"],
            border_color=COLORS["border"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"],
            dropdown_fg_color=COLORS["bg_card"],
            dropdown_hover_color=COLORS["sidebar_hover"],
            dropdown_text_color=COLORS["text_primary"],
            state="readonly",
        )
        combo.pack(fill="x", pady=(3, 0))
        if values:
            combo.set(values[0])
        return combo

    def _make_go_button(self, parent, command) -> ctk.CTkButton:
        """Create a styled action button."""
        btn = ctk.CTkButton(
            parent,
            text="Show Results →",
            font=(FONT_FAMILY, 14, "bold"),
            height=42,
            corner_radius=10,
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_hover"],
            command=command,
        )
        btn.pack(pady=(10, 5))
        return btn

    def _show_error(self, parent, msg: str):
        """Show an error label."""
        ctk.CTkLabel(
            parent,
            text=f"⚠️  {msg}",
            font=(FONT_FAMILY, 14),
            text_color=COLORS["danger"],
        ).pack(pady=20)

    def _get_grade_color(self, grade: str) -> str:
        """Return a color for the given grade."""
        return {
            "A+": COLORS["success"],
            "A": "#66ff99",
            "B": COLORS["secondary"],
            "C": COLORS["warning"],
            "D": "#ff9800",
            "F": COLORS["danger"],
        }.get(grade, COLORS["text_primary"])

    def _student_name_for_page(self) -> str | None:
        """For student role, return their own name."""
        if self.role == "student":
            return self.app.logged_in_student
        return None

    # ══════════════════════ Page Renderers ══════════════════════ #

    # ── Dashboard ── #

    def _page_dashboard(self):
        engine = self.app.engine

        if self.role == "admin":
            stats = engine.get_class_statistics()
            top = engine.get_topper_and_lowest()
            ranking = engine.get_student_ranking()

            # Stat cards row
            cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
            cards_frame.pack(fill="x", pady=(5, 10))
            for i in range(4):
                cards_frame.grid_columnconfigure(i, weight=1)

            c1 = self._make_stat_card(
                cards_frame, "🎓", "Total Students",
                stats["total_students"], COLORS["secondary"]
            )
            c1.grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

            c2 = self._make_stat_card(
                cards_frame, "📚", "Total Subjects",
                stats["total_subjects"], COLORS["primary_light"]
            )
            c2.grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

            c3 = self._make_stat_card(
                cards_frame, "📊", "Class Average",
                f"{stats['overall_average']:.1f}", COLORS["warning"]
            )
            c3.grid(row=0, column=2, padx=6, pady=6, sticky="nsew")

            c4 = self._make_stat_card(
                cards_frame, "🏆", "Topper",
                top["topper"]["name"], COLORS["gold"]
            )
            c4.grid(row=0, column=3, padx=6, pady=6, sticky="nsew")

            # Ranking table
            card = self._make_card(self.content_area)
            card.pack(fill="both", expand=True, padx=6, pady=6)

            ctk.CTkLabel(
                card,
                text="🏆  Student Rankings",
                font=(FONT_FAMILY, 15, "bold"),
                text_color=COLORS["text_primary"],
                anchor="w",
            ).pack(padx=18, pady=(14, 8), fill="x")

            cols = [("Rank", 80), ("Student", 200), ("Total", 120), ("Percentage", 120)]
            rows = [
                [r["rank"], r["name"], r["total"], f"{r['percentage']:.1f}%"]
                for r in ranking
            ]
            self._make_table(card, cols, rows)

        else:
            # Student dashboard
            name = self.app.logged_in_student
            report = engine.generate_report(name)
            if not report:
                self._show_error(self.content_area, "Could not load data.")
                return

            # Welcome banner
            banner = self._make_card(self.content_area)
            banner.pack(fill="x", padx=6, pady=(5, 10))

            ctk.CTkLabel(
                banner,
                text=f"Welcome back, {report['name']}! 👋",
                font=(FONT_FAMILY, 20, "bold"),
                text_color=COLORS["text_primary"],
                anchor="w",
            ).pack(padx=20, pady=(18, 2), fill="x")

            ctk.CTkLabel(
                banner,
                text=f"Roll No: {report['roll_number']}  •  Grade: {report['grade']}  •  Rank: #{report['rank']}",
                font=(FONT_FAMILY, 13),
                text_color=COLORS["text_secondary"],
                anchor="w",
            ).pack(padx=20, pady=(0, 16), fill="x")

            # Stat cards
            cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
            cards_frame.pack(fill="x", pady=(0, 10))
            for i in range(4):
                cards_frame.grid_columnconfigure(i, weight=1)

            self._make_stat_card(
                cards_frame, "📊", "Percentage",
                f"{report['percentage']:.1f}%", COLORS["secondary"]
            ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

            self._make_stat_card(
                cards_frame, "🎯", "Total Marks",
                f"{report['total']}/{report['max_marks']}", COLORS["primary_light"]
            ).grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

            self._make_stat_card(
                cards_frame, "🏅", "Grade",
                report["grade"], self._get_grade_color(report["grade"])
            ).grid(row=0, column=2, padx=6, pady=6, sticky="nsew")

            status_color = COLORS["success"] if report["status"] == "PASS" else COLORS["danger"]
            self._make_stat_card(
                cards_frame, "📋", "Status",
                report["status"], status_color
            ).grid(row=0, column=3, padx=6, pady=6, sticky="nsew")

            # Subject-wise marks
            card = self._make_card(self.content_area)
            card.pack(fill="both", expand=True, padx=6, pady=6)

            ctk.CTkLabel(
                card,
                text="📝  Subject-wise Marks",
                font=(FONT_FAMILY, 15, "bold"),
                text_color=COLORS["text_primary"],
                anchor="w",
            ).pack(padx=18, pady=(14, 8), fill="x")

            cols = [("Subject", 200), ("Marks", 120), ("Grade", 120)]
            rows = []
            for subj, mark in report["subjects"].items():
                pct = mark
                if pct >= 90:
                    g = "A+"
                elif pct >= 80:
                    g = "A"
                elif pct >= 70:
                    g = "B"
                elif pct >= 60:
                    g = "C"
                elif pct >= 40:
                    g = "D"
                else:
                    g = "F"
                rows.append([subj, mark, g])
            self._make_table(card, cols, rows, height=5)

    # ── Student Data ── #

    def _page_student_data(self):
        data = self.app.engine.get_student_data()
        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        cols = [("Roll No", 80), ("Name", 150)]
        for s in data["subjects"]:
            cols.append((s, 110))

        rows = []
        for st in data["students"]:
            row = [st["roll_number"], st["name"]]
            for s in data["subjects"]:
                row.append(st[s])
            rows.append(row)

        self._make_table(card, cols, rows)

    # ── Dataset Info ── #

    def _page_dataset_info(self):
        info = self.app.engine.get_dataset_info()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        for i in range(4):
            cards_frame.grid_columnconfigure(i, weight=1)

        items = [
            ("📐", "Shape", f"{info['shape'][0]} × {info['shape'][1]}", COLORS["secondary"]),
            ("📏", "Dimensions", f"{info['ndim']}D", COLORS["primary_light"]),
            ("🔢", "Data Type", info["dtype"], COLORS["warning"]),
            ("📊", "Total Elements", info["size"], COLORS["success"]),
        ]

        for i, (icon, label, val, color) in enumerate(items):
            self._make_stat_card(cards_frame, icon, label, val, color).grid(
                row=0, column=i, padx=6, pady=6, sticky="nsew"
            )

    # ── Explore Dataset ── #

    def _page_explore_dataset(self):
        overview = self.app.engine.get_dataset_overview()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        self._make_stat_card(
            cards_frame, "🎓", "Total Students",
            overview["total_students"], COLORS["secondary"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        self._make_stat_card(
            cards_frame, "📚", "Total Subjects",
            overview["total_subjects"], COLORS["primary_light"]
        ).grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

        # First & Last student
        for title, data in [("First Student", overview["first_student"]),
                            ("Last Student", overview["last_student"])]:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)

            ctk.CTkLabel(
                card, text=f"👤  {title}: {data['name']}",
                font=(FONT_FAMILY, 14, "bold"),
                text_color=COLORS["text_primary"], anchor="w",
            ).pack(padx=18, pady=(14, 4), fill="x")

            subjects = self.app.engine.get_all_subjects()
            marks_text = "  •  ".join(
                f"{s}: {m}" for s, m in zip(subjects, data["marks"])
            )
            ctk.CTkLabel(
                card, text=marks_text,
                font=(FONT_FAMILY, 13),
                text_color=COLORS["text_secondary"], anchor="w",
            ).pack(padx=18, pady=(0, 14), fill="x")

    # ── Student Marks ── #

    def _page_student_marks(self):
        fixed_name = self._student_name_for_page()

        if fixed_name:
            self._render_student_marks(fixed_name)
        else:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)

            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(padx=18, pady=14, fill="x")

            combo = self._make_dropdown(
                inner, "Select Student",
                self.app.engine.get_all_student_names()
            )

            result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
            result_area.pack(fill="both", expand=True)

            def go():
                for w in result_area.winfo_children():
                    w.destroy()
                self._render_student_marks(combo.get(), parent=result_area)

            self._make_go_button(inner, go)

    def _render_student_marks(self, name: str, parent=None):
        parent = parent or self.content_area
        data = self.app.engine.get_student_marks(name)
        if not data:
            self._show_error(parent, "Student not found.")
            return

        card = self._make_card(parent)
        card.pack(fill="x", padx=6, pady=6)

        ctk.CTkLabel(
            card, text=f"📝  Marks for {data['name']}",
            font=(FONT_FAMILY, 15, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, pady=(14, 8), fill="x")

        cols = [("Subject", 200), ("Marks", 150)]
        rows = [[s, m] for s, m in data["marks"].items()]
        self._make_table(card, cols, rows, height=5)

    # ── Subject Marks ── #

    def _page_subject_marks(self):
        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        combo = self._make_dropdown(
            inner, "Select Subject",
            self.app.engine.get_all_subjects()
        )
        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            data = self.app.engine.get_subject_marks(combo.get())
            if not data:
                self._show_error(result_area, "Subject not found.")
                return
            c = self._make_card(result_area)
            c.pack(fill="x", padx=6, pady=6)
            ctk.CTkLabel(
                c, text=f"📚  {data['subject']} — All Students",
                font=(FONT_FAMILY, 15, "bold"),
                text_color=COLORS["text_primary"], anchor="w",
            ).pack(padx=18, pady=(14, 8), fill="x")
            cols = [("Student", 200), ("Marks", 150)]
            rows = [[s["name"], s["marks"]] for s in data["students"]]
            self._make_table(c, cols, rows)

        self._make_go_button(inner, go)

    # ── Student Subject Mark ── #

    def _page_student_subject_mark(self):
        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        if self.role == "student":
            combo_sub = self._make_dropdown(
                inner, "Select Subject",
                self.app.engine.get_all_subjects()
            )
        else:
            combo_stu = self._make_dropdown(
                inner, "Select Student",
                self.app.engine.get_all_student_names()
            )
            combo_sub = self._make_dropdown(
                inner, "Select Subject",
                self.app.engine.get_all_subjects()
            )

        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            stu = self.app.logged_in_student if self.role == "student" else combo_stu.get()
            data = self.app.engine.get_student_subject_mark(stu, combo_sub.get())
            if not data:
                self._show_error(result_area, "Student or subject not found.")
                return
            c = self._make_card(result_area)
            c.pack(fill="x", padx=6, pady=6)

            items_frame = ctk.CTkFrame(c, fg_color="transparent")
            items_frame.pack(padx=18, pady=14, fill="x")
            for i in range(3):
                items_frame.grid_columnconfigure(i, weight=1)

            self._make_stat_card(
                items_frame, "👤", "Student", data["student"], COLORS["secondary"]
            ).grid(row=0, column=0, padx=6, sticky="nsew")
            self._make_stat_card(
                items_frame, "📚", "Subject", data["subject"], COLORS["primary_light"]
            ).grid(row=0, column=1, padx=6, sticky="nsew")
            self._make_stat_card(
                items_frame, "🎯", "Marks", data["marks"], COLORS["gold"]
            ).grid(row=0, column=2, padx=6, sticky="nsew")

        self._make_go_button(inner, go)

    # ── Students Range ── #

    def _page_students_range(self):
        names = self.app.engine.get_all_student_names()
        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        c1 = self._make_dropdown(inner, "Start Student", names)
        c2 = self._make_dropdown(inner, "End Student", names)
        if len(names) > 1:
            c2.set(names[-1])

        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            data = self.app.engine.get_students_range(c1.get(), c2.get())
            if not data:
                self._show_error(result_area, "Invalid range or student not found.")
                return
            subjects = self.app.engine.get_all_subjects()
            c = self._make_card(result_area)
            c.pack(fill="both", expand=True, padx=6, pady=6)
            cols = [("Student", 150)] + [(s, 110) for s in subjects]
            rows = []
            for st in data["students"]:
                row = [st["name"]]
                for s in subjects:
                    row.append(st["marks"].get(s, ""))
                rows.append(row)
            self._make_table(c, cols, rows)

        self._make_go_button(inner, go)

    # ── Subject Range ── #

    def _page_subject_range(self):
        subjects = self.app.engine.get_all_subjects()
        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        c1 = self._make_dropdown(inner, "Start Subject", subjects)
        c2 = self._make_dropdown(inner, "End Subject", subjects)
        if len(subjects) > 1:
            c2.set(subjects[-1])

        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            data = self.app.engine.get_subject_range(c1.get(), c2.get())
            if not data:
                self._show_error(result_area, "Invalid range or subject not found.")
                return
            c = self._make_card(result_area)
            c.pack(fill="both", expand=True, padx=6, pady=6)
            cols = [("Student", 150)] + [(s, 110) for s in data["subjects"]]
            rows = []
            for st in data["students"]:
                row = [st["name"]]
                for s in data["subjects"]:
                    row.append(st["marks"].get(s, ""))
                rows.append(row)
            self._make_table(c, cols, rows)

        self._make_go_button(inner, go)

    # ── Student Subject Range ── #

    def _page_student_subject_range(self):
        names = self.app.engine.get_all_student_names()
        subjects = self.app.engine.get_all_subjects()

        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        cs1 = self._make_dropdown(inner, "Start Subject", subjects)
        cs2 = self._make_dropdown(inner, "End Subject", subjects)
        if len(subjects) > 1:
            cs2.set(subjects[-1])
        cn1 = self._make_dropdown(inner, "Start Student", names)
        cn2 = self._make_dropdown(inner, "End Student", names)
        if len(names) > 1:
            cn2.set(names[-1])

        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            data = self.app.engine.get_student_subject_range(
                cs1.get(), cs2.get(), cn1.get(), cn2.get()
            )
            if not data:
                self._show_error(result_area, "Invalid range.")
                return
            c = self._make_card(result_area)
            c.pack(fill="both", expand=True, padx=6, pady=6)
            cols = [("Student", 150)] + [(s, 110) for s in data["subjects"]]
            rows = []
            for st in data["students"]:
                row = [st["name"]]
                for s in data["subjects"]:
                    row.append(st["marks"].get(s, ""))
                rows.append(row)
            self._make_table(c, cols, rows)

        self._make_go_button(inner, go)

    # ── Student Statistics ── #

    def _page_student_statistics(self):
        fixed = self._student_name_for_page()

        if fixed:
            self._render_student_statistics(fixed)
        else:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)
            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(padx=18, pady=14, fill="x")

            combo = self._make_dropdown(
                inner, "Select Student",
                self.app.engine.get_all_student_names()
            )
            result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
            result_area.pack(fill="both", expand=True)

            def go():
                for w in result_area.winfo_children():
                    w.destroy()
                self._render_student_statistics(combo.get(), parent=result_area)

            self._make_go_button(inner, go)

    def _render_student_statistics(self, name: str, parent=None):
        parent = parent or self.content_area
        data = self.app.engine.get_student_statistics(name)
        if not data:
            self._show_error(parent, "Student not found.")
            return

        # Header
        header_card = self._make_card(parent)
        header_card.pack(fill="x", padx=6, pady=6)
        ctk.CTkLabel(
            header_card, text=f"📈  Statistics for {data['name']}",
            font=(FONT_FAMILY, 16, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, pady=14, fill="x")

        # Stat cards grid
        grid = ctk.CTkFrame(parent, fg_color="transparent")
        grid.pack(fill="x", padx=0, pady=5)
        for i in range(4):
            grid.grid_columnconfigure(i, weight=1)

        stats = [
            ("📊", "Total", data["total"], COLORS["secondary"]),
            ("📈", "Average", f"{data['average']:.1f}", COLORS["primary_light"]),
            ("⬆️", "Highest", data["highest"], COLORS["success"]),
            ("⬇️", "Lowest", data["lowest"], COLORS["danger"]),
            ("📏", "Median", data["median"], COLORS["warning"]),
            ("📉", "Std Dev", data["std_dev"], COLORS["accent_cyan"]),
            ("📐", "Variance", data["variance"], COLORS["primary_light"]),
        ]

        for i, (icon, label, val, color) in enumerate(stats):
            r, c = divmod(i, 4)
            self._make_stat_card(grid, icon, label, val, color).grid(
                row=r, column=c, padx=6, pady=6, sticky="nsew"
            )

        # Subject marks table
        card = self._make_card(parent)
        card.pack(fill="x", padx=6, pady=6)
        cols = [("Subject", 200), ("Marks", 150)]
        rows = [[s, m] for s, m in data["marks"].items()]
        self._make_table(card, cols, rows, height=5)

    # ── Subject Statistics ── #

    def _page_subject_statistics(self):
        card = self._make_card(self.content_area)
        card.pack(fill="x", padx=6, pady=6)
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(padx=18, pady=14, fill="x")

        combo = self._make_dropdown(
            inner, "Select Subject",
            self.app.engine.get_all_subjects()
        )
        result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
        result_area.pack(fill="both", expand=True)

        def go():
            for w in result_area.winfo_children():
                w.destroy()
            data = self.app.engine.get_subject_statistics(combo.get())
            if not data:
                self._show_error(result_area, "Subject not found.")
                return

            grid = ctk.CTkFrame(result_area, fg_color="transparent")
            grid.pack(fill="x", pady=5)
            for i in range(4):
                grid.grid_columnconfigure(i, weight=1)

            stats = [
                ("📊", "Total", data["total"], COLORS["secondary"]),
                ("📈", "Average", f"{data['average']:.1f}", COLORS["primary_light"]),
                ("⬆️", "Highest", data["highest"], COLORS["success"]),
                ("⬇️", "Lowest", data["lowest"], COLORS["danger"]),
                ("📏", "Median", data["median"], COLORS["warning"]),
                ("📉", "Std Dev", data["std_dev"], COLORS["accent_cyan"]),
                ("📐", "Variance", data["variance"], COLORS["primary_light"]),
            ]
            for i, (icon, label, val, color) in enumerate(stats):
                r, c = divmod(i, 4)
                self._make_stat_card(grid, icon, label, val, color).grid(
                    row=r, column=c, padx=6, pady=6, sticky="nsew"
                )

            # Student marks table
            c2 = self._make_card(result_area)
            c2.pack(fill="x", padx=6, pady=6)
            ctk.CTkLabel(
                c2, text=f"📚  {data['subject']} — Student Marks",
                font=(FONT_FAMILY, 15, "bold"),
                text_color=COLORS["text_primary"], anchor="w",
            ).pack(padx=18, pady=(14, 8), fill="x")
            cols = [("Student", 200), ("Marks", 150)]
            rows = [[n, m] for n, m in data["marks"].items()]
            self._make_table(c2, cols, rows)

        self._make_go_button(inner, go)

    # ── Class Statistics ── #

    def _page_class_statistics(self):
        data = self.app.engine.get_class_statistics()

        grid = ctk.CTkFrame(self.content_area, fg_color="transparent")
        grid.pack(fill="x", pady=5)
        for i in range(4):
            grid.grid_columnconfigure(i, weight=1)

        stats = [
            ("🎓", "Students", data["total_students"], COLORS["secondary"]),
            ("📚", "Subjects", data["total_subjects"], COLORS["primary_light"]),
            ("📊", "Average", f"{data['overall_average']:.1f}", COLORS["warning"]),
            ("⬆️", "Highest", data["highest_mark"], COLORS["success"]),
            ("⬇️", "Lowest", data["lowest_mark"], COLORS["danger"]),
            ("📏", "Median", data["median"], COLORS["accent_cyan"]),
            ("📉", "Std Dev", data["std_dev"], COLORS["primary_light"]),
            ("📐", "Variance", data["variance"], COLORS["gold"]),
        ]
        for i, (icon, label, val, color) in enumerate(stats):
            r, c = divmod(i, 4)
            self._make_stat_card(grid, icon, label, val, color).grid(
                row=r, column=c, padx=6, pady=6, sticky="nsew"
            )

    # ── Student Ranking ── #

    def _page_student_ranking(self):
        ranking = self.app.engine.get_student_ranking()

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        ctk.CTkLabel(
            card, text="🏆  Student Rankings — Sorted by Total Marks",
            font=(FONT_FAMILY, 15, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, pady=(14, 8), fill="x")

        cols = [("Rank", 80), ("Student", 200), ("Total", 120), ("Percentage", 120)]
        rows = []
        for r in ranking:
            medal = ""
            if r["rank"] == 1:
                medal = "🥇 "
            elif r["rank"] == 2:
                medal = "🥈 "
            elif r["rank"] == 3:
                medal = "🥉 "
            rows.append([
                f"{medal}{r['rank']}", r["name"],
                r["total"], f"{r['percentage']:.1f}%"
            ])
        self._make_table(card, cols, rows)

    # ── Topper & Lowest ── #

    def _page_topper_lowest(self):
        data = self.app.engine.get_topper_and_lowest()

        grid = ctk.CTkFrame(self.content_area, fg_color="transparent")
        grid.pack(fill="x", pady=5)
        grid.grid_columnconfigure(0, weight=1)
        grid.grid_columnconfigure(1, weight=1)

        # Topper card
        t_card = self._make_card(grid)
        t_card.grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        ctk.CTkLabel(
            t_card, text="🏆  CLASS TOPPER",
            font=(FONT_FAMILY, 13, "bold"),
            text_color=COLORS["gold"], anchor="w",
        ).pack(padx=18, pady=(18, 8), fill="x")

        ctk.CTkLabel(
            t_card, text=data["topper"]["name"],
            font=(FONT_FAMILY, 30, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, fill="x")

        ctk.CTkLabel(
            t_card, text=f"Total Marks: {data['topper']['total']}",
            font=(FONT_FAMILY, 14),
            text_color=COLORS["text_secondary"], anchor="w",
        ).pack(padx=18, pady=(4, 18), fill="x")

        # Lowest card
        l_card = self._make_card(grid)
        l_card.grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

        ctk.CTkLabel(
            l_card, text="📉  LOWEST SCORER",
            font=(FONT_FAMILY, 13, "bold"),
            text_color=COLORS["danger"], anchor="w",
        ).pack(padx=18, pady=(18, 8), fill="x")

        ctk.CTkLabel(
            l_card, text=data["lowest"]["name"],
            font=(FONT_FAMILY, 30, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, fill="x")

        ctk.CTkLabel(
            l_card, text=f"Total Marks: {data['lowest']['total']}",
            font=(FONT_FAMILY, 14),
            text_color=COLORS["text_secondary"], anchor="w",
        ).pack(padx=18, pady=(4, 18), fill="x")

    # ── Subject Toppers ── #

    def _page_subject_toppers(self):
        data = self.app.engine.get_subject_toppers()

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        ctk.CTkLabel(
            card, text="🥇  Subject Toppers",
            font=(FONT_FAMILY, 15, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(padx=18, pady=(14, 8), fill="x")

        cols = [("Subject", 200), ("Topper", 200), ("Marks", 120)]
        rows = [[d["subject"], d["student"], d["marks"]] for d in data]
        self._make_table(card, cols, rows, height=5)

    # ── Passed Students ── #

    def _page_passed_students(self):
        data = self.app.engine.get_passed_students()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        cards_frame.grid_columnconfigure(0, weight=1)

        self._make_stat_card(
            cards_frame, "✅", "Total Passed",
            data["total"], COLORS["success"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        cols = [("#", 60), ("Student Name", 300)]
        rows = [[i + 1, name] for i, name in enumerate(data["students"])]
        self._make_table(card, cols, rows)

    # ── Failed Students ── #

    def _page_failed_students(self):
        data = self.app.engine.get_failed_students()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        cards_frame.grid_columnconfigure(0, weight=1)

        self._make_stat_card(
            cards_frame, "❌", "Total Failed",
            data["total"], COLORS["danger"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        cols = [("#", 60), ("Student Name", 300)]
        rows = [[i + 1, name] for i, name in enumerate(data["students"])]
        self._make_table(card, cols, rows)

    # ── Above Average ── #

    def _page_above_average(self):
        data = self.app.engine.get_above_average()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        for i in range(2):
            cards_frame.grid_columnconfigure(i, weight=1)

        self._make_stat_card(
            cards_frame, "📊", "Class Average",
            f"{data['class_average']:.1f}", COLORS["warning"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        self._make_stat_card(
            cards_frame, "📈", "Students Above Avg",
            data["total_count"], COLORS["success"]
        ).grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        cols = [("#", 60), ("Student", 200), ("Total Marks", 150)]
        rows = [
            [i + 1, s["name"], s["total"]]
            for i, s in enumerate(data["students"])
        ]
        self._make_table(card, cols, rows)

    # ── Below Average ── #

    def _page_below_average(self):
        data = self.app.engine.get_below_average()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        for i in range(2):
            cards_frame.grid_columnconfigure(i, weight=1)

        self._make_stat_card(
            cards_frame, "📊", "Class Average",
            f"{data['class_average']:.1f}", COLORS["warning"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        self._make_stat_card(
            cards_frame, "📉", "Students Below Avg",
            data["total_count"], COLORS["danger"]
        ).grid(row=0, column=1, padx=6, pady=6, sticky="nsew")

        card = self._make_card(self.content_area)
        card.pack(fill="both", expand=True, padx=6, pady=6)

        cols = [("#", 60), ("Student", 200), ("Total Marks", 150)]
        rows = [
            [i + 1, s["name"], s["total"]]
            for i, s in enumerate(data["students"])
        ]
        self._make_table(card, cols, rows)

    # ── Full Marks ── #

    def _page_full_marks(self):
        data = self.app.engine.get_full_marks_students()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        cards_frame.grid_columnconfigure(0, weight=1)

        self._make_stat_card(
            cards_frame, "💯", "Students with Full Marks",
            data["total"], COLORS["gold"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        if data["total"] == 0:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)
            ctk.CTkLabel(
                card, text="No student scored full marks in any subject.",
                font=(FONT_FAMILY, 14),
                text_color=COLORS["text_secondary"],
            ).pack(padx=18, pady=20)
        else:
            card = self._make_card(self.content_area)
            card.pack(fill="both", expand=True, padx=6, pady=6)

            cols = [("Student", 200), ("Subject", 200), ("Marks", 120)]
            rows = []
            for st in data["students"]:
                for sub in st["subjects"]:
                    rows.append([st["name"], sub["subject"], sub["marks"]])
            self._make_table(card, cols, rows)

    # ── Failed Subjects ── #

    def _page_failed_subjects(self):
        data = self.app.engine.get_failed_subjects()

        cards_frame = ctk.CTkFrame(self.content_area, fg_color="transparent")
        cards_frame.pack(fill="x", pady=5)
        cards_frame.grid_columnconfigure(0, weight=1)

        self._make_stat_card(
            cards_frame, "⚠️", "Students with Failed Subjects",
            data["total"], COLORS["danger"]
        ).grid(row=0, column=0, padx=6, pady=6, sticky="nsew")

        if data["total"] == 0:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)
            ctk.CTkLabel(
                card, text="No student failed in any subject. 🎉",
                font=(FONT_FAMILY, 14),
                text_color=COLORS["success"],
            ).pack(padx=18, pady=20)
        else:
            card = self._make_card(self.content_area)
            card.pack(fill="both", expand=True, padx=6, pady=6)

            cols = [("Student", 200), ("Subject", 200), ("Marks", 120)]
            rows = []
            for st in data["students"]:
                for sub in st["subjects"]:
                    rows.append([st["name"], sub["subject"], sub["marks"]])
            self._make_table(card, cols, rows)

    # ── Generate Report ── #

    def _page_generate_report(self):
        fixed = self._student_name_for_page()

        if fixed:
            self._render_report(fixed)
        else:
            card = self._make_card(self.content_area)
            card.pack(fill="x", padx=6, pady=6)
            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(padx=18, pady=14, fill="x")

            combo = self._make_dropdown(
                inner, "Select Student",
                self.app.engine.get_all_student_names()
            )
            result_area = ctk.CTkFrame(self.content_area, fg_color="transparent")
            result_area.pack(fill="both", expand=True)

            def go():
                for w in result_area.winfo_children():
                    w.destroy()
                self._render_report(combo.get(), parent=result_area)

            self._make_go_button(inner, go)

    def _render_report(self, name: str, parent=None):
        parent = parent or self.content_area
        data = self.app.engine.generate_report(name)
        if not data:
            self._show_error(parent, "Student not found.")
            return

        # ── Report Card ──
        report_card = self._make_card(parent)
        report_card.pack(fill="x", padx=6, pady=6)

        # Header
        header = ctk.CTkFrame(report_card, fg_color=COLORS["primary"], corner_radius=12)
        header.pack(fill="x", padx=12, pady=(12, 0))

        ctk.CTkLabel(
            header, text="📄  STUDENT REPORT CARD",
            font=(FONT_FAMILY, 18, "bold"),
            text_color="#ffffff", anchor="w",
        ).pack(padx=18, pady=14, fill="x")

        # Student info
        info_frame = ctk.CTkFrame(report_card, fg_color="transparent")
        info_frame.pack(fill="x", padx=18, pady=(14, 5))

        for label, val in [("Name", data["name"]), ("Roll No", data["roll_number"])]:
            row = ctk.CTkFrame(info_frame, fg_color="transparent")
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(
                row, text=f"{label}:", width=120,
                font=(FONT_FAMILY, 13, "bold"),
                text_color=COLORS["text_secondary"], anchor="w",
            ).pack(side="left")
            ctk.CTkLabel(
                row, text=str(val),
                font=(FONT_FAMILY, 13),
                text_color=COLORS["text_primary"], anchor="w",
            ).pack(side="left")

        # Subject marks with progress bars
        marks_frame = ctk.CTkFrame(report_card, fg_color="transparent")
        marks_frame.pack(fill="x", padx=18, pady=(10, 5))

        ctk.CTkLabel(
            marks_frame, text="Subject-wise Performance",
            font=(FONT_FAMILY, 14, "bold"),
            text_color=COLORS["text_primary"], anchor="w",
        ).pack(fill="x", pady=(0, 8))

        for subj, mark in data["subjects"].items():
            row = ctk.CTkFrame(marks_frame, fg_color="transparent")
            row.pack(fill="x", pady=3)

            ctk.CTkLabel(
                row, text=subj, width=110,
                font=(FONT_FAMILY, 12),
                text_color=COLORS["text_secondary"], anchor="w",
            ).pack(side="left")

            # Color based on mark
            if mark >= 90:
                bar_color = COLORS["success"]
            elif mark >= 75:
                bar_color = COLORS["secondary"]
            elif mark >= 60:
                bar_color = COLORS["warning"]
            elif mark >= 40:
                bar_color = "#ff9800"
            else:
                bar_color = COLORS["danger"]

            bar = ctk.CTkProgressBar(
                row, width=300, height=16,
                corner_radius=8,
                fg_color=COLORS["bg_input"],
                progress_color=bar_color,
            )
            bar.pack(side="left", padx=(5, 10))
            bar.set(mark / 100)

            ctk.CTkLabel(
                row, text=f"{mark}/100",
                font=(FONT_FAMILY, 12, "bold"),
                text_color=COLORS["text_primary"],
            ).pack(side="left")

        # Summary row
        summary = ctk.CTkFrame(report_card, fg_color="transparent")
        summary.pack(fill="x", padx=12, pady=(10, 14))
        for i in range(5):
            summary.grid_columnconfigure(i, weight=1)

        grade_color = self._get_grade_color(data["grade"])
        status_color = COLORS["success"] if data["status"] == "PASS" else COLORS["danger"]

        items = [
            ("Total", f"{data['total']}/{data['max_marks']}", COLORS["secondary"]),
            ("Percentage", f"{data['percentage']:.1f}%", COLORS["primary_light"]),
            ("Grade", data["grade"], grade_color),
            ("Rank", f"#{data['rank']}", COLORS["gold"]),
            ("Status", data["status"], status_color),
        ]
        for i, (label, val, color) in enumerate(items):
            self._make_stat_card(summary, "", label, val, color).grid(
                row=0, column=i, padx=4, pady=4, sticky="nsew"
            )


# ──────────────────────── Entry Point ──────────────────────── #

if __name__ == "__main__":
    app = StudentMarksApp()
    app.mainloop()
