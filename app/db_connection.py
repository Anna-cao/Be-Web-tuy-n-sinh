import pyodbc

def get_connection():
    return pyodbc.connect(
        "Driver={SQL Server};"
        "Server=NGOCHA;"  
        "Database=DuAn;"  
        "Trusted_Connection=yes;"
    )
