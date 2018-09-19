'''
Created on 29.05.2018

@author: tpilz
'''
from test.test_decimal import file

students = []

            
def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title());
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)
    
def add_student(name, student_id=-1):
    student = {"name" : name,  "student_id" : student_id}
    students.append(student)
    
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception as e:
        print("There is an exception with saving a student: ", e)
        
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception as e:
        print("There is an exception with reading a student: ", e)

def enter_students():
    while input("Would you like to add another student? Please type yes or no: ") == "yes":
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        add_student(student_name, student_id)
        save_file(student_name)
    
    for student in students:
        print("Student number {0} is {1} and his ID is {2}".format(students.index(student)+1, student["name"].title(), student["student_id"]))              
            
read_file()
print_students_titlecase()
enter_students()


#student_list = get_students_titlecase() 
#add_student(student_name, student_id)
#print_students_titlecase()
