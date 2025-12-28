class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = [] # list of student objects
        self.subjects = [] # lsit of subjects objects

    def add_student(self, student): # student obj # rahim, eight e vorti hobe.
        roll_no = f'{self.name} - (len{self.students} + 1)' # student add korar sathe sathe tader roll update hobe. Ei line tar output : Eight(class name) - 1(student er roll), Eight - 2, ......
        student.id = roll_no
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semister_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()