from ModeratelyChallengeClass import Person, Student, Teacher

def register():
    list = []
    
    name = input("Name: ")
    address = input("Address: ")

    print(list.append(Person(name, address)))
    return list     
   

register()