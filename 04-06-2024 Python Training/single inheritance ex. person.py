class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def speak(self,hobbie):
        print(f"Hi my name is {self.name} and my age is {self.age} and my hobbies are {hobbie}")
        

Sash=Person("Sasankan","26")
Sri=Person("Srilekha","20")

#Sash.speak()
#Sri.speak()

Sash.speak("singing,listening music")
