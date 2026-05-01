class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
    
s1 = Student("Bob", 1001)
s2 = Student("Jon", 1100)

print(s1.name, s1.id)
print(s2.name, s2.id)