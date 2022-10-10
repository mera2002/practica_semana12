#Integrantes:
""" Merary Julissa Araujo Velasquez """
""" Nathaly Sarai Rodriguez Silva """

#como funciona: 
""" el usuario se debera de registrar con su correo y contraseña previamente creada """
""" luego en la ventana principal podra redactar el correo al destinatario que desee"""
""" si el usuario no ha sido registrado o los campos en el formulario del 
envio del correo estan vacios no emitira un mensaje de fallo, sino un mensaje que ha sido enviado con exito"""

from queue import Empty
import smtplib
from tkinter import  Label,Entry,Button,Tk,Text,messagebox

#clase interfaz, donde definimos las ventanas principal y de registro 
class interfaz():
    def __init__(self):
        self.usuario = ""
        self.contra = ""
        self.Usuarios = Empty
        self.entradaPass = Empty
        self.emisor = Empty
        self.reseptor = Empty
        self.mensaje = Empty
        self.ventanaPrin = Empty
        self.ventana2 = Empty
    
    def ventanas(self):
        #ventana de registro
        ventana2 = Tk()
        ventana2.title("Registro")  #titulo 
        #definicion de dimensiones 
        ancho_ventana = 500 
        alto_ventana = 300

        x_ventana = ventana2.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana2.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana2.geometry(posicion)

        ventana2.resizable(0,0)
        ventana2.configure(background='Plum') #color de la ventana de registro 

#Definicion de los controles(color, texto, tipo de letra) y sus funciones
        lb1 = Label(ventana2,text="Registrarse.",bg='Lavender',font='Calibri  16 bold')
        lb1.pack()
        lb2 = Label(ventana2,text="Correo:",bg='Lavender',font='Calibri  12 bold')
        lb2.place(x=50,y=80)
        self.Usuarios  = Entry(ventana2)
        self.Usuarios.place(x=200,y=80,width=200)
        lb2 = Label(ventana2,text="Contraseña:",bg='Lavender',font='Calibri  12 bold')
        lb2.place(x=50,y=120)
        self.entradaPass = Entry(ventana2)
        self.entradaPass.place(x=200,y=120,width=200)
        btn = Button(ventana2,text="Registrarse",command=clase.ventana_registro,bg='Lavender',font='Calibri 12 bold',fg="black")
        btn.place(x=150,y=200)
        btn2 = Button(ventana2,text="Atrás ",command=clase.ventana_principal,bg='Lavender',font='Calibri 12 bold',fg="black")
        btn2.place(x=280,y=200)
        self.ventanaPrin.destroy()
        self.ventana2 = ventana2
        ventana2.mainloop()

#Metodo que nos permitira enviar el mensaje si el usuario esta registrado, sino l pedira que lo haga 
    def enviar(self):
        if self.emisor.get() == "" and self.receptor.get()=="" and self.usuario == "" and self.contra == "":
            messagebox.showerror("Enviar Correo","Usuario no registrado. ¡Registrese, por favor!")
        else:
            fromaddr = self.emisor.get() 
            toaddrs = self.receptor.get() 
            mensaj = self.mensaje.get("1.0","end")
            username = self.usuario 
            password = self.contra
        
            try:
                server = smtplib.SMTP('smtp.gmail.com:587') 
                server.starttls() 
                server.login(username,password) 
                server.sendmail(fromaddr, toaddrs, mensaj) 
                server.quit()
                self.receptor.delete(0,"end")
                self.mensaje.delete("1.0","end")
                messagebox.showinfo("Enviar Mensaje","Mensaje enviado con éxito ")
            except:
                messagebox.showerror("Enviar Mensaje","Envio Fallido ")

#metodo de registro
    def ventana_registro(self):
        self.usuario = self.Usuarios.get()
        self.contra = self.entradaPass.get()
        if self.usuario == "" and self.contra == "":
            messagebox.showerror("Registro","Debe llenar todos los campos")
        else:
            
            messagebox.showinfo("Registro","Usuario registrado")
            clase.ventana_principal()
    
#metodo que nos permitira redactar y enviar el correo 
    def ventana_principal(self):
       
        ventana = Tk()
        ventana.title("Enviar Correo")
        ancho_ventana = 500
        alto_ventana = 500

        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)

        ventana.resizable(0,0)
        ventana.configure(background='Plum')

#Definicion de controles (color, texto, tipo de letra), y sus funciones 
        lb1 = Label(ventana,text="Redactar ",bg='Lavender',font='Splash 16 bold')
        lb1.pack()
        lb2 = Label(ventana,text="Destinatario:",bg='Lavender',font='Calibri 12 bold')
        lb2.place(x=50,y=80)
        self.receptor = Entry(ventana)
        self.receptor.place(x=200,y=80,width=200)
        lb2 = Label(ventana,text="Nombre de usuario:",bg='Lavender',font='Calibri 12 bold')
        lb2.place(x=50,y=120)
        self.emisor = Entry(ventana)
        self.emisor.insert(0,self.usuario)
        self.emisor.place(x=200,y=120,width=200)
        lb0 = Label(ventana,text="Redactar correo: ",bg='Lavender',font='Calibri 12 bold')
        lb0.place(x=50,y=160)
        self.mensaje = Text(ventana)
        self.mensaje.place(x=50,y=190,height=200,width=400)
        btn = Button(ventana,text="Enviar mensaje.",command=clase.enviar,bg='Lavender',font='Calibri 14 bold',fg="black")
        btn.place(x=50,y=400)
        btn = Button(ventana,text="Registrarse.",command=clase.ventanas,bg='Lavender',font='Calibri 14 bold',fg="black")
        btn.place(x=250,y=400)
        if self.ventana2 != Empty:
            self.ventana2.destroy()
        
        self.ventanaPrin = ventana
        ventana.mainloop()

clase = interfaz()
clase.ventana_principal()