import mysql.connector

mybanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="mydatabase"
)

mycursor = mybanco.cursor()
sql = "UPDATE customers SET address = 'Manaus, AM' WHERE address = 'Recife, PE'" #fazendo um up de Recife, PE para Manaus, AM
mycursor.execute(sql)
mybanco.commit()
print(mycursor.rowcount, "linha(s) afetada(s).")