class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str: # class take represent korte chaile
        return f'Student with name: {self.name}, class : {self.current_class}, id : {self.id}'

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, subject : {self.subject}, id : {self.id}'

# এখানে ২ টা ক্লাস এর মধ্যেই যেই __repr__ মেথড ব্যবহার করা হয়েছে এটা ক্লাস অবজেক্ট এর স্ট্রিং রিপ্রেজেন্টেশন দিবে 
# অর্থাৎ আমরা যদি Teacher ক্লাস এর অবজেক্ট এর প্রিন্ট করি তাহলে এটা এই মেথড এর মধ্যে যেই স্ট্রিংটা রিটার্ন করা
# হচ্ছে সেই অনুযায়ী আউটপুট প্রিন্ট করবে 

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
        
    def __repr__(self):
        print('welcome to', self.name)
        print('-------------- OUR Teachers ---------------')
        for teacher in self.teachers:
            print(teacher)
        print('---------- OUR Students ------------')
        for student in self.students:
            print(student)
        return 'All done for now'
    
# alia = Student('Alia', 9, 1)
# ranbir = Teacher('Ranbir', 'Romance', 420)
# print(alia)
# print(ranbir)

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'DS')
phitron.add_teacher('Chris Hemsworth', 'Algorithm')
phitron.add_teacher('Robert Downey Jr', 'Database')

print(phitron)