#!/usr/bin/env python3

import validation as v
import student_maintenance as sm
import course_maintenance as csm
import sports_maintenance as spm


"""
# Programmer: Amy and Caleb
# Date: October 31, 2021
# Description:     Student Data System for managing student information (student id, first name, and last name)
"""

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Amy and Caleb'
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


def student_mntc():
    """
     display_menu()
         Displays a list of all the valid main menu options
         It also handles for nonnumerical data and invalid menu option selected.

         1 - List of Students
         2 - Add Student
         3 - Delete Student
         4 - Update Student
         0 - Return to Main Menu

         :return no value
         :rtype none
        """
    print("STUDENT MAINTENANCE MENU")
    print('=================================')
    print("1 - List of Students")
    print("2 -  Add Student")
    print("3 -  Delete Student")
    print("4 - Update Student")
    print("0 - Return to Main Menu")

    print()


def student_maint_menu(students, next_student_id):

    display_student_mntc()

    command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')

    while True:
        if command == 1:
            sm.list(students)
        elif command == 2:
            sm.add(students, next_student_id)
            next_student_id += 1
            return next_student_id
        elif command == 3:
            sm.update(students)
        elif command == 4:
            sm.delete(students)
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")


def course_mntc():
    """
     display_menu()
         Displays a list of all the valid main menu options
         It also handles for nonnumerical data and invalid menu option selected.

         1 - Course List
         2 - Add Course
         3 - Delete Course
         0 - Return to Main Menu

         :return no value
         :rtype none
        """
    print("COURSE MAINTENANCE MENU")
    print('=================================')
    print("1 - Course List")
    print("2 -  Add Course")
    print("3 -  Delete Course")
    print("0 - Return to Main Menu")

    print()


def course_maint_menu(students, next_student_id):

    display_course_mntc()

    command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')

    while True:
        if command == 1:
            sm.list(courses)
        elif command == 2:
            sm.add(students, next_student_id)  # add will change once we get course maintenance running
            next_student_id += 1
            return next_student_id
        elif command == 3:
            sm.update(courses)
        elif command == 0:
            return
        else:
            print("Not a valid command. Please try again.\n")


def sport_mntc():
    """
     display_menu()
         Displays a list of all the valid main menu options
         It also handles for nonnumerical data and invalid menu option selected.

         1 - Sports List
         2 - Add Sport
         3 - Delete Sport
         0 - Return to Main Menu

         :return no value
         :rtype none
        """
    print("COURSE MAINTENANCE MENU")
    print('=================================')
    print("1 - Sports List")
    print("2 -  Add Sport")
    print("3 -  Delete Sport")
    print("0 - Return to Main Menu")

    print()


def sport_maint_menu(students, next_student_id):

    display_sport_mntc()

    command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')

    while True:
        if command == 1:
            sm.list(sports)
        elif command == 2:
            sm.add(students, next_student_id)  # add will change once we get course maintenance running
            next_student_id += 1
            return next_student_id
        elif command == 3:
            sm.update(sports)
        elif command == 0:
            return
        else:
            print("Not a valid command. Please try again.\n")


def main():

    students = []
    next_student_id = 1

    while True:
        display_main_menu()

        command = v.get_range('Please enter a Menu #', 0, 4)
        print()

        if command == 1:
            display_student_maint_menu()
        elif command == 2:
            display_course_maint_menu()
        elif command == 3:
            display_sport_maint_menu()
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
    print("Bye!")


if __name__ == "__main__":
    main()


