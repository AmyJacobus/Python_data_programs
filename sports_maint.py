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
import student_maintenance as sm


def display_menu():
    """
    Display menu to the user.
    :return: n/a
    """
    print()
    print('Sports Menu')
    print('=' * 50)
    print('1 - List all student\'s sports')
    print('2 - Add a student\'s sport')
    print('3 - Delete a student\'s sport')
    print('0 - Return to Main Menu')
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
    print('Add student sports')
    print('=' * 50)

    student_id = v.get_positive(prompt='Please type in the ID # of the student you would like to add sports'
                                       ' for', limit=0)

    student_index = sm.find_student_index(students, student_id)
    if student_index == -1:
        print('Not found')
        return

    student = students[student_index]  # I have the student now

    #
    print(f'Student ID # {student[0]} is enrolled in the following courses:')
    list_student_sports(student)

    #
    print('These are the following sports that the student can select from: ')
    list_valid_sports(valid_sports, mode='added')

    while True:

        sport_number = v.get_range(prompt='What sport number would you like to add: ', low=0, high=5)
        if sport_number == 0:
            break

        sport_name = valid_sports[sport_number - 1]  # get the course name for the valid tuple

        if sport_name in student[3]:
            print(f'The student has already selected {sport_name}.')
            continue
        else:
            student[3].append(sport_name)  # add the course name to the student's list
            student[3].sort()  # sort the student's sport list
            print(f'The student is now in {sport_name}')
            break

    # Display what courses the student is current enrolled in by calling list_student_courses passing
    # only the selected student's data'
    list_student_sports(student)


def delete_student_sport(students, valid_sports):
    print()
    print('Delete Students\'s Sports')
    print('_' * 50)

    student_id = v.get_positive(prompt='Please type in student id: ', limit=0, data_type='int')

    student_index = sm.find_student_index(students, student_id)
    if student_index == -1:
        print('Not found')
        return

    student = students[student_index]  # I have the student now

    # Display a list of courses a student is currently enrolled in
    print(f'Student ID # {student[0]} is in the following sports:')
    list_student_sports(student)

    # Display a list of valid sports
    print('These are the following sports that can be deleted: ')
    list_valid_sports(student[3], mode='delete')

    # Prompt the user to enter a valid sport id or 0 to return to the sport maintenance menu
    print('Please type in a valid sport ID or 0 to return to sports maintenance menu')
    choice = v.get_range(prompt='input: ', low=0, high=5)

    while True:

        if choice == 0:
            print('Returning you back to the sports maintenance menu')
            break

        sport_choice = valid_sports[choice-1]

        if sport_choice not in student[3]:
            print('There has been an error.')
        else:
            student[3].remove(sport_choice)

    print('This is an update list of all the sports the student is in.')
    list_student_sports(student)


def main_menu(students, next_student_id):
    """
    This function basically runs different functions from the validation module and the student_mtnc module, in a while
    loop, until the user decided that they no longer want to continue to use the program and exit.
    :return: n/a
    """

    valid_sports = ('Football', 'Volleyball', 'Basketball', 'Track')

    students = [
        [1, 'John', 'Doe', ['English', 'Science'], ['Volleyball']],
        [3, 'Sam', 'Smith', ['English', 'History', 'Math'], ['Football', 'Basketball']]
    ]

    next_student_id = 4

    while True:

        display_menu()

        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')
        if command == 1:
            list_student_sports(students)
        elif command == 2:
            add_student_sport(students, valid_sports)
        elif command == 3:
            delete_student_sport(students, valid_sports)
        elif command == 0:
            return
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main_menu()  # Run this specific program.

