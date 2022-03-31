import mysql.connector

mybanco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="mydatabase"
)

mycursor = mybanco.cursor()

#sql = "SELECT * FROM customers WHERE address = 'Recife, PE'"
sql = "SELECT * FROM customers WHERE name LIKE '%Ema%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)