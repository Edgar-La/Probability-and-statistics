'''Programa que calcula datos de estadistica
del problema 10.8, pp 255, libro Probabilidad y
estadistica serie Schaum

By Edgar Lara
06-jun-2020
'''
import os
import matplotlib.pyplot as plt
import math
import statistics
from scipy.stats import norm
os.system("clear")
####################################################
x=[]
y=[9, 8, 7, 4, 8, 6, 8, 8, 7, 10, 8, 10, 6, 7, 7, 8, 9, 
6, 5, 8, 5, 6, 8, 7, 8, 5, 5, 8, 7, 6, 6, 4, 5]
alpha = 0.05
CI=[0,0]
i=0
while(i < len(y)):
	x.append(i+1)
	i+=1
####################################################
N = len(x)
Mean = sum(y)/len(y)
StDev = statistics.stdev(y)
SE_Mean = statistics.stdev(y)/math.sqrt(len(x))
Z = (Mean-5)/SE_Mean
P=1-norm.cdf(Z)
Mu = 5
CI[0] = (1-alpha)*Mean
CI[1] = (1+alpha)*Mean

print("N = " + str(N))
print("Mean = " + str(Mean))
print("StDev = " + str(StDev))
print("SE Mean = " + str(SE_Mean))
print("Z = " + str(Z))
print("P = " + str("{:.10f}".format(P)))
print("CI = " + str(CI))
print("CI -> Intervalo confianza -> 100±0.05% Mu")
####################################################
print("\nPor tanto:")
if(Z<-1.96):
	print("a) La hipotesis nula no se rechaza.")
else:
	print("a) La hipotesis nula se rechaza.")
if(P>alpha):
	print("b) La hipotesis nula no se rechaza.")
else:
	print("b) La hipotesis nula se rechaza.")
if (CI[0] < Mu) and (Mu<CI[1]):
	print("c) La hipotesis nula no se rechaza.")
else:
	print("c) La hipotesis nula se rechaza.")
####################################################
plt.title('Horas que escuchan la radio 33 personas')
plt.xlabel('Horas vistas')
plt.ylabel('Cant. de personas')
#plt.bar(x, y)
#plt.plot(x,y, 'ro')
plt.hist(y,bins=25)
plt.show()
input()

