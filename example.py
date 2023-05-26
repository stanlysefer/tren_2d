from tkinter import *

#------------------
#variables globales
#------------------
BASE = 460
ALTURA=220

#-----------------
#VENTANA PRINCIPAL
#-----------------
ventana_principal= Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#-----------------
#frame graficacion
#-----------------
frame_graficacion=  Frame(ventana_principal)
frame_graficacion.config(bg="green" , width=480 ,height=240)
frame_graficacion.place(x=10 ,y=10)

#creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#dibujar una linea recta
linea_1 = c.create_line(BASE/2 , ALTURA/2 , BASE,0, fill="red", width=2)
linea_2 = c.create_line(BASE , ALTURA , BASE/2 , ALTURA/2, fill="yellow", width=2)
linea_3 = c.create_line(0, ALTURA,BASE/2, ALTURA/2, fill="blue" , width=2)
linea_4 = c.create_line(0,0, BASE/2, ALTURA/2, fill="green",width=2)
linea_5 = c.create_line(230,0, BASE/2, ALTURA/2, fill="white", width=2)
linea_6 = c.create_line(0,110, BASE/2, ALTURA/2, fill="white", width=2)
linea_7 = c.create_line(230,460, BASE/2, ALTURA/2, fill="white", width=2)
linea_8 = c.create_line(230,110, BASE/2, 3*ALTURA/4, fill="white", width=2)

#dibujar texto 
texto_1 = c.create_text(BASE/4, ALTURA/2, anchor="center", text= "Sistemas", font=("Arial",25, "bold"), fill="blue",activefill="yellow")
texto_1 = c.create_text(3*BASE/4, ALTURA/2, anchor="center", text= "Colegio", font=("Arial",25, "bold"), fill="blue",activefill="yellow")
texto_1 = c.create_text(BASE/2, ALTURA/4, anchor="center", text= "Especialidad", font=("Arial",25, "bold"), fill="blue",activefill="yellow")
texto_1 = c.create_text(BASE/2, 3*ALTURA/4, anchor="center", text= "Guanenta", font=("Arial",25, "bold"), fill="blue",activefill="yellow")

#dibujar un rectangulo 

#dibujar un circulo 
circ_1= c.create_oval(BASE/2,0,BASE,ALTURA/2,fill="blue")
circ_2=c.create_oval(0,ALTURA/2,BASE/4,ALTURA,fill="yellow")
circ_3=c.create_oval(BASE/4,ALTURA/2,BASE/2,ALTURA, fill="red")

#dibujar un poligono
polig_1 = c.create_polygon(3*BASE/4,ALTURA/2, BASE, ALTURA,BASE/2,ALTURA, fill="red")
polig_1 = c.create_polygon(BASE/4,0,BASE/2,ALTURA/4,BASE/4,ALTURA/2,0,ALTURA/4, fill="white")
#color de la cruz
cruz = c.create_polygon(BASE/2-25,ALTURA/2-75,BASE/2+25,ALTURA/2-75,BASE/2+25,ALTURA/2-25, BASE/2+75,ALTURA/2-25, BASE/2+75,ALTURA/2+25, BASE/2+25, ALTURA/2+25, BASE/2+25, ALTURA/2+75, BASE/2-25, ALTURA/2+75, BASE/2-25, ALTURA/2+25, BASE/2-75, ALTURA/2+25, BASE/2-75, ALTURA/2-25, BASE/2-25, ALTURA/2-25, fill="white")

#linea vertical
linea_vertical_1 = c.create_line()
linea_vertical_2 = c.create_line(BASE/2+25,ALTURA/2-75,BASE/2+75,ALTURA/2+25,fill="red")
line_horizontal_1 = c.create_line(BASE)
line_horizontal_2 = c.create_line(BASE/2-75,ALTURA/+25,BASE/2+75,ALTURA/2+25,fill="red")

#frame de controles
#------------------
frame_controles=Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#desplegar ventana
ventana_principal.mainloop()