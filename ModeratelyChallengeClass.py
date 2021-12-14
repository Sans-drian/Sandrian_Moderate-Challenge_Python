class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __str__(self):
        return f"Their name is {self.name}, and their address is {self.address}"

class Student(Person):
    def __init__(self, numCourses = 0, courses = [], grades = []):
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def addCourseGrade(self, course, grade):
        self.course = course
        self.grade = grade

    def printGrades(self):
        print (self.grade)

    def getAverageGrade(self):
        ave = sum(self.grade)/(self.numCourses)
        print(f"The average grade is {ave}")

    def __str__(self):
        return f"The student's name is {self.name}, and their address is {self.address}"


class Teacher(Person):
    def __init__(self, numCourses = 0, courses = []):
        self.numCourses = numCourses
        self.courses = courses

    def addCourse(self, courses):
        if courses not in self.courses:
            self.course.append(courses)
        else:
            print ("The course you've inputted is already registered.")

    def removeCourse(self, courses):
        if courses in self.courses:
            self.course.pop(courses)
        else:
            print ("That course does not exist.")
        
    def __str__(self):
        return f"The teacher's name is {self.name}, and their address is {self.address}"

