'''
According to pep8 standard,
class names use PascalStyle

variable names are snake_case
'''

class Dog: 
    def __init__(self,initial_name,age=0):
        self.name = initial_name
        self.age = age
        self.x = 0
        self.y = 0

    def speak(self):
        print(self.name + " says Rrrrrrrrruuuffff!")

    def change_name(self,newname):
        self.name = newname

    def calculate_dog_years(self):
        return self.age * 7

    def walk(self,xdiff,ydiff):
        self.x += xdiff
        self.y += ydiff
    
    def fetch(self,ballx,bally):
        x = self.x
        y = self.y
        #store old position
        self.walk(x + ballx, y + bally)
        self.walk(x - ballx, y -bally)
        


    def celebrate_birthday(self):
        self.age +=1
        print("Happy birthday "+ self.name)

fido = Dog("fido",3) # should be 3
fido.speak()
fido.change_name("Remmy") 
fido.speak()

fido.fetch(5,6)

rex = Dog("rex") #should be 0
rex.speak()
fido.speak()



thor = Dog("thor") #should be 11
thor.speak()