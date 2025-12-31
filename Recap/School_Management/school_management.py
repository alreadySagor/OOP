import random

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom): # classroom er object ke parameter hisebe nilam
        self.classrooms[classroom.name] = classroom # classroom er naam ke key baniye dictionary te rakhe.

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher # kono ekti subject ke kon teacher porabe seta set korlam.
    
    def student_admission(self, student):
        class_name = student.classroom.name # student kon classroom er ta ber kora holo.
        self.classrooms[class_name].add_student(student) # Sei classroom object theke add_student() call kora holo.

    @staticmethod
    def calculate_grade(marks): # Example --> School.calculate_grade(85) → 'A+'
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
    def grade_to_value(grade): # Example --> 'A+' → 5.00
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
    def value_to_grade(value): # GPA value → Final grade
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
        
    def __repr__(self): # print(school) dile ei method call hoy.
        # All classrooms
        for key in self.classrooms.keys():
            print(key)
        
        print('All Students')
        result = ''
        for key,  value in self.classrooms.items(): # prottekta classroom e gelam
            result += f'---{key.upper()} Classroom Students\n' # ekekta class room er name show korbe
            for student in value.students:
                result += f'{student.name}\n' # ekekta classroom er under e jotogulo student ache tader name show korbe
        print(result)

        # All subjects
        subject = ''
        for key,  value in self.classrooms.items(): # prottekta classroom e gelam
            subject += f'---{key.upper()} Classroom Subjects\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject) 

        #------------------------------------------------
        print('All Teachers')
        teacher = ''
        for key, value in self.teachers.items():
            teacher += f'{key.upper()} : {value.name}\n'
        print(teacher)
        #------------------------------------------------

        print('Students Results')
        print('--------------------------------------------------------')
        for key, value in self.classrooms.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.calculate_final_grade())
                print('--------------------------------------------------------')
        return ''


class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student): # student object ashbe
        roll_no = f'{self.name} <-> len(self.students) + 1'
        student.id = roll_no
        self.students.append(student)
    
    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def take_semister_final_exam(self): # proti ta subject nije nije exam nibe.
        for subject in self.subjects:
            subject.exam(self.students)
        
        for student in self.students:
            student.calculate_final_grade()


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.min_marks = 33

    def exam(self, students): # student = student er list
        for stdnt in students:
            mark = self.teacher.evaluate_exam()
            stdnt.marks[self.name] = mark # student.marks dict e save hoy
            stdnt.subject_grade[self.name] = School.calculate_grade(mark) # grade hiseb kore save hoy

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(50, 100)
    
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
    
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)
        return f'{self.name} Final Grade : {self.grade} with GPA = {gpa}'
    
    @property # example of encapsulation
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

#-------------------------------------------------------------------------

school = School('ABC', "Dhaka")

# Adding Classroom
eight = Classroom('Eight')
nine = Classroom('Nine')
ten = Classroom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# Adding Student
rahim = Student('Rahim', eight)
karim = Student('Karim', nine)
fahim = Student('Fahim', ten)
hamim = Student('Hamim', ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# Adding Teachers
abul = Teacher('Abul Khan')
babul = Teacher('Babul Khan')
kabul = Teacher('Kbul Khan')

school.add_teacher('bangla', abul)
school.add_teacher('physics', babul)
school.add_teacher('chemistry', kabul)

# Adding Subjects
bangla = Subject('Bangla', abul)
physics = Subject('Physics', babul)
chemistry = Subject('Chemistry', kabul)
biology = Subject('Biology', kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(chemistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(biology)

eight.take_semister_final_exam()
nine.take_semister_final_exam()
ten.take_semister_final_exam()
print(school)

"""
Architecture of this code...

School
 ├── Classroom
 │    ├── Student
 │    └── Subject ── Teacher

"""

# comment