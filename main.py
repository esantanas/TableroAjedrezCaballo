#Desarrollado por Eduardo Santana Sarmiento 20.786.045-K
from tkinter import*
from tkinter import Canvas
import time
root=Tk()
root.geometry("1920x1080")
root.title("Grafos 2023 - El Problema del Caballo")
opcion=IntVar()
canvas=Canvas(root, width=641, height=641)
canvas.place(x=640, y=320)
#Se crea la ventana de interfaz gráfica, y además se llena una matriz booleana la cuál representa las casillas que han sido ocupadas.
Matriz=[
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True]
]
def Evaluar(i,j, M):
    contador=0
    if 0<=(i+2)<8:
        if 0<=j+1<8:
            if M[i+2][j+1]==True:
                contador=contador+1
        
            
        if 0<=j-1<8:
            if M[i+2][j-1]==True:
                contador=contador+1
        

    if 0<=(i-2)<8:
        if 0<=j+1<8:
            if M[i-2][j+1]==True:
                contador=contador+1
        

        if 0<=j-1<8:
            if M[i-2][j-1]==True:
                contador=contador+1
        
    if 0<=(i+1)<8:
        if 0<=j+2<8:
            if M[i+1][j+2]==True:
                contador=contador+1
        
            
        if 0<=j-2<8:
            if M[i+1][j-2]==True:
                contador=contador+1
        
                
    if 0<=(i-1)<8:
        if 0<=j+2<8:
            if M[i-1][j+2]==True:
                contador=contador+1
        
            
        if 0<=j-2<8:
            if M[i-1][j-2]==True:
                contador=contador+1
    return contador
#En esta función se consideran todos los posibles movimientos de una pieza de caballo, de estar disponible y dentro del tablero, se suma uno al total de opciones disponbles.
def Determinaimayor(Matriz, i, j):
     menor=8
     imayor=0
     jmayor=0
     if 0<=(i+2)<8:
        if 0<=j+1<8:
            if Matriz[i+2][j+1]==True:
                if Evaluar(i+2,j+1,Matriz)<=menor:
                    imayor=i+2
                    jmayor=j+1
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
        if 0<=j-1<8:
            if Matriz[i+2][j-1]==True:
                if Evaluar(i+2,j-1,Matriz)<=menor:
                    imayor=i+2
                    jmayor=j-1
                    menor=Evaluar(imayor,jmayor,Matriz)
        

     if 0<=(i-2)<8:
        if 0<=j+1<8:
            if Matriz[i-2][j+1]==True:
                if Evaluar(i-2,j+1,Matriz)<=menor:

                    imayor=i-2
                    jmayor=j+1
                    menor=Evaluar(imayor,jmayor,Matriz)
        

        if 0<=j-1<8:
            if Matriz[i-2][j-1]==True:
                if Evaluar(i-2,j-1,Matriz)<=menor:
                    imayor=i-2
                    jmayor=j-1
                    menor=Evaluar(imayor,jmayor,Matriz)
        
     if 0<=(i+1)<8:
        if 0<=j+2<8:
            if Matriz[i+1][j+2]==True:
                if Evaluar(i+1,j+2, Matriz)<=menor:
                    imayor=i+1
                    jmayor=j+2
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
        if 0<=j-2<8:
            if Matriz[i+1][j-2]==True:
                if Evaluar(i+1,j-2,Matriz)<=menor:
                    imayor=i+1
                    jmayor=j-2
                    menor=Evaluar(imayor,jmayor,Matriz)

        
                
     if 0<=(i-1)<8:
         
         if 0<=j+2<8:
            if Matriz[i-1][j+2]==True:
                if Evaluar(i-1,j+2,Matriz)<=menor:
                    imayor=i-1
                    jmayor=j-2
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
         if 0<=j-2<8:

            if Matriz[i-1][j-2]==True:
                if Evaluar(i-1,j-2,Matriz)<=menor:
                    imayor=i-1
                    jmayor=j-2
                    menor=Evaluar(imayor,jmayor,Matriz)
    
     return imayor
#En ambas funciones se determina tanto el i como el j mayor, respectivamente.
#Lo que se hace es comparar la cantidad de posibles movimientos que tiene cada posible movimiento de la casilla actual,
# y decantarse por aquella que tenga el menor número de opciones.

