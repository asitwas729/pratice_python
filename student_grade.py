class Student:
    def __init__(self, name, password):
        self.name = name
        self.scores = {}
        self.password = password
    def view_grade(self):
        print(self.scores)

class Teacher:
    def __init__(self, name, password, subject):
        self.name = name
        self.password = password
        self.subject = subject
    def set_score(self, student, score):
        student.scores[self.subject] = score
    def avg(self):

        print()

s1 = Student("s1", "1234")
t1 = Teacher("국어쌤","1234","국어")
t2 = Teacher("영어쌤","1234","영어")
t3 = Teacher("수학쌤","1234","수학")

t1.set_score(s1, 90)
t2.set_score(s1, 60)
t3.set_score(s1, 70)

s1.view_grade()