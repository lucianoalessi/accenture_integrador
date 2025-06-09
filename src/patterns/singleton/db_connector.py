import os
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import Error, connect 
from sqlalchemy import create_engine

# Cargar variables desde .env
load_dotenv()

class MySQLConnector:
    _instance = None # Implementación del patrón Singleton (una sola instancia de esta clase)

    # NOTA:__new__ es un método especial que crea la instancia de una clase antes de inicializarla con __init__
    def __new__(cls):
        # Si no hay instancia previa, entonces se crea una:
        if cls._instance is None:
            print("Estableciendo nueva conexión...")
            cls._instance = super(MySQLConnector, cls).__new__(cls)
            cls._instance._initialized = False  # Se marca que aún no fue inicializado
        else: 
            print("Usando instancia existente.")
        return cls._instance  # Siempre devuelve la misma instancia
    
    def __init__(self):
        # Evita que se vuelva a inicializar si ya está iniciado
        if self._initialized:
            return

        # Carga configuración desde las variables de entorno (.env)
        self.config = {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "port": int(os.getenv("DB_PORT")),
        }

        self.conexion = None  # La conexión con la base de datos
        self.cursor = None    # Cursor para ejecutar queries
        self._initialized = True  # Marca como inicializado


    def conectar(self):
        if self.conexion is None:  # Solo se conecta si no está conectado aún
            try:
                self.conexion = connect(
                    **self.config  # Desempaqueta el diccionario de configuración
                )
                self.cursor = self.conexion.cursor()  # Crea el cursor para ejecutar queries
                print(
                    f"Conexion exitosa a la base de datos '{self.config['database']}'"
                )
            except Error as err:
                print(f"Error al conectar: {err}")
                raise  # Vuelve a lanzar el error si hay un problema


    def ejecutar_query(self, query):
        if self.cursor is None:
            raise Exception(
                "Primero debes conectarte con el metodo conectar()."
            )
        self.cursor.execute(query)
        return self.cursor.fetchall()  # Devuelve los resultados como lista de tuplas
    
    
    def query_df(self, query):
        """Ejecuta una consulta y devuelve un DataFrame usando SQLAlchemy"""
        # Arma la URI de conexión para SQLAlchemy
        uri = (
            f"mysql+mysqlconnector://{self.config['user']}:{self.config['password']}"
            f"@{self.config['host']}:{self.config['port']}/{self.config['database']}"
        )
        engine = create_engine(uri)  # Crea el motor de conexión
        return pd.read_sql(query, engine)  # Ejecuta la query y devuelve un DataFrame
    
    
    # def ejecutar_script_sql(self, ruta_script):
    #     """
    #     Ejecuta un archivo .sql completo (puede contener múltiples sentencias).
    #     Si ocurre un error de sintaxis, muestra la sentencia problemática y su posición.
    #     """
    #     if self.cursor is None:
    #         raise Exception(
    #             "Primero debes conectarte con el metodo conectar()."
    #         )
    #     with open(ruta_script, 'r', encoding='utf-8') as archivo:
    #         script = archivo.read()
    #     statements = script.split(';')
    #     for idx, statement in enumerate(statements, 1):
    #         stmt = statement.strip()
    #         if stmt:
    #             try:
    #                 self.cursor.execute(stmt)
    #             except Exception as e:
    #                 print(f"\n[ERROR] en sentencia #{idx} del script '{ruta_script}':")
    #                 print(f"Sentencia SQL:\n{stmt}\n")
    #                 print(f"Error: {e}\n")
    #                 raise  # Vuelve a lanzar el error para que el usuario lo maneje si lo desea
    #     self.conexion.commit()  # Asegura que los cambios se guarden
    #     print(f"Script '{ruta_script}' ejecutado correctamente.")


    def ejecutar_script_sql(self, ruta_script):
        """
        Ejecuta un archivo .sql completo (puede contener múltiples sentencias).
        """
        if self.cursor is None:
            raise Exception(
                "Primero debes conectarte con el metodo conectar()."
            )
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            script = archivo.read()
        for statement in script.split(';'):
            stmt = statement.strip()
            if stmt:
                self.cursor.execute(stmt)
        self.conexion.commit()  # Asegura que los cambios se guarden
        print(f"Script '{ruta_script}' ejecutado correctamente.")

    
    def cerrar(self):
        if self.cursor:
            self.cursor.close()  # Cierra el cursor
            self.cursor = None
        if self.conexion:
            self.conexion.close()  # Cierra la conexión
            self.conexion = None
            print("Conexion cerrada.")

