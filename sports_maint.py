#!/usr/bin/env python3

"""
Programmers: Programmer: Caleb Fowler and Ammishaddai Jacobus
Date: Nov 10, 2021
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
    print('1 - List all students sports')
    print('2 - Add a student\'s sport')
    print('3 - Delete a student\'s sport')
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
            display_list_valid_sports()
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


def list_student_sports(student):
    """

    :param student:
    :return:
    """
    print(f'    Student ID # {student[0]} {student[1]} {student[2]} is in: ', end='')

    for sport in student[3]:
        print(f'{sport}', end=', ')

    print()


def list_valid_sports(valid_sports, mode='added'):
    """
    :param valid_sports:
    :param mode:
    :return:
    """
    print(f'Please select from the following list of sports to be {mode}:')

    num_sports = 0

    print('   ', end='')
    for sport in valid_sports:
        num_sports += 1
        print(f'{num_sports}={sport}', end=', ')
    print('0=Done')

    return num_sports


def add_student_sport(students, valid_sports):
    print()
    print('Add a Student\'s Sport')
    print('_' * 50)

    first_name = v.get_string(prompt='Please enter the student\'s First Name').title()
    last_name = v.get_string(prompt='Please enter the student\'s Last Name').title()
    print()

    students.append([next_student_id, first_name, last_name])

    print(f'Student ID #{next_student_id} {first_name} {last_name} was added.')


def delete_student_sport(student, sports):
    print()
    print(test)
    print(test)
