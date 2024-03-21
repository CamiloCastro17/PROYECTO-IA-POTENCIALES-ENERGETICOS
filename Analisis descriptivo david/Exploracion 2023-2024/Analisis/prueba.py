import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns

archivo_excel = 'C:/Users/David/Documents/Universidad/Grado/Analisis descriptivo/Exploracion 2023-2024/Datos/Fontibon 2023-2024.xlsx'

nombre_hoja="DATA"
columnas = ['DateTime','PM10', 'CO','OZONO','NO','NO2','NOX','SO2','Vel Viento','Dir Viento','Temperatura','Precipitacion','PM2.5','HR','Presion Baro']
columnas_deseadas = ['DateTime','Vel Viento','Dir Viento','Temperatura']


fila_inicio = 0

df = pd.read_excel(archivo_excel,sheet_name=nombre_hoja, skiprows=fila_inicio)
df.columns=columnas

print("Tamaño de los datos \nColumnas: ", df.shape[1],"\nFilas: ",df.shape[0] )

df['DateTime'] = df['DateTime'].replace('24:00', '00:00', regex=True)
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d-%m-%Y %H:%M')
df['PM10'] = pd.to_numeric(df['PM10'],errors="coerce")
df['CO'] = pd.to_numeric(df['CO'],errors="coerce")
df['OZONO'] = pd.to_numeric(df['OZONO'],errors="coerce")
df['NO'] = pd.to_numeric(df['NO'],errors="coerce")
df['NO2'] = pd.to_numeric(df['NO2'],errors="coerce")
df['NOX'] = pd.to_numeric(df['NOX'],errors="coerce")
df['SO2'] = pd.to_numeric(df['SO2'],errors="coerce")
df['Vel Viento'] = pd.to_numeric(df['Vel Viento'],errors="coerce")
df['Dir Viento'] = pd.to_numeric(df['Dir Viento'],errors="coerce")
df['Temperatura'] = pd.to_numeric(df['Temperatura'],errors="coerce")
df['Precipitacion'] = pd.to_numeric(df['Precipitacion'],errors="coerce")
df['PM2.5'] = pd.to_numeric(df['PM2.5'],errors="coerce")
df['HR'] = pd.to_numeric(df['HR'],errors="coerce")
df['Presion Baro'] = pd.to_numeric(df['Presion Baro'],errors="coerce")

msno.matrix(df)

df_limpio = df.dropna()
msno.matrix(df_limpio)

df_viento = df[columnas_deseadas]
msno.matrix(df_viento)
df_viento_limpio = df_viento.dropna()
msno.matrix(df_viento_limpio)
print("Correlacion")
corr = df_viento_limpio.corr()

ax = plt.subplots(figsize=(9,7))

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True

ax = sns.heatmap(corr,annot=True,cmap='viridis',mask = mask)


fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Diagrama de caja para Vel Viento
axs[0].boxplot(df_viento_limpio['Vel Viento'])
axs[0].set_title('Velocidad de Viento')
axs[0].set_ylabel('m/s')

# Diagrama de caja para Dir Viento
axs[1].boxplot(df_viento_limpio['Dir Viento'])
axs[1].set_title('Dirección de Viento')
axs[1].set_ylabel('grados')

# Diagrama de caja para Temperatura
axs[2].boxplot(df_viento_limpio['Temperatura'])
axs[2].set_title('Temperatura')
axs[2].set_ylabel('°C')

# Ajustes adicionales si es necesario
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
cols = ['Vel Viento', 'Dir Viento', 'Temperatura']
# Crear histogramas para cada columna
for i in range(len(cols)):
    sns.histplot(df[cols[i]], kde=True, ax=axs[i])
    axs[i].set_title(f'Histograma - {cols[i]}')
    axs[i].set_xlabel(cols[i])
    axs[i].set_ylabel('Frecuencia')

# Ajustes adicionales si es necesario
plt.tight_layout()
plt.show()