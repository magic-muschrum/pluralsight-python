'''
Created on 26.10.2018

@author: tpilz
'''

from nested.Student import Student

class HSStudent(Student):
    '''
    classdocs
    '''

    school_name = "Washington"


    def __init__(self, name, student_id=-1):
        '''
        Constructor
        '''
        self.name = name
        self.student_id = student_id
        
    def get_school_name(self):
        return self.school_name
    
    def get_name_capitalized(self):
        original_value = super().get_name_capitalized()
        return original_value + "-HS"        