import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# Load environment variables from .env file
load_dotenv()

class DataConexion:
    def connect(self):
        """
        Method to create and return a connection to the database using SQLAlchemy.
        """
        try:
            host = os.getenv("DB_HOST")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            database = os.getenv("DB_NAME")

            # Create SQLAlchemy engine
            connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
            engine = create_engine(connection_string)

            # Test connection
            with engine.connect() as connection:
                print("Welcome to the database!")
            return engine

        except SQLAlchemyError as e:
            print("Critical database connection error: Database server is not available or parameters are incorrect", e)
            return None

    def execute_procedure(self, procedure_name, params=[]):
        """
        Method for executing a stored procedure that returns results.
        """
        results = []
        args = params
        engine = self.connect()
        cursor = None
        if engine is not None:
            try:
                connection = engine.raw_connection()
                cursor = connection.cursor(dictionary=True)
                cursor.callproc(procedure_name, params)

                for result in cursor.stored_results():
                    results = result.fetchall()

                connection.commit()

            except SQLAlchemyError as e:
                print("Error executing procedure:", e)
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        return {'result': results, 'params': args}

    def export_to_excel(self, table_names):
        """
        Method to export tables to an Excel file with each table in a separate sheet.
        """
        filename = os.getenv("EXCEL_EXPORT_PATH")
        engine = self.connect()
        if engine is not None:
            try:
                with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                    for table_name in table_names:
                        query = f"SELECT * FROM {table_name}"
                        df = pd.read_sql(query, engine)
                        df.to_excel(writer, sheet_name=table_name, index=False)
                print(f"Data exported to {filename}")
            except SQLAlchemyError as e:
                print("Error exporting to Excel:", e)
        else:
            print("Failed to connect to the database")

# An instance of the DataConexion class is created
data_conexion = DataConexion()
