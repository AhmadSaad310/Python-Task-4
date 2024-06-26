class Student:
    def __init__(self,name,course):
        self.names=[]
        self.courses=[]
        print (f'{name} {course}')
    def enroll (self,name_of_course):
        self.courses.append(name_of_course)
        print ('Hallo')
    def get_courses (self):
        return self.courses
student=Student ('Ahmad','Mathe')
student.enroll('Mathe')
print (student.get_courses())

