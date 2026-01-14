import sqlite3


DB_NAME = "inventory_system.db"

def get_connection():                     # Function to connect database
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn