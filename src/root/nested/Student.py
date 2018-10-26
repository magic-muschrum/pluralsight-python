'''
Created on 26.10.2018

@author: tpilz
'''

class Student(object):
    '''
    classdocs
    '''

    school_name = "Springfield"

    def __init__(self, name, student_id=-1):
        '''
        Constructor
        '''
        self.name = name
        self.student_id = student_id
    
    def __str__(self):
        return "Student" + self.name
    
    
    def get_name_capitalized(self):
        return self.name.capitalize()
    
    # _get_school_name / underscore to say method should not be overriden or used directly 
    def get_school_name(self):
        return self.school_name