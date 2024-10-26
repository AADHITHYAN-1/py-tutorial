'''def add(a,b,c=0):
    print(a+b+c)
add(10,20)
add(10,20,10)'''




'''class animal():
    def sound(self):
        print("animal makes sound")

class dog(animal):
    def sound(self):
        print("dog braks")
class brid(animal):
    def sound(self):
        print("brid sing")
    
a1=brid()
a1.sound()'''


'''class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)
obj=rectangle()
obj.area()'''
        
    

'''class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def dis(self):
        print(self.name,self.grade)

obj=student("aadhi","22")
obj.dis()'''



        
'''class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print('car started')
obj=vehicle()
obj.start()
'''




'''class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,depertant):
        super().__init__(name,salary)
        self.depertant=depertant
        
    def display(self):
        print(self.name,self.salary,self.depertant)
obj=manager("aadhi","2333","bsc")
obj.display()'''





'''class fun():
    def poly(self,*args):
        ans=0
        for i in args:
            ans+=i
        return ans
fun1=fun()
print(fun1.poly(1,2,3,4,5))'''



'''class a1:
    def sound(self):
        print("sound")
class a2(a1):
    def sound(self):
        print("cat")
class a3(a1):
    def sound(self):
        print("dog")

ani=a1()
c=a2()
b=a3()
ani.sound()
c.sound()
b.sound()'''



class f1():
    def money(self):
        print("have money")
class f2(f1):
    def mobile(self):
        super().money()
        print("have a phone")
class f3():
    def lap(self):
        print("have a lap")

obj1=f2()
obj1











        
