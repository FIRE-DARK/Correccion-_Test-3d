"""
Esta es la corrección del progra Test_3d
Autor: Daniel Norberto hernández Santiago
Fecha:01/02/2021

"""

#se hacen las importaciones a utilizar
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, sqrt


#se ponen los ejes que se mostraran en el plano
plt.axis([0,150,100,0])
plt.axis('on')
plt.grid(True)
#Pedirle al usuario que proporcione las coordenadas del hit point o ingresar el número de control 
# para finalizar el programa 
while True:
    dec=input('para ingresar el hitpoint presione enter, para salir del programa ingrese en número de control 18390015: ')
    if dec=='18390015':
        break
    else:
        xx=float(input('dame x'))
        yy=float(input('dame y'))
        x=[40,30,80,xx] #———coordenadas del plano
        y=[60,10,60,yy]
        z=[0,0,0,0]
       #——área de etiqueta A(en esta parte se crea el triangulo principal o base)
        plt.plot([x[0],x[1]],[y[0],y[1]],color='k')
        plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
        plt.plot([x[2],x[0]],[y[2],y[0]],color='k')
        plt.scatter(x[3],y[3],s=20,color='r')#este es el punto que nos indica donde esta el hitpoint
        #plot área del triangulo A1,A2
        plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='r') 
        plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color='r')
        plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color='r')
        #esta parte muestra los números en los lados de las esquinas de los triángulos
        plt.text(35,63,'0') 
        plt.text(25,10,'1')
        plt.text(83,63,'2')
        plt.text(x[3]+2,y[3],'3')
        #en esta parte se hace el calculo de las dimensiones que se utilizaran para los triangulos
        a=x[1]-x[0] 
        b=y[1]-y[0]
        c=z[1]-z[0]
        Q01=sqrt(a*a+b*b+c*c)
        a=x[2]-x[1]
        b=y[2]-y[1]
        c=z[2]-z[1]
        Q12=sqrt(a*a+b*b+c*c)

        a=x[2]-x[0]
        b=y[2]-y[0]
        c=z[2]-z[0]
        Q02=sqrt(a*a+b*b+c*c)
        a=x[1]-x[3]
        b=y[1]-y[3]
        c=z[1]=z[3]
        Q13=sqrt(a*a+b*b+c*c)

        a=x[2]-x[3]
        b=y[2]-y[3]
        c=z[2]-z[3]
        Q23=sqrt(a*a+b*b+c*c)

        a=x[0]-x[3]
        b=y[0]-y[3]
        c=z[0]-z[3]
        Q03=sqrt(a*a+b*b+c*c)
        #Se hace el  cálculo de las áreas A, A1 y A2 por medio fórmula de Heron(s=(a+b+c)/2
        #A=raizcuadrada(s(s-a)(s-b)(s-c))
        s=(Q01+Q12+Q02)/2 
        A=sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))
        s1=(Q01+Q03+Q13)/2
        A1=sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))

        s2=(Q02+Q23+Q03)/2
        A2=sqrt(s2*(s2-Q02 )*(s2-Q23)*(s2-Q03))
        plt.arrow(70,55,10,15,linewidth=.5,color='grey') #——etiqueta que indica donde se posiciona el área A
        plt.text(82,73,'A',color='k')
        # se imprimen las etiqueta de A,A1,A2,A1+A2 con sus respectivos resultados 
        plt.text(100,40,'A=')
        dle='%7.0f'% (A)
        dls=str(dle)
        plt.text(105,40,dls)

        plt.text(100,45,'A1=',color='r')
        dle='%7.0f'% (A1)
        dls=str(dle)
        plt.text(105,45,dls)
        plt.text(100,50,'A2=',color='r')
        dle='%7.0f'% (A2)
        dls=str(dle)
        plt.text(105,50,dls)
        plt.text(91,55,'A1+A2=',color='r')
        dle='%7.0f'% (A1+A2)
        dls=str(dle)
        plt.text(106,55,dls)
        plt.text(100,40,'A=')
        dle='%7.0f'% (A)
        dls=str(dle)
        plt.text(105,40,dls)
        plt.text(100,45,'A1=',color='r')
        dle='%7.0f'% (A1)
        dls=str(dle)
        plt.text(105,45,dls)

        plt.text(100,50,'A2=',color='r')
        dle='%7.0f'% (A2)
        dls=str(dle)
        plt.text(105,50,dls)

        plt.text(91,55,'A1+A2=',color='r')
        dle="%7.0f"% (A1+A2)
        dls=str(dle)
        plt.text(106,55,dls)
        # en esta parte se hace la verificación con la que se determina se el punto esta
        # dentro o fuera de los limites
        if A1+A2 > A:
            plt.text(70,83,'El punto esta fuera de los limites')
        else:
            plt.text(70,83,'El punto esta dentro de los limites')

        plt.show()