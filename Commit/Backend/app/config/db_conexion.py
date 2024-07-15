import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

class DataConexion:
    def connect(self):
        """
        Method to create and return a connection to the database.

        - Uses environment variables to obtain connection information.
        - Returns a connection object.
        """
        try:
            host = os.getenv("DB_HOST")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASSWORD")
            database = os.getenv("DB_NAME")

            conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if conexion.is_connected():
                print("Welcome to the database!")
                return conexion
            else:
                print("Could not connect to database: incorrect connection parameters or database not found")
                return None
        
        except Error as e:
            print("Critical database connection error: Database server is not available or parameters are incorrect", e)
            return None

    def execute_procedure(self, procedure_name, params=[]):
        """
        Method for executing a stored procedure that returns results.

        - procedure_name: Name of the stored procedure to execute.
        - params: List of parameters for the stored procedure.

        Returns a dictionary with the results and the parameters used.
        """
        results = []
        args = params
        cnn = self.connect()
        if cnn is not None:
            try:
                cursor = cnn.cursor(dictionary=True)
                cursor.callproc(procedure_name, params)

                # We go through the results of the stored procedure
                for result in cursor.stored_results():
                    results.append(result.fetchall())
                
                cnn.commit()

            except Error as e:
                print(e)
            finally:
                if cnn and cnn.is_connected():
                    cursor.close()
                    cnn.close()
            return {'result': results, 'params': args}
        else:
            return {'result': [], 'params': args}

# An instance of the DataConexion class is created
data_conexion = DataConexion
