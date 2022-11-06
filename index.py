
from tkinter import ttk
from tkinter import *

import sqlite3


import sqlite3
#conn= sqlite3.connect(host="localhost",user="root",passwd="admin",database="Product")
#print(conn)


class Product :
     db_name='database.db'

     #def  __init__(self,window):
     #    self.wind= window                       #window  panel
     #    self.wind.title('College Application')



         #buttton add
      #   ttk.Button(text='Save',command= self.add_product).grid(row=6,column=2,sticky= W + E)    
    #    #button table
      #   ttk.Button(text='DELETE',command=self.delete_product).grid(row=5,column=1,sticky= W+E)
       #  ttk.Button(text='EDIT',command=self.edit_product).grid(row=5,column=0,sticky= W+E)
    #    # update table
      #   self.get_prod()

     def run_query(self,query,parameters = ()):
         with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
         return result

     
          

     def get_prod(self):
        records=self.tree.get_children() #clear table
        for elements in records:
             self.tree.delete(elements)
        
         #query data
        query= 'SELECT * FROM colegio ORDER BY Name DESC'
        db_rows=self.run_query(query)

    #     # insert in table
        for row in db_rows:
             self.tree.insert('',0,text=row[1],values=row[2])
        print(db_rows)

     def validation(self):  #validate data entry
         return len(self.name.get()) != 0 and len(self.price.get()) !=0


     def add_product(self):
        if self.validation():
           query='INSERT INTO colegio VALUES(NULL,?,?)'
           parameters=(self.name.get(),self.price.get())
           self.run_query(query,parameters)
           self.message['text']= 'Product {} added Successfully'.format(self.name.get())
           self.name.delete(0,END)
           self.price.delete(0,END)
        else:
           self.message['text']= 'Name and Price ara requerid'
           self.get_prod()
    
    # # delete product
     def delete_product(self):       
         self.message['text']=''
         try:
          self.tree.item(self.tree.selection())['text'][0]
         except IndexError as e:
            self.message['text']='Please Select a Record'
            return 
         name =self.tree.item(self.tree.selection())['text']
         query = 'DELETE FROM colegio WHERE name = ?'
         self.run_query(query, (name, ))
         self.message['text']= 'Record {} deleted Succesfully'.format(name)
         self.get_prod()
    
    # # edit product
     def edit_product(self):
         self.message['text']=''
         try:
          self.tree.item(self.tree.selection())['text'][0]
         except IndexError as e:
            self.message['text']='Please Select a Record'
            return
         name = self.tree.item(self.tree.selection())['text']
         old_apellido=self.tree.item(self.tree.selection())['values'][0]
         self.edit_wind= Toplevel()
         self.edit_wind.title='Edit Product'

    #     #old name
         Label(self.edit_wind,text='Old Name:').grid(row=0 , column=1)
         Entry(self.edit_wind,textvariable= StringVar(self.edit_wind, value= name),state='readonly').grid(row=1,column=2)

    #     #new name
         Label(self.edit_wind,text='New Name').grid(row=1,column=1)
         new_name= Entry(self.edit_wind)
         new_name.grid(row=1,column=2)

    #     #old apellido
         Label(self.edit_wind,text='Old Apellido:').grid(row=2 , column=1)
         Entry(self.edit_wind,textvariable= StringVar(self.edit_wind, value= old_apellido),state='readonly').grid(row=2,column=2)

    #     #new apellido
         Label(self.edit_wind,text='New Apellido').grid(row=3,column=1)
         new_apellido= Entry(self.edit_wind)
         new_apellido.grid(row=3,column=2)

    #     # change date
        # Button(self.edit_wind,text='Update',command= lambda: self.edit_record(new_name.get(),name,new_apellido.get(),
         #old_apellido)).grid(row=4,column=2,sticky=W)
    
     def edit_record(self,new_name,name,new_apellido,old_apellido):
         query='UPDATE colegio SET name=? , price=? WHERE name=? AND apellido=?'
         parameters = (new_name,new_apellido,name,old_apellido)
         self.run_query(query,parameters)
         self.edit_wind.destroy()
         self.message['text']= 'Record {} update Successfully'.format(name)
         self.get_prod()

