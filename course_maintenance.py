#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

import validation as v
import student_maintenance as sm

# Authorship
__author__ = 'ADD NAMES HERE'
__version__ = '1.0'
__date__ = 'NOV 2, 2021'
__status__ = 'Development'


def display_menu():
    """
    Display menu to the user.
    :return: n/a
    """
    print()
    print('Student Menu')
    print('=' * 50)
    print('1 - List all courses')
    print('2 - Add a course')
    print('3 - Delete a course')
    print('0 - Exit Program')
    print()


def main_menu(students, valid_courses):
    """
    This function basically runs different functions from the validation module and the student_mtnc module, in a while
    loop, until the user decided that they no longer want to continue to use the program and exit.
    :return: n/a
    """

    while True:

        display_menu()

        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')
        if command == 1:
            list_student_courses(students)
        elif command == 2:
            add_student_course(students, valid_courses)
           valid_courses += 1
        elif command == 3:
            delete_student_course(students, valid_courses)
        elif command == 0:
            exit()
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


def list_student_courses(students):

    if len(students) == 0:
        print('There are no students in the list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s} {"Courses":<43s}')
    print('=' * 4, '=' * 15, '='*15, '=' *34)

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:>4d} {first_name:<15s} {last_name:<15s}', end='')

        for course in courses:
            print(f'{course}', end=', ')
        print()

    return

def list_courses_option(valid_courses, mode='added'):
    """

    :param valid_courses:
    :param mode:
    :return: num_courses so other functions or modules can make use of it
    """

    print(f'Pleases select from the following list of courses to me {mode}:')

    num_courses = 0

    print('    ', end='')
    for course in valid_courses:
        num_courses += 1
        print(f'{num_courses}={course}', end=', ')
    print('0=Done')

    return num_courses


def add_student_course(students, valid_courses):

    print('Add student courses')
    print('='*50)

    student_id = v.get_positive(prompt='Please type in the ID # of the student you would like to add courses'
                                       'for', limit=0)

    # NEEDS TO BE CHECKED
    student_index = sm.find_student_index(student_id)
    if student_index == -1:
        print('Not found')
        return

    student = students[student_index] # I have the student now

    #
    print(f'Student ID # {student[0]} is enrolled in the following courses:')
    list_student_courses(student)

    #
    print('These are the following courses that the student can select from: ')
    list_courses_option('WHAT TO PUT IN HERE')

    while True:

        course_number = v.get_range(prompt='What course number would you like to add: ', low=0, high=4)
        if course_number == 0:
            break

        if (the course name already in the student's list of courses')
            print('display message already in course name')
        else:
            students.append([]) # add the course name to the student's list
            # sort the student's course list'
            print('Student is now in the course name.')
    # Display what courses the student is current enrolled in by calling list_student_courses passing
    # only the selected student's data'

    print(f'Student ID # {} is enrolled in the following courses: {}')



def delete_student_course(students, valid_courses):

    print()
    print('Delete Courses')
    print('_' * 50)

    student_id = v.get_positive(prompt='Please type in student id: ', limit=0, data_type='int')

    # Display a list of courses a student is currently enrolled in
    # Display a list of valid courses

    # Prompt the user to enter a valid course id or 0 to return to the course maintenance menu
    print('Please type in a valid course ID or 0 to return to course maintenance menu')
    choice = v.get_range(prompt='input: ', low=0, high=4)

    # If the student is not the select course, then display error message
        print("There has been an error.")
    # Else remove the course to the student's course list

    print('This is an update list of all the courses the student is enrolled in.')
    # display an update list here


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main_menu()  # Run this specific program.