import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(50, 100) # jotil kono kichu korini, ekjon teacher 50 theke 100 er moddhe jekono number ekjon student er exam er jonno set korbe
    

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom # classroom object
        self.__id = None
        self.marks = {} # {"eng" : 78, "Ict": 90}
        self.subject_grade = {} # {"Eng": 'A', "math": 'A+'}
        self.grade = None # final grade
        
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values(): # ekhane value bolte jeta bojhano hoyeche ({"Eng" (key) : 'A' (Value), "math": 'A+'}) mane english subject er grade A ke bojhano hoyeche. ({"eng" : 'A'} eta hocche key, value pair)
            point = School.grade_to_value(grade) # 'A'dile 4.00 dibe
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade) # 7 / 2 = 3.50
            self.grade = School.value_to_grade(gpa) # 3.50 dile 'A-' dibe
        return f'{self.name} Final Grade : {self.grade} with GPA = {gpa}'
    #getter
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value