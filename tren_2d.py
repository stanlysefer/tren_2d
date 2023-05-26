from tkinter import *

#------------------
#variables globales
#------------------
x= 460
y=220

#-----------------
#VENTANA PRINCIPAL
#-----------------
ventana_principal= Tk()
ventana_principal.title("TREN 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="gold")

#-----------------
#frame graficacion
#-----------------
frame_graficacion=  Frame(ventana_principal)
frame_graficacion.config(bg="green" , width=480 ,height=240)
frame_graficacion.place(x=10 ,y=10)

#creacion canvas
c = Canvas(frame_graficacion, width=x, height=y)
c.config(bg="white")
c.place(x=10, y=10)
""""
#------------------
photo=PhotoImage(file='img/trenSistemas.png')
c.create_image(120, 1, image=photo, anchor=NW)
"""
#creacion del tren
c.create_line(x/2,-y,x/2,y,fill="black")
c.create_line(-x,y/2,x,y/2,fill="black")
c.create_rectangle(x/2+70,y/2,x/2-80,y/2+75,fill="blue")
c.create_rectangle(x/2-10,y/2,x/2+70,y/2-60,fill="red")
c.create_oval(x/2+20,y/2+90,x/2-20,y/2+50,fill="pale green")
c.create_rectangle(x/2,y/2-80,x/2+80,y/2-60,fill="gold")
c.create_rectangle(x/2,y/2-80,x/2-25,y/2-60,fill="gold")
c.create_rectangle(x/2-70,y/2-50,x/2-40,y/2,fill="purple")
c.create_rectangle(x/2-100,y/2+50,x/2-80,y/2+20,fill="blue")
c.create_rectangle(x/2-120,y/2+70,x/2-100,y/2,fill="red")
c.create_rectangle(x/2-80,y/2-50,x/2-30,y/2-30,fill="cyan")
c.create_oval(x/2-70,y/2+90,x/2-30,y/2+50,fill="pale green")
c.create_oval(x/2+30,y/2+90,x/2+70,y/2+50,fill="pale green")
c.create_text(x/2-10,y/2+30, text="Stanly", fill="white",font=("times new roman", 20))
c.create_arc(x/2-150, y/2+60,x/2-90,y/2+10, start=90, extent=180,fill="green")
c.create_rectangle(x/2,y/2-100,x/2+50,y/2-80,fill="blue")
c.create_rectangle(x/2+50,y/2+60,x/2+5,y/2+80,fill="gray")
c.create_rectangle(x/2,y/2+60,x/2-50,y/2+80,fill="gray")
c.create_rectangle(x/2,y/2-5,x/2+60,y/2-55,fill="gray")
c.create_oval(x/2,y/2-5,x/2+60,y/2-55,fill="yellow")
c.create_oval(x/2+10,y/2-30,x/2+30,y/2-40,fill="red")
c.create_oval(x/2+50,y/2-30,x/2+32,y/2-40,fill="red")
c.create_oval(x/2+40,y/2-20,x/2+20,y/2-20,fill="black")

#frame de controles

frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()