import matplotlib.pyplot as plt
import math as mt
import numpy as np

def open_file(nom):
	file = open(nom, 'r')
	matrix = [line.split() for line in file]
	file.close()
	
	Aguilas_ = 0
	Lanzamientos_ = len(matrix)
	for t in range(len(matrix)):
		Aguilas_ += int(matrix[t][1])
	Sellos_ = Lanzamientos_ - Aguilas_

	E_A_ = mt.sqrt(Aguilas_)/Aguilas_
	E_S_ = mt.sqrt(Sellos_)/Sellos_

	Prob_ = [Aguilas_/Lanzamientos_, Sellos_/Lanzamientos_]
	Errores_ = [E_A_, E_S_]

	return Lanzamientos_, Prob_, Errores_


lanzamientos, Prob, Errores = open_file('lanzamientos.txt')
#print(Prob, Errores)
labels = ['P Aguilas = ' +str(Prob[0]),   'P Sellos = '  +str(Prob[1])]
labels_error = ['E_A = ' + str(Errores[0]),    'E_S = ' +str(Errores[1])]
x_pos = [0, 1]


for i in range(len(labels)):
	plt.text(x = x_pos[i]-0.4 , y = Prob[i], s = labels_error[i])

plt.title('Probabilidad de 100 lanzamientos de moneda')
#plt.
plt.bar(x_pos, Prob, yerr=Errores, align='center', alpha=0.5, ecolor='black', capsize=10)
plt.ylabel('Probabilidades')
plt.xticks(range(2), labels)
plt.axhline(0.5, label = 'P predicha')
plt.legend()
plt.show()