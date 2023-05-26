from tkinter import *
import random*
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
c.config(bg="cyan")
c.place(x=10, y=10)

"""
#creacion de lineas
c.create_line(x/2,-y,x/2,y,fill="black")
c.create_line(-x,y/2,x,y/2,fill="black")

#arcos
arco_1 = c.create_arc(0,0,x/2,y/2,start=180, extent=180,fill="red")
arco_2 = c.create_arc(0,0,x/2,y/2,start=0, extent=180,fill="blue")
"""
rect1=c.create_rectangle(x/2-100,y,x/2+100,y/2+90,outline="black",fill="orange4")
trian1=c.create_polygon(x/2-20,y-20,x/2+20,y-20,x/2,y/2,outline="black", fill="saddle brown")

#crear un molino 
color = "#"
for i in range(6):
    color = color + random.choice("0123456789ABCDEF")
    
    
    

arco_1 = c.create_arc(x/2-70,y/2-70,x/2+70,y/2+70,start=20, extent=45,outline="black", fill="orange3")
arco_2 = c.create_arc(x/2-70,y/2-70,x/2+70,y/2+70,start=110, extent=45,outline="black", fill="orange3")
arco_3 = c.create_arc(x/2-70,y/2-70,x/2+70,y/2+70,start=200, extent=45,outline="black", fill="orange3")
arco_4 = c.create_arc(x/2-70,y/2-70,x/2+70,y/2+70,start=290, extent=45, outline="black",fill="orange3")

#frame de controles
frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#boton salir
boton_salir = Button(frame_controles, text="Salir", command=ventana_principal.destroy)
boton_salir.place(x=200, y=10)


#desplegar ventana
ventana_principal.mainloop()