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
    print('Student Records Report')
    print('=' * 50)
    print('1 - List all students report')
    print('2 - List select student\'s report')
    print('3 - Delete a student\'s complete report')
    print('0 - Return to Main Menu')
    print()


def selected_student_data():
    print('Display data for a selected student')

def all_students_data():
    print('Display data for all students in the database')


def main_menu():
    print('In here we test and display everything!')


if __name__ == "__main__":  # Basically if the name of the module is equal to main
        main_menu()  # Run this specific program.