from numpy.random import choice
from collections import Counter
from icecream import ic
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

turnos = ['T1', 'T2', 'T3']
probabilidades = [0.4, 0.35, 0.25]

tamano_muestra = 100000

muestra_turnos = choice(turnos, tamano_muestra, p=probabilidades)

print(muestra_turnos )
print("\n")  

probabilidades_teoricas = [0.4, 0.35, 0.25]


df_probabilidades_teoricas = pd.DataFrame({
    'Turno': ['T1', 'T2', 'T3'],
    'Probabilidad Teórica': probabilidades_teoricas
})


fig = px.funnel(df_probabilidades_teoricas, x='Probabilidad Teórica', y='Turno',
                title='PROBABILIDADES TEÓRICAS POR TURNO',
                labels={'Turno': 'Turno', 'Probabilidad Teórica': 'Probabilidad Teórica'},
                height=400, width=600,
                color='Turno',  
                color_discrete_map={'T1': 'blue', 'T2': 'green', 'T3': 'purple'})  


fig.show()

# Contando los turnos por muestra
conteo = Counter(muestra_turnos)
print(conteo)
print("\n")

df_conteo = pd.DataFrame(list(conteo.items()), columns=['Turno', 'Frecuencia'])


fig = px.bar(df_conteo, x='Turno', y='Frecuencia', 
             title='ARTÍCULO FABRICADOS POR TURNO',
             color='Frecuencia',
             color_continuous_scale=px.colors.sequential.Bluyl)


fig.show()

# Calculando probabilidades empíricas
Prob_T1 = conteo['T1'] / tamano_muestra
Prob_T2 = conteo['T2'] / tamano_muestra
Prob_T3 = conteo['T3'] / tamano_muestra
print('Prob_T1: ', round(Prob_T1, 4))
print('Prob_T2: ', round(Prob_T2, 4))
print('Prob_T3: ', round(Prob_T3, 4))
print("\n")

df_probabilidades = pd.DataFrame({
    'Turno': ['T1', 'T2', 'T3'],
    'Probabilidad': [Prob_T1, Prob_T2, Prob_T3]
})


fig = px.funnel(df_probabilidades, x='Probabilidad', y='Turno',
                title='PROBABILIDADES EMPÍRICAS POR TURNO',
                labels={'Turno': 'Turno', 'Probabilidad': 'Probabilidad Empírica'},
                height=400, width=600,
                color='Turno',  
                color_discrete_map={'T1': 'blue', 'T2': 'green', 'T3': 'purple'})  


fig.show()

# Listas de probabilidad de defectuosos y no defectuosos
Prob_T1_def = [0.01, 0.99]
Prob_T2_def = [0.02, 0.98]
Prob_T3_def = [0.03, 0.97]

# Listas de resultados por turno: defectuoso (D) y no defectuoso (G)
Resultados_T1 = ['T1D', 'T1G']
Resultados_T2 = ['T2D', 'T2G']
Resultados_T3 = ['T3D', 'T3G']

# Generando defectuosos y no defectuosos por turno
Detalle_T1 = choice(Resultados_T1, conteo['T1'], p=Prob_T1_def)
Detalle_T2 = choice(Resultados_T2, conteo['T2'], p=Prob_T2_def)
Detalle_T3 = choice(Resultados_T3, conteo['T3'], p=Prob_T3_def)
Detalle_Total = Detalle_T1.tolist() + Detalle_T2.tolist() 
Detalle_Total = Detalle_Total + Detalle_T3.tolist()

# Conteo defectuosos por turno
print(Counter(Detalle_T1))
print(Counter(Detalle_T2))
print(Counter(Detalle_T3))
print("\n")

Defectuosos = [i for i in Detalle_Total if "D" in i]
conteo_defectuosos = len(Defectuosos)


# Identificando número de defectuosos por turno
conteo_defectuosos_turno = Counter(Defectuosos)
print(conteo_defectuosos_turno)
print("\n")

# Contando el número total de defectuosos
numero_defectuosos = len(Defectuosos)
print('Total de defectuosos: ',numero_defectuosos)
print("\n")

# Calculando la probabilidad de que un artículo al azar resulte ser defectuoso #probailidad analítica 0.0185
probabilidad_defectuoso = numero_defectuosos / tamano_muestra
print('Probabilidad empírica de item defectuoso: ', round(probabilidad_defectuoso,4))  
print("\n")

df_probabilidad_defectuoso = pd.DataFrame({
    'Categoría': ['Defectuoso', 'No Defectuoso'],
    'Probabilidad': [probabilidad_defectuoso, 1 - probabilidad_defectuoso]
})


fig = px.bar(df_probabilidad_defectuoso, x='Categoría', y='Probabilidad',
             text='Probabilidad',
             labels={'Probabilidad': 'Probabilidad'},
             title='Probabilidad de Artículo Defectuoso',
             height=400, width=600,
             color='Categoría',  
             color_discrete_map={'Defectuoso': 'paleturquoise', 'No Defectuoso': 'turquoise'})


fig.update_layout(
    yaxis_tickformat=',.2f'  
)


fig.show()

# Calculando probabilidades revisadas
Prob_T1_dado_D = conteo_defectuosos_turno['T1D'] / conteo_defectuosos
Prob_T2_dado_D = conteo_defectuosos_turno['T2D'] / conteo_defectuosos
Prob_T3_dado_D = conteo_defectuosos_turno['T3D'] / conteo_defectuosos
print('Prob_T1_dado_D: ', round(Prob_T1_dado_D, 4)) #probabilidad analítica 0.216
print('Prob_T2_dado_D: ', round(Prob_T2_dado_D, 4)) #probbailidad analítica 0.378
print('Prob_T3_dado_D: ', round(Prob_T3_dado_D, 4)) #probabilidad analítica 0.405

data = {
    'Turno': ['T1', 'T2', 'T3'],
    'Probabilidad': [round(Prob_T1_dado_D, 4), round(Prob_T2_dado_D, 4), round(Prob_T3_dado_D, 4)]
}

df = pd.DataFrame(data)

colores_personalizados = ['#FF9999', '#66B2FF', '#99FF99']


fig = px.pie(df, names='Turno', values='Probabilidad',
             title='PROBABILIDADES CONDICIONALES POR TURNO DADO QUE SON DEFECTUOSOS',
             color_discrete_sequence=colores_personalizados)


fig.show()