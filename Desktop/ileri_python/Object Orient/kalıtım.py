
class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person nesnesi oluşturuldu")
class Student (Person):
    
    pass


class Teacher (Person):
    
    pass

p1=Person("Ali","Veli",30)
print(p1.name,p1.surname,p1.age)
s1=Student("Ayşe","Fatma",20)