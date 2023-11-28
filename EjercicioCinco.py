from numpy.random import choice
from collections import Counter
from icecream import ic
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

resultados = [1,2,3,4,5,6]
tamano_muestra = 100000

# Resultados lanzamiento de dado 1
dado_1 = choice(resultados, tamano_muestra)

# Resultados lanzamiendo de dado 2
dado_2 = choice(resultados, tamano_muestra)
 
# Suma de los resultados dado 1 + dado 2
suma_result = dado_1 + dado_2
  

dado_1 = pd.Series(dado_1) 
dado_1
dado_2 = pd.Series(dado_2)
dado_2
suma_result = pd.Series(suma_result) 
suma_result
dado_1_6 = dado_1 == 6 

dado_2_6 = dado_2 == 6
  
suma_result_6 = suma_result[dado_1_6 | dado_2_6] 


# Contando número de ejecuciones donde salió al menos un seis
conteo_ejecuciones_con_6 = suma_result_6.count()


# Contando ejecuciones con suma mayor o igual a 9
conteo_suma_mayoroigual_9 = suma_result_6[suma_result_6>=9].count()
 

probabilidad = conteo_suma_mayoroigual_9 / conteo_ejecuciones_con_6  #probbailidad analítica = 0.6363
print('P(la suma de puntos sea ≥ 9 | la cara 6 aparece) = ', probabilidad)

df = pd.DataFrame({
    'Dado_1': dado_1,
    'Dado_2': dado_2,
    'Suma_Result': suma_result
})


df_6 = df[(df['Dado_1'] == 6) | (df['Dado_2'] == 6)]


conteo_ejecuciones_con_6 = len(df_6)


conteo_suma_mayoroigual_9 = len(df_6[df_6['Suma_Result'] >= 9])


probabilidad = conteo_suma_mayoroigual_9 / conteo_ejecuciones_con_6

fig = px.pie(names=['Suma ≥ 9', 'Suma < 9'],
             values=[conteo_suma_mayoroigual_9, conteo_ejecuciones_con_6 - conteo_suma_mayoroigual_9],
             title=f'Probabilidad P(Suma ≥ 9 | Al menos un 6) = {probabilidad:.4f}',
             labels={'label': 'Suma de Resultados'},
             color_discrete_sequence=['darkblue', 'royalblue'])


fig.show()