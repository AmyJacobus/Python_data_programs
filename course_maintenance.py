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




def delete_student_course(student,, valid_courses):
    print()