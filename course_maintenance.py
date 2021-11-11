#!/usr/bin/env python3

"""
Programmers: Programmer: Caleb Fowler and Ammishaddai Jacobus
Date: Nov 10, 2021
Description:  This module basically stores student records. It can add students courses, it can update the courses for
each student,it can delete courses for each student, and you can also check for all the courses that a student is enrolled
in, or check all the students and all the courses they all are enrolled in. It outputs all the data information in a
nicely formatted report.
"""

import validation as v
import student_maintenance as sm

# Authorship
__author__ = 'Caleb Fowler and Ammishaddai Jacobus'
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


def list_student_courses(student):
    """
    This function displays one specific students in the database with their enrolled courses.
    :param student: Takes the parameter student to have access to this specific student data to be used in this
    function.
    :return:
    """

    print(f'       Student ID # {student[0]} {student[1]} {student[2]} is in: ', end='')

    for course in student[3]:
        print(f'{course}', end=', ')

    print()


def list_students_courses(students):
    """
    This function first checks is there are students in the database, if not, it will tell the user that there are no
    students in the database. And if there are students, it will display a full report of all the students in
    the database with their courses that they are enrolled in. Output is displayed in a nicely formatted report.
    :param students:
    :return:
    """

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


def list_valid_courses(valid_courses, mode='added'):
    """
    This function displays the valid courses that a student can enrolled in, it outputs the valid courses with a number
    assigned to each.
    :param valid_courses: It takes the list valid_courses to be used in this function.
    :param mode: This is a mode that stores a string, that basically can be used in other functions if they choose to
     use this function.
    :return: num_courses so other functions or modules can make use of it
    """

    print(f'Pleases select from the following list of courses to be {mode}:')

    num_courses = 0

    print('    ', end='')
    for course in valid_courses:
        num_courses += 1
        print(f'{num_courses}={course}', end=', ')
    print('0=Done')

    return num_courses


def add_student_course(students, valid_courses):
    """
    This function displays the message of add student courses to let the user know they are in that section of the menu.
    It takes the user input of the student ID, basically the student they want to add a course to, it validates
    their input (checks if its positive), gets the user student out of the student list, to access that student's information.
    It lists the valid courses that you can add for that students, it asks what courses the user wants to add for the
    student, and validates their input on that, and adds the courses, it also outputs the updated information to
    let the user know what they have updated exactly.
    :param students: It takes the parameter students, to be able to make use of the students list in this function.
    :param valid_courses: It takes the parameter students, to be able to make use of the valid courses in this function.
    :return: n/a
    """

    print('Add student courses')
    print('='*50)

    student_id = v.get_positive(prompt='Please type in the ID # of the student you would like to add courses'
                                       'for', limit=0)

    # NEEDS TO BE CHECKED
    student_index = sm.find_student_index(students,student_id)
    if student_index == -1:
        print('Not found')
        return

    student = students[student_index] # I have the student now

    #
    print(f'Student ID # {student[0]} is enrolled in the following courses:')
    list_student_courses(student)

    #
    print('These are the following courses that the student can select from: ')
    list_valid_courses(valid_courses, mode='added')

    while True:

        course_number = v.get_range(prompt='What course number would you like to add: ', low=0, high=5)
        if course_number == 0:
            break

        course_name = valid_courses[course_number-1]  # get the course name for the valid tuple

        if course_name in student[3]:
            print(f'The student is already enrolled in {course_name}.')
            continue
        else:
            student[3].append(course_name) # add the course name to the student's list
            student[3].sort() # sort the student's course list
            print(f'Student is now enrolled in {course_name}')
            break

    # Display what courses the student is current enrolled in by calling list_student_courses passing
    # only the selected student's data'
    list_student_courses(student)


def delete_student_course(students, valid_courses):
    """
    THis function basically helps the user delete courses for a specific student. It takes the user input of the
    student they would like to delete a course for, validates that, to make sure the ID input is a positive number,
    gets the specific student based of that ID input, it displays what courses this student is currently enrolled in,
    it then display the list of valid courses for the user to see, gives the user the chance to type in a course they
    want to delete or press 0 to not make any changes to this student courses. And if the user does go through
    with making changes, basically the user will get an update information to let them know that the changes were made,
    and what changes were made exactly.
    :param students: THis function takes the parameter students, to make use of it in this function to run certain statements.
    :param valid_courses: THis function takes the parameter students, to make use of it in this funciton to run certain statements.
    :return: n/a
    """

    print()
    print('Delete Courses')
    print('_' * 50)

    student_id = v.get_positive(prompt='Please type in student id: ', limit=0, data_type='int')

    student_index = sm.find_student_index(students,student_id)
    if student_index == -1:
        print('Not found')
        return

    student = students[student_index]  # I have the student now

    # Display a list of courses a student is currently enrolled in
    print(f'Student ID # {student[0]} is enrolled in the following courses:')
    list_student_courses(student)

    # Display a list of valid courses
    # print('These are the following courses that can be deleted: ')

    num_courses = list_valid_courses(student[3], mode='delete')

    while True:

        # Prompt the user to enter a valid course id or 0 to return to the course maintenance menu
        print('Please type in a valid course ID or 0 to return to course maintenance menu')
        choice = v.get_range(prompt='input: ', low=-1, high=num_courses)

        if choice == 0:
            print('Returning you back to the course maintenance menu')
            break

        choice -= 1
        course_choice = student[3][choice]

        if course_choice not in student[3]:
            print('There has been an error.')

        else:
            student[3].remove(course_choice)
            print('This is an update list of all the courses the student is enrolled in.')
            list_student_courses(student)
            break


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
            list_students_courses(students)
        elif command == 2:
            add_student_course(students, valid_courses)
        elif command == 3:
            delete_student_course(students, valid_courses)
        elif command == 0:
            print('Exiting the course maintenance now..')
            print('You have successfully exited the course maintenance.')
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main_menu()  # Run this specific program.