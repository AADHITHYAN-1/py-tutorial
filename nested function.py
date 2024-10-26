'''def outer():
    msg1="welcome"
    def inner():
        msg2="python"
        msg=msg1+msg2
        return msg
    return inner
obj=outer()
print(obj())'''


#global local variyable

'''x=10
def fun():
    y=88
    print(y)
    print(x)
fun()
print(y)'''


#nonlocal variyable
#nolocal keyword is used to nested function to modify variyaable defined the nearest evclosing scope is not the golbal scope

def outer():
    x=10
    def inner():
        nonlocal x
        x=20
        print(x)
    inner()
    print(x)
outer()



