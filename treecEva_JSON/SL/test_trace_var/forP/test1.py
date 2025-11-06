class Score:
    def __init__(self, math, english):
        self.math = math
        self.english = english

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

score = Score(95, 88)
student = Student("Alice", 18, score)
final = student.score.math + 5
print(final)