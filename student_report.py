"""
Programmer: Caleb Fowler and Ammishaddai Jacobus
Date: Nov 10, 2021
Description: This is the student report module. In this module we output the student report to the user. It outputs all
the user's store in the database, their ID, their first name, their last name, the courses they are enrolled in, and
their sports. The user also gets the option to exit this program and go back to the main menu of the database.
"""


import student_maintenance as sm
import validation as v


# the following are module level dunders (metadata) for the authorship information
__author__ = 'Caleb Fowler and Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = '2021.11.02'
_status__ = 'Development'


def display_menu():
    """
    This is the main menu to be displayed for this module.
    :return: n/a
    """
    print('Student Records Report Menu')
    print('=' * 50)
    print('1 - List all students report')
    print('0 - Return to Main Menu')
    print()


def all_students_data(students):
    """
    This function basically first checks if there are any students in the database, if not, it will tell the user
    that there are no students in the database. And if there are students in the database, it will display the students
    in a nicely formatted report.
    :param students: This module takes the parameter students in order to use the list information to output
    that data nicely formatted.
    :return: n/a
    """

    print()
    print('Report of all students in the database')
    print()

    if len(students) == 0:
        print('There are no students in the list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s} {"Courses":<34s} {"sports":<53s}')
    print('=' * 4, '=' * 15, '='*15, '=' * 34,'=' * 54 )

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:>4d} {first_name:<15s} {last_name:<16s}', end='')

        course_list = ''
        sport_list = ''

        for course in courses:
            course_list += course + ', '
        print(f'{course_list:<36s}', end='')

        for sports_list in sports:
            print(f'{sports_list}', end=', ')
        print()

    return


def main_menu(students):
    """
    THis is the main menu for the student report module. It displays the menu of this module. It takes user input of
    menu option they want to choose, it validates their input. They can either choose to see the report or choose
    to exit the this module. The main also tells them once they have successfully exited the database.
    :param students: This module takes the parameter student to use the list students to run other functions in this module.
    :return: n/a
    """


    while True:

        display_menu()

        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=2, data_type='int')
        if command == 1:
            all_students_data(students)
        elif command == 0:
            print('Exiting the student database menu now..')
            print('You have successfully exited the student database.')
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


if __name__ == "__main__":  # Basically if the name of the module is equal to main
        main_menu()  # Run this specific program.