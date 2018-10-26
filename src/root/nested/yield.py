students = []

def read_file():
    try:
        f=open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
        f.close()
    except Exception as e:
        print(e)

#create a function we can iterate in a for loop and creates a new line in the list

def read_students(f):
    for line in f:
        yield line
        
read_file()
print(students)