def Determinajmayor(Matriz, i, j):
     menor=8
     imayor=0
     jmayor=0
     if 0<=(i+2)<8:
        if 0<=j+1<8:
            if Matriz[i+2][j+1]==True:
                if Evaluar(i+2,j+1,Matriz)<=menor:
                    imayor=i+2
                    jmayor=j+1
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
        if 0<=j-1<8:
            if Matriz[i+2][j-1]==True:
                if Evaluar(i+2,j-1,Matriz)<=menor:
                    imayor=i+2
                    jmayor=j-1
                    menor=Evaluar(imayor,jmayor,Matriz)
        

     if 0<=(i-2)<8:
        if 0<=j+1<8:
            if Matriz[i-2][j+1]==True:
                if Evaluar(i-2,j+1,Matriz)<=menor:

                    imayor=i-2
                    jmayor=j+1
                    menor=Evaluar(imayor,jmayor,Matriz)
        

        if 0<=j-1<8:
            if Matriz[i-2][j-1]==True:
                if Evaluar(i-2,j-1,Matriz)<=menor:
                    imayor=i-2
                    jmayor=j-1
                    menor=Evaluar(imayor,jmayor,Matriz)
        
     if 0<=(i+1)<8:
        if 0<=j+2<8:
            if Matriz[i+1][j+2]==True:
                if Evaluar(i+1,j+2, Matriz)<=menor:
                    imayor=i+1
                    jmayor=j+2
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
        if 0<=j-2<8:
            if Matriz[i+1][j-2]==True:
                if Evaluar(i+1,j-2,Matriz)<=menor:
                    imayor=i+1
                    jmayor=j-2
                    menor=Evaluar(imayor,jmayor,Matriz)

        
                
     if 0<=(i-1)<8:
         
         if 0<=j+2<8:
            if Matriz[i-1][j+2]==True:
                if Evaluar(i-1,j+2,Matriz)<=menor:
                    imayor=i-1
                    jmayor=j+2
                    menor=Evaluar(imayor,jmayor,Matriz)
        
            
         if 0<=(j-2)<8:

            if Matriz[i-1][j-2]==True:
                if Evaluar(i-1,j-2,Matriz)<=menor:
                    imayor=i-1
                    jmayor=j-2
                    menor=Evaluar(imayor,jmayor,Matriz)
    
     return jmayor

#En orden de aligerar el código, se han hecho funciones para los movimientos
def MoverIzq(nombre="w"):
    for l in range(16):
        canvas.move(nombre, -5, 0)
        root.update()
        time.sleep(0.05)
def MoverDer(nombre="w"):
    for l in range(16):
        canvas.move(nombre, 5, 0)
        root.update()
        time.sleep(0.05)
def MoverArriba(nombre="w"):
    for l in range(16):
        canvas.move(nombre, 0, -5)
        root.update()
        time.sleep(0.05)
def MoverAbajo(nombre="w"):
    for l in range(16):
        canvas.move(nombre, 0, 5)
        root.update()
        time.sleep(0.05)



