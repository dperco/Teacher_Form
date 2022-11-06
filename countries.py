import mysql.connector

class Alumno:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="12345678", database="colegio")

    def __str__(self):
        datos=self.consulta_alumnos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_alumnos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM alumnos")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_alumno(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM alumnos WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_alumno(self,Nombre, Apellido, Materia, Nota,Observaciones):
        cur = self.cnn.cursor()
        sql='''INSERT INTO alumnos (Nombre, Apellido, Materia, Nota,Observaciones) 
        VALUES('{}', '{}', '{}', '{}','{}')'''.format(Nombre, Apellido, Materia,Nota, Observaciones)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_alumno(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM alumnos WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_alumno(self,Id,Nombre, Apellido, Materia,Nota, Observaciones):
        cur = self.cnn.cursor()
        sql='''UPDATE alumnos SET Nombre='{}', Apellido='{}', Materia='{}',Nota='{}',
        Observaciones='{}' WHERE Id={}'''.format(Nombre, Apellido, Materia,Nota, Observaciones,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
