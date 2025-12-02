import pandas as pd
from db import engine

#FUNCIÓN PARA LEER EL CSV CON LA INFORMACIÓN GENERADA Y PASARLA A LA TABLA DE RESERVAS EN LA BASE DE DATOS.
def leer_reservas():
    reservas = pd.read_csv('data/reservas_libros.csv')
    reservas.to_sql("reservas", engine, if_exists='append', index=False, chunksize=100)

    return "DATOS INSERTADOS"
