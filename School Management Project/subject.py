from person import Teacher
from school import School

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher # teacher er object thakbe
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students): # student = student der list
        for student in students:
            mark = self.teacher.evaluate_exam() # 1 theke 100 theke marking hoye jabe 1 ta student er jonno
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)