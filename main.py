#!/usr/bin/env python3

import validation as v
import student_maint as sm

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


def main():
    """
       main()
             Main keeps the program looping until the user enters 0 to exit the program
             then based on the user's selected, will call the corresponding function option
             Local scoped students is a 2D list that is pass as an argument to each menu option function
             Local scoped max_student_id is the last student id used, and is passed to the add_student function,
             and this function will return the last added student id
            :return no value
            :rtype none
    """
    students = []
    next_student_id = 1

    while True:
        display_main_menu()
        command = v.get_range('Please enter a Menu #', 0, 4)
        print()

        if command == 1:
            sm.list(students)
        elif command == 2:
            sm.add(students, next_student_id)
            next_student_id += 1
        elif command == 3:
            sm.update(students)
        elif command == 4:
            sm.delete(students)
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
    print("Bye!")


if __name__ == "__main__":
    main()


