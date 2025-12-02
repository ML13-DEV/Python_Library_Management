#ESTE ES EL ARCHIVO QUE TIENE LAS FUNCIONES QUE REALIZAN OPERACIONES CON LA BASE DE DATOS

#IMPORTAMOS EL MÓDULO MARIADB PARA CONECTARNOS A LA BASE DE DATOS
#import mariadb
from db import engine
from sqlalchemy import text

#CREAMOS LA CLASE ControlStock
class ControlStock():

    def __init__(self, table, category):
        self.table = table
        self.category = category

    def search_product(self, dato):
        try:
            query = text(f"SELECT * FROM {self.category} ORDER BY {self.table} ASC")

            with engine.connect() as conn:
                productos = conn.execute(query).fetchall()

            l = 0
            r = len(productos) - 1

            while l <= r:
                m = (l + r) // 2
                if dato == productos[m][1]:
                    return productos[m]
                elif dato > productos[m][1]:
                    l = m + 1
                else:
                    r = m - 1

            return None

        except Exception as e:
            print(f"ERROR DURING SEARCH: {e}")
            return None

    def insert(self, datos):
        try:
            if isinstance(datos, list):
                placeholders = ", ".join([":p" + str(i) for i in range(len(datos[0]))])
                query = text(f"INSERT INTO {self.category} VALUES ({placeholders})")

                with engine.begin() as conn:
                    conn.execute(query, [ {f"p{i}": value for i, value in enumerate(row)} for row in datos ])
                return f"{len(datos)} ROWS INSERTED."

            elif isinstance(datos, tuple):
                placeholders = ", ".join([":p" + str(i) for i in range(len(datos))])
                query = text(f"INSERT INTO {self.category} VALUES ({placeholders})")

                with engine.begin() as conn:
                    conn.execute(query, {f"p{i}": value for i, value in enumerate(datos)})

                return f"PRODUCT INSERTED: {datos}"

        except Exception as e:
            print(f"ERROR DURING INSERT: {e}")
            return None

    def read(self):
        try:
            if len(self.table) > 1:
                query = text(f"SELECT * FROM {self.category} ORDER BY {self.table}")
            else:
                query = text(f"SELECT * FROM {self.category}")

            with engine.connect() as conn:
                productos = conn.execute(query).fetchall()

            return productos

        except Exception as e:
            print(f"ERROR DURING READ: {e}")
            return None

    def update(self, old, new):
        if not old or not new:
            return "MISSING ARGUMENTS"

        query = text(
            f"UPDATE {self.category} SET {self.table} = :new WHERE {self.table} = :old"
        )

        try:
            with engine.begin() as conn:
                conn.execute(query, {"old": old, "new": new})
            return f"UPDATED: {old} → {new}"
        except Exception as e:
            print(f"ERROR DURING UPDATE: {e}")
            return None

    def delete(self, field):
        query = text(f"DELETE FROM {self.category} WHERE {self.table} = :field")

        try:
            with engine.begin() as conn:
                conn.execute(query, {"field": field})
            return f"PRODUCT DELETED: ({field})"

        except Exception as e:
            print(f"ERROR DURING DELETE: {e}")
            return None
