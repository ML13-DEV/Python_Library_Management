from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db import engine

BASE_DIR = Path(__file__).resolve().parent.parent
FIGURES_DIR = BASE_DIR / "reports"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

#FUNCIÓN PARA GRAFICAR LOS LIBROS MÁS ALQUILADOS
def libros_mas_alquilados():
    mas_alquilados = """select Libro as 'libro', COUNT(reservas.ID_Libro) as 'reservas' from libros 
                        join reservas on libros.ID_Libro = reservas.ID_Libro
                        group by libros.ID_Libro order by COUNT(reservas.ID_Libro) desc limit 5;"""
    
    plt.figure(figsize=(10,6))
    
    datos = pd.read_sql_query(mas_alquilados, engine)
    
    plt.bar(datos["libro"], datos['reservas'])
    plt.title("Los 5 libros más alquilados")
    plt.xlabel("Libros")
    plt.ylabel("Cantidad de reservas")
    plt.savefig(FIGURES_DIR / "libros_mas_alquilados.png")
    plt.show()

#FUNCIÓN PARA GRAFICAR LOS MESES CON MÁS ALQUILERES 
def meses_mas_alquilados():
    meses_alquileres = """select month(Fecha_salida) as 'Mes', COUNT(linea) as 'Reservas' from reservas
                        group by month(Fecha_salida)
                        order by COUNT(linea) DESC;"""
                        
    datos = pd.read_sql_query(meses_alquileres, engine)

    plt.figure(figsize=(10,7))
    bars = plt.bar(datos['Mes'], datos['Reservas'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval),
                ha='center', va='bottom', fontsize=10)
    plt.xlabel("Meses")
    plt.ylabel("Cantidad de reservas")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "meses_mas_alquilados.png")
    plt.show()
 
#FUNCIÓN PARA GRAFICAR LOS USUARIOS CON MÁS ALQUILERES   
def usuarios_alquilados():
    usuarios_alquileres = """select CONCAT(usuarios.Nombre, " " ,usuarios.Apellido) as 'Usuario', COUNT(reservas.DNI_Usuario ) as 'reservas' from usuarios 
                        join reservas on usuarios.DNI_Usuario  = reservas.DNI_Usuario 
                        group by usuarios.DNI_Usuario  order by COUNT(reservas.DNI_Usuario ) desc limit 5;"""
                        
    datos = pd.read_sql_query(usuarios_alquileres, engine)

    plt.figure(figsize=(10,7))
    bars = plt.bar(datos['Usuario'], datos['reservas'])
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval),
                ha='center', va='bottom', fontsize=10)
    plt.xlabel("Usuarios")
    plt.ylabel("Cantidad de reservas")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "usuarios_con_mas_alquileres.png")
    plt.show()

#FUNCIÓN PARA GRAFICAR LOS ALQUILERES POR MES EN EL AÑO 2024
def ver_2024():
    alquileres_2024 = """select MONTH(reservas.Fecha_salida) as 'Mes', COUNT(reservas.linea) as 'Reservas' from reservas where YEAR(reservas.Fecha_salida) = '2024'
                            group by MONTH(reservas.Fecha_salida);"""
                            
    datos = pd.read_sql_query(alquileres_2024, engine)
    datos['Mes'] = pd.to_numeric(datos['Mes'])
    sns.lineplot(x='Mes', y='Reservas', data=datos, marker='o', palette="viridis", linewidth=2.5)
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Reservas')
    plt.xticks(range(1, 13)) 
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "ver_2024.png")
    plt.show()

#FUNCIÓN PARA GRAFICAR LOS ALQUILERES POR MES EN EL AÑO 2025
def ver_2025():
    alquileres_2025 = """select MONTH(reservas.Fecha_salida) as 'Mes', COUNT(reservas.linea) as 'Reservas' from reservas where YEAR(reservas.Fecha_salida) = '2025'
                            group by MONTH(reservas.Fecha_salida);"""
    
    datos = pd.read_sql_query(alquileres_2025, engine)
    datos['Mes'] = pd.to_numeric(datos['Mes'])
    sns.lineplot(x='Mes', y='Reservas', data=datos, marker='o', palette="viridis", linewidth=2.5)
    plt.xlabel('Mes')
    plt.ylabel('Cantidad de Reservas')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.savefig(FIGURES_DIR / "ver_2025.png")
    plt.show()

#FUNCIÓN QUE COMPARA LOS ALQUILERES MENSUALES DEL AÑO 2024 VS 2025
def comparar_years():
    reservas = """select MONTH(reservas.Fecha_salida) as 'Mes', COUNT(reservas.linea) as 'Reservas', YEAR(reservas.Fecha_salida) as 'Año' from reservas 
                    group by Mes, Año order by Mes, Año;"""
    
    datos2 = pd.read_sql_query(reservas, engine)
    datos2['Mes'] = pd.to_numeric(datos2['Mes'])
    datos2['Año'] = pd.to_numeric(datos2['Año'])
    
    g = sns.catplot(data=datos2, kind='bar', x='Mes', y='Reservas', hue='Año', errorbar="sd", palette="dark", alpha=.6, height=6, dodge=True)
    g.despine(left=True)
    g.set_axis_labels("Meses", "Reservas")
    plt.savefig(FIGURES_DIR / "2024_vs_2025.png")
    plt.show()
