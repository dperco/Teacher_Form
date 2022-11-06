import mysql.connector

cnn=mysql.connector.connect(host="localhost",user="root",passwd="12345678",database="colegio")

cur= cnn.cursor()

cur.execute("SELECT * FROM alumnos")
datos = cur.fetchall()

for fila in datos:
    print(fila)



#print(cnn)



