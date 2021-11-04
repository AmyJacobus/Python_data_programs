#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

# Authorship
__author__ = 'Amy and Caleb'
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
    print('Student Menu')
    print('=' * 50)
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Update a student')
    print('0 - Exit program')
    print()


def list(students):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.
    :param students: This will pull in the students list into the function, in order to be used in the statements
    in the function.
    :return:  no value
    """
    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    print()
    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-'*4, '_'*20, '_'*20)

    for student in students:
        print(f'{student[0]:4d}  {student[1]:20s} {student[2]:20s}')

    print()


def add(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.
    :param students: Passing the students list to the function
    :param next_student_id: Passing the next_student_id to the function
    :return: no value
    """
    print()
    print('Add Student')
    print('_' * 50)

    first_name = v.get_string(prompt='Please enter the student\'s First Name').title()
    last_name = v.get_string(prompt='Please enter the student\'s Last Name').title()
    print()

    students.append([next_student_id, first_name, last_name])

    print(f'Student ID #{next_student_id} {first_name} {last_name} was added.')


def find_student_index(students, student_id):
    """
    Basically this function locates the student index based on the user ID input
    :param students: Passing the student list to the function
    :param student_id: Passing the student_id to the function
    :return: -1 to the program to other functions can use it
    """
    for student in students:
        if student_id in student:
            return students.index(student)

    return -1


def delete(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.
    It will then prompt the user for a valid student ID to be deleted from the 2D list
    It handles for non numeric data, and student IDs that do not exists via the find_student_index
    It will prompt the user to confirm they want to delete the selected student, and then let the user know
    if the user was successfully deleted.
    :param students: Passing the student list to this function, so it can be used in the different statements in the
    function
    :return: no value
    """
    print()
    print('Delete Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    student_id = v.get_positive(prompt='Please enter the Student ID you would like to delete', limit=0)

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index]  # I have the student now

    confirm = v.get_yes_no(prompt=f'Please confirm that you want to delete student ID # {student_id}'
                                  f' {student[1]} {student[2]} (y=yes, n=no): ')

    if confirm in ['y', 'yes']:
        student = students.pop(student_index)
        print(f'Student ID # {student_id} {student[1]} {student[2]} was deleted.')
    else:
        print('Delete was cancelled!')


def update(students):
    """
    It will first check to see if there is any student data, and notify the user if no data is found.
    It will then prompt the user for a valid student ID to be updated from the 2D list.
    It handles for non numeric data, and student IDs that do not exists via the find_student_index.
    It will prompt the user to confirm they want to update the selected student, and then let the user know
    if the user was successfully updated.
    :param students: Passing the student list to this function, so it can be used in the different statements in the
    function
    :return: no value
    """

    print()
    print('Update Student')
    print('_' * 50)

    if len(students) == 0:
        print("There are no students in the database.\n")
        return

    student_id = v.get_positive(prompt='Please enter the Student ID you would like to update', limit=0)

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID #{student_id} not found.')
        return

    student = students[student_index]  # I have the student now

    confirm = v.get_yes_no(prompt=f'Please confirm that you want to update the student ID# {student_id}'
                                  f' {student[1]} {student[2]} (y/n): ')

    og_name = students[student_index][1]
    og_last_name = students[student_index][2]

    if confirm in ['y', 'yes']:
        new_name = input(f'Please enter the Students First Name or press ENTER to keep {student[1]}: ')
        new_last_name = input(f'Please enter the Students First Name or press ENTER to keep {student[2]}: ')

        if new_name == '':
            print(f'No changes where made to ID #{student_id} first name.')
        else:
            students[student_index][1] = new_name

        if new_last_name == '':
            print(f'No changes where made to ID #{student_id} last name.')
        else:
            students[student_index][2] = new_last_name

        if new_name == '' and new_last_name == '':
            print('You did not type in anything, no changes were made.')
        else:
            print(f'Student ID # {student_id} {og_name} {og_last_name} was updated to '
                  f'{students[student_index][1]} {students[student_index][2]}.')
    else:
        print('Update was cancelled')


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
            add(students, next_student_id)
            next_student_id += 1
        elif command == 3:
            delete(students)
        elif command == 4:
            update(students)
        elif command == 0:
            print()
            print('=' * 50)
            print("You have securely and successfully exited the student record database!")
            exit()
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main_menu()  # Run this specific program.