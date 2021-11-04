#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

# Authorship
__author__ = 'ADD NAMES HERE'
__version__ = '1.0'
__date__ = 'NOV 2, 2021'
__status__ = 'Development'

import validation as v


def display_menu():
    """
    Display menu to the user.
    :return: n/a
    """
    print()
    print('Sports Menu')
    print('=' * 50)
    print('1 - List all Sports')
    print('2 - Add a Sport')
    print('3 - Delete a Sport')
    print('0 - Return to Main Menu')
    print()


def main_menu(students, next_student_id):
    """
    This function basically runs different functions from the validation module and the student_mtnc module, in a while
    loop, until the user decided that they no longer want to continue to use the program and exit.
    :return: n/a
    """

    while True:

        display_menu()

        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')
        if command == 1:
            list(students)
        elif command == 2:
            add(sports, next_student_id)
            next_student_id += 1
        elif command == 3:
            delete(sports)
        elif command == 0:
            return
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


def list_student_sports(students):
    """

    :param students:
    :return:
    """
    print(f'    Student ID # {student[0]} {student[1]} {student[2]} is in: ', end='')

    for sport in student[3]


def list_sports_option(valid_courses, mode='added'):
    print()


def add_student_sport(students, valid_courses):
    print()


def delete_student_sport(student, valid_courses):
    print()
    print(test)
    print(test)