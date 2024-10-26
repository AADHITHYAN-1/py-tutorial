

#7
'''
num=int(input("enter a num"))
fact=1
for i in range(num,0,-1):
    print(i)
    fact=fact*i
print( "the fact is :",fact)'''
    

    
    


#9
'''
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = dict1 | dict2
print(merged_dict)'''



#6

'''a=int(input("num1:"))
b=int(input("num2:"))
c=int(input("num3:"))
if(a>b and a>c):
    print("a")
elif(b>a and b>c):
    print("b")
elif(c>a and c>b):
    print("c")'''






#5
'''n=int(input("entern num :"))
for i in range(n):
    if i%2==0:
        print("01010101")
    else:
        print("10101010")'''




'''
n=int(input("enter a num:")):
    for i in range(1,n):
        for j in range'''
        

'''
#test qu
#7

a=int(input("enter a number"))
b=int(input("enter a number"))
res=lambda a,b:a if a>b else b
print("enter big num is",res(a,b))
#9
a=[1,2,3,4,5]
result=lambda a:a**2
b=list(map(result,a))
print(b)


#10

a=[3,4,6,9,2]
res=lambda a:a>5
b=list(filter(res,a))
print(b)



#11
a=[(1,2),(3,1),(2,1)]
b=sorted(a,key=lambda x:x[1])
print(b)
'''
'''


#30-8-2024
#1
def fun(n):
    a=[]
    for i in n:
        if i not in a:
            a.append(i)
    yield a
val=input('enter a spe num:')
cal=val.split()
a=fun(cal)
print(next(a))


#2
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return(inner)
res=outer()
print(res())
print(res())


#3
def add1(x):
    def add2(y):
        return x+y
    return(add2)
val=add1(10)
res=val(10)
print(res)



#4
def uppercase(n):
    def inner():
        cal=n()
        return cal.upper
    return(inner)
@uppercase
def greek():
    return "aadhithyan"
val=greek()
print(val())'''

    

'''
class year:
    def __init__(self,year):
        self.year=year
    def leep(self):
        if n%4==0:
            print("leep year")
        else:
            print("normal year")
n=int(input('enter year'))
obj=year(n)
obj.leep()
'''


#10
'''def num(n):
    print(len(n))
n=input("enter a string:")
obj=num(n)'''




n=int(input("enter word :"))
a=
    
    










































