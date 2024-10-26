
#single in

'''class ram():
    def product(self):
        print("music intruction")
class seetha(ram):
    def pro(self):
        print("beautiful")

L1=seetha()
L1.product()'''



'''class dad():
    def phone(self):
        print("dad phone")
class son(dad):
    def lap(self):
        print("son lap")

raj=son()
raj.phone()'''



#multi in

'''class raj():
    def lap(self):
        print("raj lap")
class arun():
    def ball(self):
        print("arun ball")
class aadhi(arun,raj):
    def phone(self):
        print("aadhi phone")

aadhi=aadhi()
aadhi.phone()
aadhi.ball()
aadhi.lap()'''




'''class dad():
    def phone(self):
        print("dad phone")
class mom():
    def sweet(self):
        print("mom sweet")
class son(dad,mom):
    def lap(self):
        print("son lap")

raj=son()
raj.phone()
raj.sweet()'''


#multilevel in
'''
class max():
    def van(self):
        print("max van")
class gwen(max):
    def magic(self):
        print("gwen magic")
class ben(gwen):
    def watch(self):
        print("ben watch")
ben=ben()
ben.watch()
ben.van()
'''


'''class freefire():
    def players(self):
        print("enjoyment")
class charater(freefire):
    def alok(self):
        print("helling")
class wepen(charater):
    def guns(self):
        print("attack")

play=wepen()
play.guns()
play.players()'''





#higyarakiyal in
'''
class sir():
    def teach(self):
        print("neew skill learning")
class student1(sir):
    pass

class student2(sir):
    pass

class student3(sir):
    pass

class student4(sir):
    pass

stu=student4()
stu.teach()'''




"""
class dad():
    def money(self):
        print("dad money")
class son1(dad):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

class son4(dad):
    pass


sonn=son4()
sonn.money()"""





#super key
'''class a():
    def __init__(self):
        print("its a")
    def dis(self):
        print("A")

class b():
    def __init__(self):
        super().__init__()
        print("its b")
    def dis(self):
        print("b")
        
class c(b,a):
    def __init__(self):
        super().__init__()
        print("its c")
    def dis(self):
        print("c")


c=c()'''




'''class r1():
    def __init__(self):
        print("use penet")
    def dis(self):
        print("PENUTS")
class r2():
    def __init__(self):
        super().__init__()
        print("see that r1")
    def dis(self):
        print("seeing")
class r3(r2,r1):
    def __init__(self):
        super().__init__()
        print("see all")
    def dis(self):
        print("see")
room=r3()  '''     
        



class aadhi():
    def call(self):
        print("BATMAN")
class rajesh():
    def lap(self):
        print("mobile")
class arun():
    def lap(self):
        super().lap()
        print("laptop")
fam=arun()
fam.lap()
























        























































