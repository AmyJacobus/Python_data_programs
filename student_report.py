"""
# Programmer: Caleb Fowler and Ammishaddai Jacobus
# Date: Nov 10, 2021
# Description:   STILL NEED DESCRIPTION HERE
"""


#Imports come here



# the following are module level dunders (metadata) for the authorship information
__author__ = 'Caleb Fowler & Amy Jacobus'
__version__ = '1.0'
__date__ = '2021.11.02'
_status__ = 'Development'


def display_menu():
    print('Student Records Report Menu')
    print('=' * 50)
    print('1 - List all students report')
    print('2 - List select student\'s report')
    print('3 - Delete a student\'s complete report')
    print('0 - Return to Main Menu')
    print()


def selected_student_data():
    print('Display data for a selected student')


def all_students_data(students):

    print('Report of all students in the database')

    if len(students) == 0:
        print('There are no students in the list.')
        return

    print(f'{"ID":>4s} {"First Name":<15s} {"Last Name":<15s} {"Courses":<43s} {"sports":<43s}')
    print('=' * 4, '=' * 15, '='*15, '=' * 34,'=' * 34 )

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:>4d} {first_name:<15s} {last_name:<15s}', end='')

        for course in courses:
            print(f'{course}', end=', ')
        print(f'{" ":<15s}', end='')

        for course in courses:
            print(f'{course}', end=', ')
        print()

    return


def main_menu():

    valid_courses = ('English', 'History', 'Math', 'Science')
    valid_sports = ('Football', 'Volleyball', 'Basketball', 'Track')

    students = [
        [1, 'John', 'Doe', ['English', 'Science'], ['Volleyball']],
        [3, 'Sam', 'Smith', ['English', 'History', 'Math'], ['Football', 'Basketball']]
    ]
    print('In here we test and display everything!')
    all_students_data(students)


if __name__ == "__main__":  # Basically if the name of the module is equal to main
        main_menu()  # Run this specific program.