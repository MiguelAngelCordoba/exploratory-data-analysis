import pandas as pd
import random

def crear_csv_reducido(input_path, output_path, numero_filas=500):
    # Leer el archivo CSV
    df = pd.read_csv(input_path)

    # Seleccionar filas aleatorias
    filas_seleccionadas = random.sample(range(len(df)), min(numero_filas, len(df)))

    # Crear un nuevo DataFrame con las filas seleccionadas
    df_reducido = df.iloc[filas_seleccionadas]

    # Ordenar el nuevo DataFrame por orden ascendente
    df_reducido = df_reducido.sort_index()

    # Guardar el nuevo DataFrame en un nuevo archivo CSV
    df_reducido.to_csv(output_path, index=False)

input_csv = 'C_DIGO__NICO_DE_MEDICAMENTOS_VENCIDOS.csv'  
output_csv = 'Medicamentos_vencidos_reducido.csv'  

crear_csv_reducido(input_csv, output_csv)

df = pd.read_csv("Medicamentos_vencidos_reducido.csv")