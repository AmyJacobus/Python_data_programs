#!/usr/bin/env python3

import validation as v
import student_maintenance as sm
import course_maintenance as csm
import sports_maintenance as spm


"""
# Programmer: Caleb Fowler
# Date: October 31, 2021
# Description:     Student Data System for managing student information (student id, first name, and last name)
"""

# the following are module level dunders (metadata) for the authorship information
__author__ = 'Caleb Fowler'
__version__ = '1.0'
__date__ = '2021.11.02'
_status__ = 'Development'


def display_main_menu():
    print("MAIN MENU")
    print('=================================')
    print("1 - Student Maintenance Menu")
    print("2 -  Courses Maintenance Menu")
    print("3 -  Sports Menu")
    print("4 - Full Report")
    print("0 - Exit Program")

    print()

def student_maint_menu():
    """
     display_menu()
         Displays a list of all the valid main menu options
         It also handles for nonnumerical data and invalid menu option selected.

         1 - Student Maintenance Menu
         2 - Courses Maintenance Menu
         3 - Sports Menu
         4 - Full Report
         0 - Exit program

         :return no value
         :rtype none
        """
    print("MAIN MENU")
    print('=================================')
    print("1 - Student Maintenance Menu")
    print("2 -  Courses Maintenance Menu")
    print("3 -  Sports Menu")
    print("4 - Full Report")
    print("0 - Exit Program")

    print()


def student_maint_menu(students, next_student_id):

    display_menu_student_mntc()

    command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')

    while True:
        if command == 1:
            sm.list(students)
            return students
        elif command == 2:
            sm.add(students, next_student_id)
            next_student_id += 1
            return students, next_student_id
        elif command == 3:
            sm.update(students)
            return students
        elif command == 4:
            sm.delete(students)
            return students
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")


def main(students, next_student_id):

    # students = []
    # next_student_id = 1

    while True:
        display_main_menu()

        command = v.get_range('Please enter a Menu #', 0, 4)
        print()

        if command == 1:
            student_maint_menu(students, next_student_id)
    #     elif command == 2:
    #         # sm.add(students, next_student_id)
    #         next_student_id += 1
    #     elif command == 3:
    #         # sm.update(students)
    #     elif command == 4:
    #         # sm.delete(students)
    #     elif command == 0:
    #         break
    #     else:
    #         print("Not a valid command. Please try again.\n")
    #
    #     print()
    # print("Bye!")


if __name__ == "__main__":
    main()


