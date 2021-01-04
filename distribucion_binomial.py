'''Programa que calcula la distribución binomial
del problema 10.3, pp 252, libro Probabilidad y
estadistica serie Schaum

By Edgar Lara
06-jun-2020
'''
import os
import matplotlib.pyplot as plt
import math
os.system("clear")

x=[]
y=[]
#x = range(1,64)
lanzamientos = 64
n=1
p=0.5
i=0

def binomial(x,n,p):
	A = math.factorial(n)
	B = (math.factorial(x)*math.factorial(n-x))
	factoriales = A/B
	probabilidades=p**x*(1-p)**(n-x)
	return(factoriales*probabilidades)
print("x\tProbabilidad")
while (i < lanzamientos):
	x.append(i)
	y.append(binomial(x[i],lanzamientos,p))
	print(x[i],y[i])
	i += 1
#print(y)

plt.title('Lanzamientos de moneda')
plt.xlabel('x')
plt.ylabel('probabilidad')
plt.plot(x,y,'+')
plt.show()
input()
