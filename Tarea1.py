import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import  mean_squared_error, r2_score
from mpl_toolkits.mplot3d import axes3d
import numpy as np
data=pd.read_excel('BI_Alumnos08.xlsx')
lista=pd.DataFrame()
alt=data['Altura']
ed=data['Edad']
lista['Altura']=alt
lista['Edad']=ed

XY=np.array(lista)
Z=data['Peso'].values
regLM=linear_model.LinearRegression()
regLM.fit(XY,Z)
z_pred=regLM.predict(XY)
print('Coeficientes de R',regLM.coef_)
print('error cuadrado medio: %.2f '% mean_squared_error(Z,z_pred))
print('puntaje de varianza: %.2f' % r2_score(Z,z_pred))
arreglo=np.array(data['Altura'])
arreglo2=np.array(data['Edad'])

for i in arreglo:
    for o in arreglo2:
        predPeso = regLM.predict([[i, o]])
        print("|  ",i," | ", o," |    ", int(predPeso),"   |")

arreglo3=np.array([int(predPeso)])

# Creamos la figura
fig = plt.figure()
# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')
ax1.scatter(arreglo3, arreglo2, arreglo, c='g', marker='o')
ax1.set_xlabel('Peso Predictivo')
ax1.set_ylabel('Edad')
ax1.set_zlabel('Altura')
ax1.set_title('Regresión Lineal con Múltiples Variables')
# Mostramos el gráfico
plt.show()