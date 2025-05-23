# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 22:08:50 2025

@author: gidfr
"""

str = 'Firstname MiddleName Surname RegNo Sex'
# Given string (example)
student_info = 'Tumaini Hamis Kimario 2016-06-56789 M'

# (a) Display the value of str
print("Student Info:", student_info)

# Manually extracting each part of the string using slicing
first_name = student_info[:student_info.find(" ")]  # First word before the first space
middle_name = student_info[student_info.find(" ") + 1: student_info.find(" ", student_info.find(" ") + 1)]  # Between first and second space
surname_start = student_info.find(" ", student_info.find(" ") + 1) + 1
surname_end = student_info.find(" ", surname_start)
surname = student_info[surname_start:surname_end if surname_end != -1 else None]  # Between second and third space
reg_no_start = student_info.find(" ", surname_end) + 1
reg_no_end = student_info.find(" ", reg_no_start)
reg_no = student_info[reg_no_start:reg_no_end if reg_no_end != -1 else None]  # Between third and fourth space
sex = student_info[-1]  # Last character in the string

# (b) Display the particulars with names capitalized
first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
surname = surname.capitalize()

sex_display = "Male" if sex == "M" else "Female"  # To handle Male or Female

print(f"Firstname: {first_name}")
print(f"Middle name: {middle_name}")
print(f"Surname: {surname}")
print(f"Reg. No.: {reg_no}")
print(f"Sex: {sex_display}")

# (c) Display the full name starting with surname in capital letters and followed by initials
surname = surname.upper()
initials = f"{first_name[0].upper()}.{middle_name[0].upper()}."

print(f"Fullname is: {surname}, {initials}")

# (d) Display if the student is Male or Female
is_male = sex == "M"
is_female = sex == "F"

print(f"Is student Male? {is_male}")
print(f"Is student Female? {is_female}")
