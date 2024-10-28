import numpy as np

aray=np.array([1,2,3,4,5,6,7,8,9,0])
print(aray[0])

print(aray[0:5])
print(aray[:5])
print(aray[4:10])
print(aray[4:])
print(aray[0:10:2])
print(aray[::-1])

araar=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(araar)
print(araar[0:2,0:2])

rar=np.arange(1,50).reshape(7,7)
print(rar)

print(rar[2:5,2:5])

ara=np.array([1,2,3,4,5,6,7,8])

even= ara[ara%2 == 0]
print(even)

odd=ara[ara%2==1]
print(odd)

a=ara[ara == 5]
print(a)

av=ara[ara == 50]
print(av)
print(ara[[2,4,6]])

araa=np.array([1,2,3,4,5,6,7,8,9,10])
less5=araa[araa < 5]
print(less5)

araa +=1
print(araa)

array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])

result=array1+array2
print(result)

difference=array2-array1
print(difference)

araaaa=np.random.permutation(np.arange(16)).reshape(4,4)
print(araaaa)

araaa=np.random.permutation(np.arange(16)).reshape(4,4)
print(araaa)

araaaaaaa=araaa+araaaa
print(araaaaaaa)

def linear_eqn(x):
    y=(2*x)+3
    print(y)

linear_eqn(3)

x=np.array([1,2,3,4,5])
linear_eqn(x)