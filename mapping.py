'''def dowle(x):
    return x*2
number=[1,2,3,4,5]
result=map(dowle,number)
print(set(result))
print(tuple(result))
print(list(result))'''


'''a=lambda s:s.upper()
words=["hello","pyhton"]
result=map(a,words)
print(list(result))'''



'''ten=lambda x:x+10
number=[23,44,55,6,6]
result=map(ten,number)
print(list(result))'''



'''def a(N):
    return N%2==0
number=[1,2,3,4,5,6,6]
result=filter(a,number)
print(list(result))'''
'''
b=lambda n:n>0
number=[-18,23,13,-66,-99]
result=filter(b,number)
print(list(result))'''

'''

def add(n):
    return n + n

numbers=[1,2,3,4,5]
result=map(add,numbers)
print(list(result))

num=[2,3,5,6,4,2]
res=map(lambda x:x+x,num)
print(list(res))

'''



num1=[2,4,6,8]
num2=[4,5,3,2]
res=map(lambda x,y:x*y,num1,num2)
print(list(res))































