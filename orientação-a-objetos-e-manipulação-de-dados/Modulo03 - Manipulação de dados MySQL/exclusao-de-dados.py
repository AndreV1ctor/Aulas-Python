import mysql.connector

mybanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="mydatabase"
)

mycursor = mybanco.cursor()
sql = "DROP TABLE customers" #Deleta todas as informações contidas na tabela.

mycursor.execute(sql)
print("Tabela excluída com sucesso")