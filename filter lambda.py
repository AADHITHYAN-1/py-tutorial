#filter
'''number=[1,2,3,4,5,5,7,8,5,12]
a=filter(lambda x:x%2==0,number)
print(list(a))


names=["pyhton","print","praveen","peple","idle"]
b=lambda name:name.startswith("p")
c=filter(b,names)
print(list(c))'''

'''
def fun(num):
    if num%2==0:
        return True
    else:
        return False
number=[1,2,3,4,5,6,7,8]
fil=filter(fun,number)
print(list(fil))
'''


'''
a=[1,2,3,4,18,99,88,100]
def age(o):
    if o>=18:
        return True
    else:
        return False
res=filter(age,a)
for x in res:
    print(x)'''




'''seq=[1,2,3,4,5,11,22,33,44,55,44,33]
res=filter(lambda x:x%2==0,seq)
print(list(res))
'''


res=filter(lambda x:x%2==0,range(1,50))
print(list(res))





























