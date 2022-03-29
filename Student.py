# Student Class - Defines the student object
from hashlib import new


class Student:

    grade = 0
    passing_score = 75
    award_credit = False


    #initializer sometimes called a constructor
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name.lower() + self.last_name.lower() + '@weber.edu'
        self.status = status

    def print_student_info(self):
        print('STUDENT:', self.first_name, self.last_name, 
        '\nEMAIL:', self.email, 
        '\nSTATUS', self.status,
        '\nPassing', self.award_credit)

    def set_grade(self, new_grade):
        self.grade = new_grade
        if (self.grade >= self.passing_score):
            self.award_credit = True
        if (self.grade < self.passing_score):
            self.award_credit = False

    
scott = Student('Scott','Hadzik','Full time') #scott is an instance of the Student class
camille = Student('Camille', 'Hadzik','Part time') #camille is an instance of the Student class

scott.set_grade(80)

print ('\n')
scott.print_student_info()
print ('\n')
camille.print_student_info()
print ('\n')