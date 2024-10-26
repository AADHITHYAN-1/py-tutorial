'''def upper_string(ref):
    def process():
        data=ref()
        return data.upper()
    return process
def myfunction():
    return"happy morning"
output=upper_string(myfunction)
print(output())
'''

'''def x(mark):
    def y():
        data=mark()
        return data.upper()
    return y
def z():
    return'my mark is high'
output=x(z)
print(output())'''


'''def upper(res):
    def process():
        data=res()
        return data.upper()
    return process
@upper
def myfun():
    return"welcome python"
print(myfun())'''
    

'''def upper(res):
    def process():
        data=res()
        return data.upper()
    return process
def upper2(res):
    def process2():
        data=res()
        return data.split()
    return process2
@upper2()
@upper()
def myfun():
    return"welcome python"
print(myfun())'''
    


'''
def outer():
    mes1='hello'
    def inner():
        mes2='aadhi'
        mes=mes1+mes2
        return mes
    return inner
obj=outer()
print(obj())'''




'''def add(x):
    def add(y):
        return x+y
    return add
obj=add(5)
res=obj(6)
print(res)'''


def dec(fun):
    def process(*args):
        if 0 in args[1:]:
            return "zero division"
        return process
    return process
@dec
def divide(a,b):
    return a|b
print(divide(10,0))














#passing function parametter
'''
def fun1():
    print("function1")
def fun2():
    print("fun2")
fun1()
fun2()'''


'''
def fun1():
    print("fun1")
def fun2(res):
    res()
    print("fun2")
print(fun1)
fun2(fun1)




def add(x,y):
    return x+y
def dis(fun,x,y):
    return fun (x,y)
res=dis(add,4,5)
print(res)
'''




'''def upper(test):
    return test.upper()
def lower(test):
    return test.lower()
def test(fun):
    msg=fun("happy learning")
    print(msg)
test(upper)
test(lower)'''
    
    


#return value
def val(name):
    def val2():
        return "happy",name
    return(val2)
call=val("aadhi")
print(call())




























































