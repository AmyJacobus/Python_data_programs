#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

import validation as v
import student_maintenance as sm

# Authorship
__author__ = 'ADD NAMES HERE'
__version__ = '1.0'
__date__ = 'NOV 2, 2021'
__status__ = 'Development'


def display_main():
    print()

def main_menu(students, valid_courses):
    print()

def list_student_courses(students):
    print()


def list_courses_option(valid_courses, mode='added'):
    print()

def add_student_course(students, valid_courses):

    print('Add student courses')
    print('='*50)

    student_id = v.get_positive(prompt='Please type in the ID # of the student you would like to add courses'
                                       'for', limit=0)

    student_index = sm.find_student_index(student_id)

    student = students[student_index] # I have the student now

    # display what courses the student is current enrolled in by calling list_student_courses passing
    # only the selected students data
    print(f'Student ID # {student[0]} {student[1]} {student[2]} is currently enrolled in courses: {student[3]}')

    # Display what courses that the user can select from by calling the list_courses_option passing the tuple
    # of valid courses, and the mode added
    print(f'The student can select the following courses: {list_courses_option(valid_courses)}')

    while True:
        # ADD A MAX OF NUMBERS FOR COURSES STILL
        course_number = v.get_range(prompt='What course number would you like to add: ', low=0, high=)
        if course_number == 0:
            break

        course_name =







def delete_student_course(student,, valid_courses):
    print()