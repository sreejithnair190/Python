#Class Attributes and Methods

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_people(cls):
        cls.number_of_people += 1


p1 = Person("Sreejith")
print(p1.number_of_people)
#p1 object don't have number_of_people but the class of the object has one so its actually Person.number_of_people

p2 = Person("Prince")
print(p2.number_of_people)

p3 = Person("Satya")
print(p3.number_of_people)

p4 = Person("Stebin")
print(p4.number_of_people)


