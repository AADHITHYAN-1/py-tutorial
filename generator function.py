'''python.exedef num():
    return 5
print(num())


def num():
    yield 5
print(num())'''


'''def num():
    yield 5
    yield 3
    yield 6
    yield 9
for i in num():
    print(i)'''



'''def num():
    yield 2
    yield 3
    yield 5
    yield 7
obj=num()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())'''



'''def num():
    yield 2
    yield 3
    yield 5
    yield 7
obj=num()
print(obj)'''







'''def num():
    yield 2
    yield 3
    yield 5
    yield 7
for i in num():
    print(i)'''




'''def multiple():
    str1="welcome"
    yield str1
    str2="python"
    yield str2
    str3="programming"
    yield str3
obj=multiple()
print(next(obj))
print(next(obj))
print(next(obj))'''


'''def sum():
    for i in range(20):
        if i%2==0:
            yield i
for i in sum():
    print(i)'''



'''def loop():
    n=1
    while n<=10:
        obj=n
        yield obj
        n=n+1
for i in loop():
    print(i)'''





'''
def loop():
    n=1
    while n<=10:
        obj=n
        yield obj
        n=n+1
summ=loop()
print(summ.__next__())
print(summ.__next__())
print(summ.__next__())
print(summ.__next__())
print(summ.__next__())'''



'''def loop():
    n=1
    while n<=10:
        obj=n*n
        yield obj
        n=n+1
for i in loop():
    print(i)'''


'''def fibna(val):
    a,b=1,2
    while True:
        c=a+b
        if c<val:
            yield c
            a=b
            b=c
        else:
            break
obj=fibna(10)
print(obj.__next__())
print(obj.__next__())
'''


'''def cube(n):
    for i in range(1,n+1):
        yield i**3
n=int(input('enter num'))
obj=cube(n)
print(obj.__next__())
print(obj.__next__())'''




'''
def res(val):
    yield val[::-1]
num=str(input("enter word:"))
obj=res(num)
print("the reverse is  :",obj.__next__())
'''


'''def fun():
    for i in range(1,10):
        yield i*i
for squ in fun():
    print(f"the squ is :",{squ})'''





'''def fun():
    fact=1
    for i in range(1,6):
        fact=fact*i
        yield fact
for i in fun():
    print(i)'''




'''def string(val):
    length=len(val)
    for i in range(length):
        for j in range(i,length):
            yield j
for z in string("abc"):
    print(z)'''



'''def fub():
    a=[1,2,2,3,4,55,66,7,6,7]
    b=list(set(a))
    for i in b:
        yield i
var=fub()
print(var.__next__())'''


def check(n):
    a=[]
    for i in n:
        if i not in a:
            a.append(i)
    yield a
val=input("enter a number :")
cal=val.split()
b=check(cal)
print(next(b))







































        
        








































    
