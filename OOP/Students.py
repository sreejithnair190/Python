class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, course_name, max_students):
        self.name = course_name
        self.max_students =  max_students
        self.students = []

    def add_students(self,student):
         if len(self.students) < self.max_students:
             self.students.append(student)
             return True
         return False

    def get_average_score(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            average = total/len(self.students)
        return(average)

s1 = Student("Sreejith", 21, 95)
s2 = Student("Prince", 21, 85)
s3 = Student("Stebin", 21, 65)
s4 = Student("Satya", 22, 75)

course = Course("Msc CS", 4)

course.add_students(s1)
course.add_students(s2)
course.add_students(s3)
course.add_students(s4)

print(course.get_average_score())

