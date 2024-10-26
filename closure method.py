'''def outer(x):
    def inner(y):
        return x+y
    return inner
a=outer(5)
result=a(10)
print(result)'''


'''
def aadhi(mark):
    def balaji(mark2):
        return mark+mark2
    return balaji
a=aadhi(1000)
result=a(500)
print(result)'''



'''def outer(x):
    def inner(y):
        return x+y
    return inner
a=outer("welcome")
res=a("aadhi")
print(res)'''



def mul(x):
    def mul2(y):
        return x*y
    return mul2
a=mul(int(input("enter num1")))
res=a(int(input('enter num2')))
print(res)
