import mysql.connector

mybanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="mydatabase"
)

mycursor = mybanco.cursor()
#sql = "SELECT name FROM customers ORDER BY name" #ordem alfabética
sql = "SELECT name FROM customers ORDER BY name DESC" #ordem descendente

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)