from tkinter import *
from tkinter import ttk
from countries import Alumno
from tkinter import messagebox
class Ventana(Frame):

    estudiante= Alumno()
    
    def __init__(self,master=None):
        super().__init__(master,width=880,height=560)
        self.master=master
        self.pack()
        self.create_widgets()
        self.update()
        self.habilitarbox('disabled')
        self.habilitarBtn('normal')
        self.habilitarBtnGuardar('disabled')
        self.id=-1

    def habilitarbox(self,states):
        self.name.configure(state=states)
        self.apellido.configure(state=states)
        self.materia.configure(state=states)
        self.nota.configure(state=states)
        self.obsrv.configure(state=states)

    def habilitarBtn(self,states):
            self.btnNuevo.configure(state=states)
            self.btnModificar.configure(state=states)
            self.btnEliminar.configure(state=states)

    def habilitarBtnGuardar(self,states):
            self.btnGuardar.configure(state=states)
            self.btnCancelar.configure(state=states)
            
        

    def borrar_input(self):
        self.name.delete(0,END)
        self.apellido.delete(0,END)
        self.materia.delete(0,END)
        self.nota.delete(0,END)
        self.obsrv.delete(0,END)

    def limpia_grid(self):
        for item in self.grid.get_children():  
            self.grid.delete(item) 

    def update(self):
         datos=self.estudiante.consulta_alumnos()
         for row in datos:
            #self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row=[4],row[5]))
             self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))

    def fNuevo(self):
        self.habilitarbox("normal")
        self.habilitarBtn("disabled")
        self.habilitarBtnGuardar("normal")
        self.borrar_input()
        self.name.focus()

    def fModificar(self):
        selected=self.grid.focus()
        clave=self.grid.item(selected,'text')
        if clave == '' :
            messagebox.showwarning('Modificar','Debes seleccionar un elemento')
        else:           
           self.id=clave
           self.habilitarbox('normal')
           valores=self.grid.item(selected,'values')
           self.borrar_input()
           self.name.insert(0,valores[0])
           self.apellido.insert(0,valores[1])
           self.materia.insert(0,valores[2])
           self.nota.insert(0,valores[3])
           self.obsrv.insert(0,valores[4])
           self.habilitarBtn('disabled')
           self.habilitarBtnGuardar('normal')
           self.name.focus()
           
           
           

    def fEliminar(self):
        selected=self.grid.focus()
        clave=self.grid.item(selected,'text')
        if clave == '' :
            messagebox.showwarning('Eliminar','Debes seleccionar un elemento')
        else:
           valores=self.grid.item(selected,'values')
           data=str(clave) + ','+valores[0] +','+valores[1]
           r=messagebox.askquestion('Eliminar','Desea eliminar el registro?\n'+ data)        
           if r == messagebox.YES:
              reg=self.estudiante.elimina_alumno(clave)
              if reg == 1:
                    messagebox.showinfo('Eliminar','Elemento eliminado')
                    self.limpia_grid()
                    self.update()
              else:
                    messagebox.showinfo('Eliminar','No se pudo eliminar')
           
                


    def fGuardar(self):
        if self.id == -1:
           self.estudiante.inserta_alumno(self.name.get(),self.apellido.get(),self.materia.get(),self.nota.get(),self.obsrv.get())
           messagebox.showinfo('Insertar','Elemento Insertado')
        else:
           self.estudiante.modifica_alumno(self.id,self.name.get(),self.apellido.get(),self.materia.get(),self.nota.get(),self.obsrv.get())
           messagebox.showinfo('Modificar','Elemento Modificado')
           self.id=-1
        self.limpia_grid()
        self.update()
        self.borrar_input()
        self.habilitarBtnGuardar('disabled')
        self.habilitarBtn('normal')
        self.habilitarbox('disabled')

    def fCancelar(self):
        r=messagebox.askquestion('Cancelar','Esta seguro de cancelar ?')
        if r == messagebox.YES:
            self.borrar_input()
            self.habilitarBtnGuardar('disabled')
            self.habilitarBtn('normal')
            self.habilitarbox('disabled')

            
    def create_widgets(self):
        frame1= Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=259)
        self.btnNuevo= Button(frame1,text="Nuevo",command=self.fNuevo,bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=50, width=80,height=30)
        self.btnModificar= Button(frame1,text="Modificar",command=self.fModificar,bg="blue",fg="white")
        self.btnModificar.place(x=5,y=90,height=30 ,width=80)
        self.btnEliminar= Button(frame1,text="Eliminar",command=self.fEliminar,bg="blue",fg="white")
        self.btnEliminar.place(x=5,y=130,height=30,width=80)

        frame2= Frame(self,bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=259)
        lbl1=Label(frame2,text="Nombre:")
        lbl1.place(x=3,y=5)
        self.name=Entry(frame2)
        self.name.place(x=3,y=25,width=90,height=15)
        lbl2=Label(frame2,text="Apellido:")
        lbl2.place(x=3,y=45)
        self.apellido=Entry(frame2)
        self.apellido.place(x=3,y=70,width=90,height=15)
        lbl3=Label(frame2,text="Materia:")
        lbl3.place(x=3,y=90)
        self.materia=Entry(frame2)
        self.materia.place(x=3,y=110,width=90,height=15)
        lbl4=Label(frame2,text="Nota:")
        lbl4.place(x=3,y=130)
        self.nota=Entry(frame2)
        self.nota.place(x=3,y=150,width=90,height=15)
        lbl4=Label(frame2,text="Observaciones:")
        lbl4.place(x=3,y=170)
        self.obsrv=Entry(frame2)
        self.obsrv.place(x=3,y=190,width=120,height=30)
        self.btnGuardar= Button(frame2,text="Guardar",command=self.fGuardar,bg="blue",fg="white")
        self.btnGuardar.place(x=3,y=230, width=50,height=20)
        self.btnCancelar= Button(frame2,text="Cancelar",command=self.fCancelar,bg="yellow",fg="black")
        self.btnCancelar.place(x=70,y=230, width=50,height=20)

        frame3= Frame(self,bg="yellow")
        frame3.place(x=247,y=0,width=420,height=259)

        self.grid=ttk.Treeview(frame3,columns=("col1","col2","col3","col4","col5"))
        #self.grid.column("#0",width=50)
        self.grid.column("#0",width=30,anchor=CENTER)
        self.grid.column("col1",width=60,anchor=CENTER)
        self.grid.column("col2",width=60,anchor=CENTER)
        self.grid.column("col3",width=60,anchor=CENTER)
        self.grid.column("col4",width=30,anchor=CENTER)
        self.grid.column("col5",width=160,anchor=CENTER)
        self.grid.heading("#0",text="Id")
        self.grid.heading("col1",text="Nombre")
        self.grid.heading("col2",text="Apellido")
        self.grid.heading("col3",text="Materia")
        self.grid.heading("col4",text="Nota")
        self.grid.heading("col5",text="Observaciones")
        self.grid.pack(side=LEFT,fill=Y)
        sb=Scrollbar(frame3,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'


        
