import mysql.connector as mysql
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor
conn:MySQLConnection = mysql.connect(
    host="localhost",
    user="robert",
    passwd="clave123",
    database="pydb"
)

cursor:MySQLCursor = conn.cursor()
def insertData():
    print("ingrese un nombre de producto: ")
    name = input()
    print("ingrese el precio del producto: ")
    price = int(input())
    print("ingrese la cantidad de de producto: ")
    quantity = float(input())
    cursor.execute("insert into products(name,price,quantity) values(%s,%s,%s)",(name,price,quantity))
    conn.commit()



print("1) ingresar datos\n2)ver datos")
option = input()
if(option == "1"):
    insertData()
cursor.execute("select * from products")

products = cursor.fetchall()

print("Productos:")
print(products)


cursor.close()
conn.close()
