'''
Created on 26.10.2018

@author: tpilz
'''
students = []

class Student:
    
    #no access modifiers
    school_name = "Springfield"
    
    def __init__(self, name, student_id=-1):
        self.name = name
        self.student_id = student_id
        students.append(self)
        
    def __str__(self):
        return "Student " + self.name
    
    def get_name_capitalized(self):
        return self.name.capitalize()
    
    # _get_school_name / underscore to say method should not be overriden or used directly 
    def get_school_name(self):
        return self.school_name

'''
mark = Student("Mark")

print(students)
print(mark)

print(mark.get_school_name())
print(Student.school_name)
'''
   
class HighSchoolStudent(Student):
    
    school_name = "Washington"
    
    def get_school_name(self):
        return "This is a highschool student"
    
    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"
    
james = HighSchoolStudent("james")
print(james.get_name_capitalized())
print(james.get_school_name())





