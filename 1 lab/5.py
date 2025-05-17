from random import randint
list=[]
for i in range(20):
    list.append(randint(1,100))
print(list)

chetnie=[]
for i in list:
    if i %2 ==0:
        chetnie.append(i)
print(sorted(chetnie)) 

delna3=[]
for i in list:
    if i %3 ==0:
        delna3.append(i)
print(sorted(delna3))   

sum=0
kol=0
for i in list:
    sum +=i
    kol+=1
print(sum/kol)   
