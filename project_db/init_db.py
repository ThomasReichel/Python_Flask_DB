from flask import Flask
import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

sql_anweisung = """ 
        CREATE TABLE IF NOT EXISTS artikel ( 
                    bezeichnung VARCHAR(20),  
                    notiz VARCHAR(30),  
                    anzahl INTEGER 
); 
"""

cursor.execute(sql_anweisung)

conn.commit()
conn.close()