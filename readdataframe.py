import mysql.connector
import pandas as pd



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="test1"
)

sql = 'select * from predictioninfo limit 5000'

df = pd.read_sql(sql, mydb)
print(df)