def Recorrer():
    
    U=[
        [1,2,3,4,5,6,7,8],
        [9,10,11,12,13,14,15,16],
        [17,18,19,20,21,22,23,24],
        [25,26,27,28,29,30,31,32],
        [33,34,35,36,37,38,39,40],
        [41,42,43,44,45,46,47,48],
        [49,50,51,52,53,54,55,56],
        [57,58,59,60,61,62,63,64]
        ]

    num=opcion.get()
   
   
    for i1 in range(8):
        for j1 in range(8):
            if num==U[i1][j1]:
                i=i1
                j=j1
                break
    canvas.create_polygon(80*j+20,80*i+10, 80*j+20, 80*i+60,80*j+70 , 80*i+35, fill="Black", tags="caballo")
    Matriz[i][j]=False
    imayor=Determinaimayor(Matriz,i,j)
    jmayor=Determinajmayor(Matriz,i,j)
    for y in range(63):
        time.sleep(0.5)
        #Determinamos qué movimiento hará el caballo, y en orden de ello se hace la respectiva animación, y se cambia la posición actual de la matriz
        if imayor-i==2 and jmayor-j==1:
            MoverAbajo("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverAbajo("caballo")
            MoverDer("caballo")
            Matriz[imayor][jmayor]=False
            
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==2 and jmayor-j==-1:
            MoverAbajo("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverAbajo("caballo")
            MoverIzq("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        
        elif imayor-i==1 and jmayor-j==2:
            MoverAbajo("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverDer("caballo")
            MoverDer("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==1 and jmayor-j==-2:
            MoverAbajo("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverIzq("caballo")
            MoverIzq("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==-2 and jmayor-j==1:
            MoverArriba("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverArriba("caballo")
            MoverDer("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==-2 and jmayor-j==-1:
            MoverArriba("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverArriba("caballo")
            MoverIzq("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==-1 and jmayor-j==2:
            MoverArriba("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverDer("caballo")
            MoverDer("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)
        elif imayor-i==-1 and jmayor-j==-2:
            MoverArriba("caballo")
            canvas.create_rectangle(j*80+25, i*80+25, j*80+55, i*80+55, fill="Green")
            canvas.create_text(j*80+40,i*80+40, text=f"{y+1}")
            MoverIzq("caballo")
            MoverIzq("caballo")
            Matriz[imayor][jmayor]=False
            i=imayor
            j=jmayor
            imayor=Determinaimayor(Matriz,i,j)
            jmayor=Determinajmayor(Matriz,i,j)

    canvas.create_text(j*80+40, i*80+40,text=f"{64}",fill="green")


        

   
    
    
boton=Button(root, text="Comenzar!", command=Recorrer, bd=3)
boton.place(x=310, y=300)

label=Label(root, text="Por favor, selecciona la casilla desde la cual deseas comenzar:")
x1=Radiobutton(text="A1", value=1, variable=opcion)
x2=Radiobutton(text="B1", value=2, variable=opcion)
x3=Radiobutton(text="C1", value=3, variable=opcion)
x4=Radiobutton(text="D1", value=4, variable=opcion)
x5=Radiobutton(text="E1", value=5, variable=opcion)
x6=Radiobutton(text="F1", value=6, variable=opcion)
x7=Radiobutton(text="G1", value=7, variable=opcion)
x8=Radiobutton(text="H1", value=8, variable=opcion)
x9=Radiobutton(text="A2", value=9, variable=opcion)
x10=Radiobutton(text="B2", value=10, variable=opcion)
x11=Radiobutton(text="C2", value=11, variable=opcion)
x12=Radiobutton(text="D2", value=12, variable=opcion)
x13=Radiobutton(text="E2", value=13, variable=opcion)
x14=Radiobutton(text="F2", value=14, variable=opcion)
x15=Radiobutton(text="G2", value=15, variable=opcion)
x16=Radiobutton(text="H2", value=16, variable=opcion)
x17=Radiobutton(text="A3", value=17, variable=opcion)
x18=Radiobutton(text="B3", value=18, variable=opcion)
x19=Radiobutton(text="C3", value=19, variable=opcion)
x20=Radiobutton(text="D3", value=20, variable=opcion)
x21=Radiobutton(text="E3", value=21, variable=opcion)
x22=Radiobutton(text="F3", value=22, variable=opcion)
x23=Radiobutton(text="G3", value=23, variable=opcion)
x24=Radiobutton(text="H3", value=24, variable=opcion)
x25=Radiobutton(text="A4", value=25, variable=opcion)
x26=Radiobutton(text="B4", value=26, variable=opcion)
x27=Radiobutton(text="C4", value=27, variable=opcion)
x28=Radiobutton(text="D4", value=28, variable=opcion)
x29=Radiobutton(text="E4", value=29, variable=opcion)
x30=Radiobutton(text="F4", value=30, variable=opcion)
x31=Radiobutton(text="G4", value=31, variable=opcion)
x32=Radiobutton(text="H4", value=32, variable=opcion)
x33=Radiobutton(text="A5", value=33, variable=opcion)
x34=Radiobutton(text="B5", value=34, variable=opcion)
x35=Radiobutton(text="C5", value=35, variable=opcion)
x36=Radiobutton(text="D5", value=36, variable=opcion)
x37=Radiobutton(text="E5", value=37, variable=opcion)
x38=Radiobutton(text="F5", value=38, variable=opcion)
x39=Radiobutton(text="G5", value=39, variable=opcion)
x40=Radiobutton(text="H5", value=40, variable=opcion)
x41=Radiobutton(text="A6", value=41, variable=opcion)
x42=Radiobutton(text="B6", value=42, variable=opcion)
x43=Radiobutton(text="C6", value=43, variable=opcion)
x44=Radiobutton(text="D6", value=44, variable=opcion)
x45=Radiobutton(text="E6", value=45, variable=opcion)
x46=Radiobutton(text="F6", value=46, variable=opcion)
x47=Radiobutton(text="G6", value=47, variable=opcion)
x48=Radiobutton(text="H6", value=48, variable=opcion)
x49=Radiobutton(text="A7", value=49, variable=opcion)
x50=Radiobutton(text="B7", value=50, variable=opcion)
x51=Radiobutton(text="C7", value=51, variable=opcion)
x52=Radiobutton(text="D7", value=52, variable=opcion)
x53=Radiobutton(text="E7", value=53, variable=opcion)
x54=Radiobutton(text="F7", value=54, variable=opcion)
x55=Radiobutton(text="G7", value=55, variable=opcion)
x56=Radiobutton(text="H7", value=56, variable=opcion)
x57=Radiobutton(text="A8", value=57, variable=opcion)
x58=Radiobutton(text="B8", value=58, variable=opcion)
x59=Radiobutton(text="C8", value=59, variable=opcion)
x60=Radiobutton(text="D8", value=60, variable=opcion)
x61=Radiobutton(text="E8", value=61, variable=opcion)
x62=Radiobutton(text="F8", value=62, variable=opcion)
x63=Radiobutton(text="G8", value=63, variable=opcion)
x64=Radiobutton(text="H8", value=64, variable=opcion)
#Se definen y configuran los botones
label.place(x=180, y=20)
x1.place(x=90, y=60)
x2.place(x=160,y=60)
x3.place(x=240, y=60)
x4.place(x=310, y=60)
x5.place(x=380, y=60)
x6.place(x=450, y=60)
x7.place(x=520, y=60)
x8.place(x=590, y=60)

x9.place(x=90, y=90)
x10.place(x=160,y=90)
x11.place(x=240, y=90)
x12.place(x=310, y=90)
x13.place(x=380, y=90)
x14.place(x=450, y=90)
x15.place(x=520, y=90)
x16.place(x=590, y=90)

x17.place(x=90, y=120)
x18.place(x=160,y=120)
x19.place(x=240, y=120)
x20.place(x=310, y=120)
x21.place(x=380, y=120)
x22.place(x=450, y=120)
x23.place(x=520, y=120)
x24.place(x=590, y=120)

x25.place(x=90, y=150)
x26.place(x=160,y=150)
x27.place(x=240, y=150)
x28.place(x=310, y=150)
x29.place(x=380, y=150)
x30.place(x=450, y=150)
x31.place(x=520, y=150)
x32.place(x=590, y=150)

                                
x33.place(x=90, y=180)
x34.place(x=160,y=180)
x35.place(x=240, y=180)
x36.place(x=310, y=180)
x37.place(x=380, y=180)
x38.place(x=450, y=180)
x39.place(x=520, y=180)
x40.place(x=590, y=180)

x41.place(x=90, y=210)
x42.place(x=160,y=210)
x43.place(x=240, y=210)
x44.place(x=310, y=210)
x45.place(x=380, y=210)
x46.place(x=450, y=210)
x47.place(x=520, y=210)
x48.place(x=590, y=210) 

x49.place(x=90, y=240)
x50.place(x=160,y=240)
x51.place(x=240, y=240)
x52.place(x=310, y=240)
x53.place(x=380, y=240)
x54.place(x=450, y=240)
x55.place(x=520, y=240)
x56.place(x=590, y=240) 

x57.place(x=90, y=270)
x58.place(x=160,y=270)
x59.place(x=240, y=270)
x60.place(x=310, y=270)
x61.place(x=380, y=270)
x62.place(x=450, y=270)
x63.place(x=520, y=270)
x64.place(x=590, y=270)

#Se pinta el tablero
for i in range(8):
     for j in range(8):
         if i%2==0:
             if (j%2==0 and i%2==0):
                 canvas.create_rectangle((j*80)+1, (i*80)+1, (j+1)*80, (i+1)*80, fill="#dfc07f")
             else:
                 canvas.create_rectangle((j*80)+1, (i*80)+1, (j+1)*80, (i+1)*80, fill="#7a4f37")
         elif(i%2!=0):
             if(j%2!=0 and i%2!=0):
                 canvas.create_rectangle((j*80)+1, (i*80)+1, (j+1)*80, (i+1)*80, fill="#dfc07f")
             else:
                 canvas.create_rectangle((j*80)+1, (i*80)+1, (j+1)*80, (i+1)*80, fill="#7a4f37")
        
        


root.mainloop()