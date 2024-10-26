"""class company():
    def __init__(self):
        self.__company="amazon"
obj=company()
obj.company="micro"
print(obj.__company)

this class can private because dowle under score __ is a private so this not output sowed"""


'''class company():
    def __init__(self):
        self.__company="amazon"
    def cname(self):
        print(self.__company)
obj=company()
obj.cname()
print(obj.__company)

but this code run becase class cna be acces the private and dont other change the names'''




"""class company():
    def __init__(self):
        self._company="amazon"
class b(company):
    pass
obj=b()
print(obj._company)

its a protected method its child class can be used properties"""




'''(__)dowle under score is a private,no one change the variyable name its hideed
(_)single is a proticted,  and its acces with child class
()is a public,its all are change'''
