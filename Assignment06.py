# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   Celia Louie, 11/19/2023, Created script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
--------------------------------------
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
menu_choice: str
students: list = []


# Processing
class FileProcessor:
    """
    A collection of processing layer functions that process a json file

    ChangeLog: (Who, When, What)
    Celia Louie,11.20.2023,Created class and functions
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
         This function reads in data from a json file into a table
         """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.")
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to the json file
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with writing to the file. \n "
                                             "Please check that the file is not open by another program.", error=e)
            if not file.closed:
                file.close()
        finally:
            if not file.closed:
                file.close()


# Presentation
class IO:
    """
    A collection of presentation layer functions that manager user input and output

    ChangeLog: (Who, When, What)
    Celia Louie,11.20.2023,Created class and functions
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function prints a custom error message
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu choices
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function takes in the user's input
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the registered students
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    def input_student_data(student_data: list):
        """
        This function takes the user input for student registration
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            students.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Input student data
        students = IO.input_student_data(student_data=students)
        continue
    elif menu_choice == "2":  # Display the registered students
        IO.output_student_courses(student_data=students)
        continue
    elif menu_choice == "3":  # Save data to json file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    elif menu_choice == "4":  # End the program
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

