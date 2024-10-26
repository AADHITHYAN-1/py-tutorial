
#public
'''class vehical:
    def bike(self):
        print("this is bike")
    def car(self):
        print("this is car")
    def motor(self):
        print("this is motor")
obj=vehical()
obj.bike()
obj.car()
obj.motor()'''



#privite(__is the privite)u can privite mathod  __ is to convot privite after to can public change (self.__method name)
#protected(_ single under core)

'''class vehical:
    def bike(self):
        self.__car()
        self._motor() 
        print("this is bike")
    def __car(self):
        print("this is car")  
    def _motor(self):
        print("this is motor")
obj=vehical()
obj.__car()

'''


#polymorphism

'''class animal():
    pass
class dog(animal):
    def sound(self):
        print("dog braks")
class cat(animal):
    def sound(self):
        print("cat mews")
class brids(animal):
    def sound(self):
        print("brids is singing")
animal=[dog(),cat(),brids()]
for animal in animal:
    animal.sound()







class animal():
    pass
class dog(animal):
    def sound(self):
        print("dog braks")
class cat(animal):
    def sound(self):
        print("cat mews")
class brids(animal):
    def sound(self):
        print("brids is singing")
animal=[dog(),cat(),brids()]
for animal in animal:
    animal.sound()
'''
