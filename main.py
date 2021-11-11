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
    """
    Displays a list of all the valid main menu options
    It also handles for nonnumerical data and invalid menu option selected

    1-Student Maintenance
    2-Course Maintenance
    3-Sport Maintenance
    4-Full Report
    0-Exit Program

    :return: n/a
    """
    print("MAIN MENU")
    print('=================================')
    print("1 - Student Maintenance Menu")
    print("2 - Courses Maintenance Menu")
    print("3 - Sports Maintenance Menu")
    print("4 - Full Report")
    print("0 - Exit Program")
    print()


def main():
    """
    Main keep the program looping until the user enters 0 to exit the program
    then based on the user's selected, will call the corresponding function option
    Local scoped students is a 2D list that is pass as an argument to each menu option function
    Local scoped max_student_id is the last student id used, and is passed to the add_student function,
    and this function will return the last added student id

    :return: n/a
    """

    valid_courses = ('English', 'History', 'Math', 'Science')
    valid_sports = ('Football', 'Volleyball', 'Basketball', 'Track')

    students = [
        [1, 'John', 'Doe', ['English', 'Science'], ['Volleyball']],
        [3, 'Samy', 'Smith', ['English', 'History', 'Math'], ['Football', 'Basketball']]
    ]

    next_student_id = 4

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
