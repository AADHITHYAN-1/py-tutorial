"""lambda function(anonymous function)


->its limited to single expression and cannot span multiple line


syntax:v name=lambda :arqument ,expression:


"""

'''normal function'''


'''def fun(x,y):
    return x+y
print(fun(5,6))'''



'''lambda fuction'''

'''add=lambda x,y:x+y
print(add(3,5))'''


'''square'''
'''square=lambda x:x**3
print(square(4))'''



'''concat'''
'''concat=lambda a,b:a+b
print(concat("hello","world!"))
'''

'''even number'''
'''a=lambda x:x%2==0
print(a(10))
print(a(3))
'''




'''
max value'''

'''b=lambda x,y:x if x>y else y
print(b(1000,5000))'''


'''length'''
'''c=lambda s:len(s)
print(c("aadhithyam"))'''



'''
add=lambda a,b:a+b
print(add(10,2))
add=lambda y:y+2999
print(add(1000))'''



'''a=lambda name:print("hello world",name)
a("aadhi")'''



'''lam=lambda a:a+10
print(lam(6))'''

'''
a=lambda a,b,c,d:a-b-c-d
print(a(2,3,4,5))'''


l1=[4,5,6,7,8]
l2=[]
for i in l1:
    temp=lambda i:i**2
    l2.append(temp(i))
print(l2)
























