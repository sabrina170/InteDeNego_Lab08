import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import  mean_squared_error, r2_score

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

predPeso= regLM.predict([[180,22]])
print('prediccion de peso: ', int(predPeso))

