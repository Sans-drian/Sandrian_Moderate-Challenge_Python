class Person:
    #initiallizer
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    #getter functions
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    #setter function
    def setAddress(self, address):
        self.address = address

    #string function
    def __str__(self):
        return f"Their name is {self.name}, and their address is {self.address}"

class Student(Person):
    #initiallizer
    def __init__(self, numCourses = 0, courses = [], grades = []):
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def addCourseGrade(self, course, grade):
        self.course = course
        self.grade = grade

    #print grades    
    def printGrades(self):
        print (self.grade)
        
    #calculate the average grade
    def getAverageGrade(self):
        ave = sum(self.grade)/(self.numCourses)
        print(f"The average grade is {ave}")

    #print the student's credentials
    def __str__(self):
        return f"The student's name is {self.name}, and their address is {self.address}"


class Teacher(Person):
    #initiallizer
    def __init__(self, numCourses = 0, courses = []):
        self.numCourses = numCourses
        self.courses = courses

    #function for adding the course; checks whether input is the same in the list of courses or not, if yes, print out the text, if no, append.
    def addCourse(self, courses):
        if courses not in self.courses:
            self.course.append(courses)
        else:
            print ("The course you've inputted is already registered.")

    #function for removing a course; checks whether input is the same in the list of courses or not, if yes, remove from the list, if no, print text.
    def removeCourse(self, courses):
        if courses in self.courses:
            self.course.pop(courses)
        else:
            print ("That course does not exist.")
    
    #print the teacher's credentials
    def __str__(self):
        return f"The teacher's name is {self.name}, and their address is {self.address}"

