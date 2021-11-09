#!/usr/bin/env python3

"""
Programmer: Caleb Fowler  and Ammishaddai Jacobus
Date: Nov 10, 2021
Description: This the main module that imports all modules and runs them as a main program. It imports student maintenance,
course maintenance, student sports,  student report and the validation to validate all user input. All these together
make up the student database menu.
"""

import validation as v
import student_maintenance as sm
import course_maintenance as csm
import sports_maint as spm
import student_report as str

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Caleb Fowler'
__version__ = '1.0'
__date__ = '2021.11.02'
_status__ = 'Development'


def display_main_menu():
    print("MAIN MENU")
    print('=================================')
    print("1 - Student Maintenance Menu")
    print("2 - Courses Maintenance Menu")
    print("3 - Sports Menu")
    print("4 - Full Report")
    print("0 - Exit Program")
    print()


def main():

    students = []
    next_student_id = 1

    while True:
        display_main_menu()

        command = v.get_range('Please enter a Menu #', low=-1, high=4)
        print()

        if command == 1:
            sm.main_menu(students, next_student_id)
        elif command == 2:
            csm.main_menu(students, valid_courses)
        elif command == 3:
            spm.main_menu(students, valid_sports)
        elif command == 4:
            str.main_menu(students)
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
    print("You have successfully exited the database!")


if __name__ == "__main__":
    main()
