'''name=["aadhi","praveen","siva"]
name2=['1233321','444333','554433']
a=dict(zip(name,name2))
print(a)
'''


'''a=['aadhi','siba','balaji','vicky']
b=('1000','44444','55555','33333')
c={"kumbakonam","mayavaram","sirkaxzi","bangulare"}
res=tuple(zip(c,a,b))
print(res)'''



'''name=['aadhi',"balaji",'siva']
num=('111222333','333444455','2233344567')
a=list(zip(name,num))
for a,b in a:
    print(a,b)'''


'''color=("yello","red","pink")
name=('mango','apple','graph')
a=list(zip(name,color))
print(a)'''


#unzip method (zip(*itrable)to convert unzip


'''color=("yello","red","pink")
name=('mango','apple','graph')
a=list(zip(name,color))
print(a)
a1,a2=list(zip(*a))
print(a1)
print(a2)'''




'''paries=[(1,"aadhi"),(2,'siva'),(3,'balaji'),(4,'vicky')]
num,name=zip(*paries)
print(num)
print(name)'''






from itertools import zip_longest
a=[1,2,3,4,5,6,7]
b=('a','b','c','d','f','g','h')
c=range(10)
zipping=zip_longest(a,b,c,fillvalue="missing")
print(list(zipping))




















































