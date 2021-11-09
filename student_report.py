"""
Programmer: Caleb Fowler and Ammishaddai Jacobus
Date: Nov 10, 2021
Description: This is the student report module. In this module we output the student report to the user. It outputs all
the user's store in the database, their ID, their first name, their last name, the courses they are enrolled in, and
their sports.
"""


import student_maintenance as sm
import validation as v


# the following are module level dunders (metadata) for the authorship information
__author__ = 'Caleb Fowler & Amy Jacobus'
__version__ = '1.0'
__date__ = '2021.11.02'
_status__ = 'Development'


def display_menu():
    print('Student Records Report Menu')
    print('=' * 50)
    print('1 - List all students report')
    print('0 - Return to Main Menu')
    print()


def selected_student_data():
    print('Display data for a selected student')


def all_students_data(students):

    print('Report of all students in the database')

    if len(students) == 0:
        print('There are no students in the list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s} {"Courses":<43s} {"sports":<53s}')
    print('=' * 4, '=' * 15, '='*15, '=' * 34,'=' * 54 )

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:>4d} {first_name:<15s} {last_name:<16s}', end='')

        course_list = ''
        sport_list = ''

        for course in courses:
            course_list += course + ', '
        print(f'{course_list:<36s}', end='')

        for course in courses:
            print(f'{course}', end=', ')
        print()

    return


def main_menu(students):


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