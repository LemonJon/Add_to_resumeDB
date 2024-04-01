import mysql.connector
from mysql.connector import Error

def get_db_connection(config):
    """Establishes and returns a database connection."""
    try:
        connection = mysql.connector.connect(**config)
        print("Database connection successful")
        return connection
    except Error as e:
        print(f"Database connection error: {e}")