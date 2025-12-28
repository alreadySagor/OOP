"""
Docstring for school

{} eta dictionary ke represent kore
[] eta list ke represent kore
"""
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {"Bangla" : teacher_object} # ei format e data gula rakhte chai
        self.classrooms = {} # {"Eight": classroom object}
    
    def add_classroom(self, classroom): # classroom er obj ke nilam
        # classrooms dictionary te ekti class er under e[suppose : eight] classroom object ke rekhe dilam
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self, subject, teacher): # teacher object
        self.teachers[subject] = teacher
    
    def student_admission(self, student): # student object
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)
    
    # ei static method ta ekta class er shoyong nijossho method, eta kokhonoi object ba instance use korte parbena
    @staticmethod
    def calculate_grade(marks): # marks ta input hisebe nibo
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks <= 79:
            return 'A'
        elif marks >= 60 and marks <= 69:
            return 'A-'
        elif marks >= 50 and marks <= 59:
            return 'B'
        if marks >= 40 and marks <= 49:
            return 'C'
        elif marks >= 33 and marks <= 39:
            return 'D'
        elif marks < 33:
            return 'F'
        else:
            return f'Envalid Marks!!'
    
    @staticmethod
    def grade_to_value(grade): # grade ta input hisebe nibo
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return 'A+'
        elif value >= 4.00 and value < 5.00:
            return 'A'
        elif value >= 3.50 and value < 4.00:
            return 'A-'
        elif value >= 3.00 and value < 3.50:
            return 'B'
        elif value >= 2.00 and value < 3.00:
            return 'C'
        elif value >= 1.00 and value < 2.00:
            return 'D'
        elif value > 0.00 and value < 1.00:
            return 'F'
        else:
            return f'Invalid Input!!'
        
    def __repr__(self):
        # All classrooms
        for key in self.classrooms.keys():
            print(key)
        print('All Students')
        result = ''
        for key,  value in self.classrooms.items(): # prottekta classroom e gelam
            result += f'---{key.upper()} Classroom Students\n' # class room er name show korbe
            for student in value.students:
                result += f'{student.name}\n' # classroom er under e jotogulo student ache tader name show korbe
        print(result)

        # All subjects
        subject = ''
        for key,  value in self.classrooms.items(): # prottekta classroom e gelam
            subject += f'---{key.upper()} Classroom Subjects\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject)

        # All Teachers -- homework

        print('Students Results')
        for key, value in self.classrooms.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''