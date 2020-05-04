# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
"Punto 1"
"Teniendo en cuenta que en la regla de los trapecios, estime el número mínimo de
"trapecios para aproximar ∫ sin2𝑥𝑑𝑥 2
"0
", con tolerancia: 0.0001.

""
import sympy as sp 
import numpy as np
def main():
    cantPoints = input("Ingrese cantidad de puntos conocidos > ")\
 
    if cantPoints < 2:
        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"
        main()\
 
    points = [[sp.sin(2)],[2]]
    integs = []
 
    for i in range(cantPoints):
        print "\n( x",i,",y",i,")"
        x = float(input("Ingrese 'x' > "))
        y = float(input("Ingrese 'y' > "))
        points[0].append(x)
        points[1].append(y)
 
    for i in range(cantPoints-1):
        integ = ((points[0][i+1]-points[0][i])/2)*(points[1][i]+points[1][i+1])
        integs.append(integ)
 
    print "\nIntegral: ",sum(integs)
    raw_input()
 
main()


"Punto 2"
"Dados los siguientes puntos: Utilicé la fórmula de Simpson para encontrar una aproximación del área bajo la
"curva y calculé su error.
"-Qué resultado se obtendría si utilizamos la regla del trapecio
"-Utilice la siguiente metodología: a. Primero interpole y encuentre f(x); b. Integre
"utilizando un método analítico"

import numpy as np
 
def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a
 
def lagrange(A,n):
    results = []
    lfun = np.arange((len(A[0]))**2,dtype=float)
    lfun.shape = (len(A[0]),len(A[0]))\
 
    for i in range(len(A[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:   lfun[i,j] = (n-A[0][j])/(A[0][i]-A[0][j])\
 
    for i in range(len(A[1])):
        results.append(prod(lfun[i])*A[1][i])\
 
    return sum(results)
 
def main():
    cantPoints = input("Ingrese cantidad de puntos conocidos> ")\
 
    if cantPoints < 2:
        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"
        main()\
 
    integs = []
    points = [[],[]]
    midPoints = [[],[]]\
 
    for i in range(cantPoints):
        print "\n( x",i,",y",i,")"
        x = float(input("Ingrese 'x'> "))
        y = float(input("Ingrese 'y'> "))
        points[0].append(x)
        points[1].append(y)\
 
    for i in range(len(points[0])-1):
        midPoints[0].append((points[0][i+1]+points[0][i])/2)
        midPoints[1].append(lagrange(points,midPoints[0][i]))\
 
    for i in range(len(midPoints[0])):
        intg = ((points[0][i+1]-points[0][i])/6)*\
               (points[1][i]+(4*midPoints[1][i])+points[1][i+1])
        integs.append(intg)\
 
    print "\n\tIntegral: ",sum(integs)
    raw_input()
 
print "\n\tREGLA DE SIMPSON\n\n"
main()

"Punto 3
"Con la fórmula de Simpson integrar iterativamente ∫ √1 + 𝑐𝑜𝑠2𝑥𝑑𝑥 2
"0
"hasta que el
"error de truncamiento sea menor de 0.0001. 

import numpy as np
 
def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a
 
def lagrange(A,n):
    results = []
    lfun = np.arange((len(A[0]))**2,dtype=float)
    lfun.shape = (len(A[0]),len(A[0]))\
 
    for i in range(len(A[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:   lfun[i,j] = (n-A[0][j])/(A[0][i]-A[0][j])\
 
    for i in range(len(A[1])):
        results.append(prod(lfun[i])*A[1][i])\
 
    return sum(results)
 
def main():
    cantPoints = input("Ingrese cantidad de puntos conocidos> ")\
 
    if cantPoints < 2:
        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"
        main()\
 
    integs = []
    points = [[],[]]
    midPoints = [[],[]]\
 
    for i in range(cantPoints):
        print "\n( x",i,",y",i,")"
        x = float(input("Ingrese 'x'> "))
        y = float(input("Ingrese 'y'> "))
        points[0].append(x)
        points[1].append(y)\
 
    for i in range(len(points[0])-1):
        midPoints[0].append((points[0][i+1]+points[0][i])/2)
        midPoints[1].append(lagrange(points,midPoints[0][i]))\
 
    for i in range(len(midPoints[0])):
        intg = ((points[0][i+1]-points[0][i])/6)*\
               (points[1][i]+(4*midPoints[1][i])+points[1][i+1])
        integs.append(intg)\
 
    print "\n\tIntegral: ",sum(integs)
    raw_input()
 
print "\n\tREGLA DE SIMPSON\n\n"
main()

"Punto 4
"Utilice la fórmula de la cuadratura de Gauss para aproximar ∫ 𝑥𝑒
"𝑥𝑑
 import math
from sympy import *
 
x = Symbol('x')
y = Symbol('y')
 
def rodrigues(n):   # Aqui 'n' es el grado del polinomio de Legendre
    y = (x**2 - 1)**n
    pol = diff(y,x,n)/(2**n * math.factorial(n)) # Fórmula de Rodrigues
    return pol
 
def main():
    func = raw_input("Ingrese funcion (y = ...) > ")
    A = float(input("Ingrese 'a' de rango  de integración (a<->b) > "))
    B = float(input("Ingrese 'b' de rango  de integración (a<->b) > "))
    n = input("Ingrese 'n' (n >= 2) > ")\
 
    file = open("data.py", "w")
    file.close()
    file = open("data.py", "a")
    file.write("import math\n")
    file.write("from sympy import *\n")
    file.write("x = Symbol('x')\n")
    file.write("y = Symbol('y')\n")
    file.write(func)
    file.close()\
 
    xIpots = solve(rodrigues(n), x) # Raices de polinomios de Legendre
    LePolD = diff(rodrigues(n))     # Derivada de polinomios de Legendre
    Cis = []
    DataFSum = [[],[]]\
 
    import data\
 
    for i in range(n):
        Cis.append(2/((1-xIpots[i]**2)*(LePolD.evalf(subs={x:xIpots[i]}))**2))
        DataFSum[0].append(data.y.evalf(subs={x:(B-A)*(xIpots[i]/2)+(A+B)/2}))
        DataFSum[1].append(Cis[i]*DataFSum[0][i])\
 
    cuad = ((B-A)/2)*sum(DataFSum[1])
    exac = (integrate(data.y,x).evalf(subs={x:B}))-(integrate(data.y,x).evalf(subs={x:A}))
    erro = abs((exac-cuad)*100)
    print "\nResultado de cuadratura: ...", cuad
    print "Resultado exacto : .........", exac
    print "Porcentaje de Error: .......", erro
    raw_input("\nENTER para Salir...")
 
print "\n\tCUADRATURA DE GAUSS\n"
main()



"Punto 5
"Utilice la misma fórmula de cuadratura de Gauss, pero particione la integral de la
"siguiente manera ∫ 𝑥𝑒 𝑥𝑑𝑥 2 1 = ∫ 𝑥𝑒 𝑥𝑑𝑥 1.5 1 + ∫ 𝑥𝑒 𝑥𝑑𝑥 2 1.5 mejoró el resultado?

import math
from sympy import *
 
x = Symbol('x')
y = Symbol('y')
 
def rodrigues(n):   # Aqui 'n' es el grado del polinomio de Legendre
    y = (x**2 - 1)**n
    pol = diff(y,x,n)/(2**n * math.factorial(n)) # Fórmula de Rodrigues
    return pol
 
def main():
    func = raw_input("Ingrese funcion (y = ...) > ")
    A = float(input("Ingrese 'a' de rango  de integración (a<->b) > "))
    B = float(input("Ingrese 'b' de rango  de integración (a<->b) > "))
    n = input("Ingrese 'n' (n >= 2) > ")\
 
    file = open("data.py", "w")
    file.close()
    file = open("data.py", "a")
    file.write("import math\n")
    file.write("from sympy import *\n")
    file.write("x = Symbol('x')\n")
    file.write("y = Symbol('y')\n")
    file.write(func)
    file.close()\
 
    xIpots = solve(rodrigues(n), x) # Raices de polinomios de Legendre
    LePolD = diff(rodrigues(n))     # Derivada de polinomios de Legendre
    Cis = []
    DataFSum = [[],[]]\
 
    import data\
 
    for i in range(n):
        Cis.append(2/((1-xIpots[i]**2)*(LePolD.evalf(subs={x:xIpots[i]}))**2))
        DataFSum[0].append(data.y.evalf(subs={x:(B-A)*(xIpots[i]/2)+(A+B)/2}))
        DataFSum[1].append(Cis[i]*DataFSum[0][i])\
 
    cuad = ((B-A)/2)*sum(DataFSum[1])
    exac = (integrate(data.y,x).evalf(subs={x:B}))-(integrate(data.y,x).evalf(subs={x:A}))
    erro = abs((exac-cuad)*100)
    print "\nResultado de cuadratura: ...", cuad
    print "Resultado exacto : .........", exac
    print "Porcentaje de Error: .......", erro
    raw_input("\nENTER para Salir...")
 
print "\n\tCUADRATURA DE GAUSS\n"
main()


"Punto 6
"Utilice el siguiente código de la regla de Simpson en dos direcciones (para integrales
"dobles) para resolver el siguiente problema:
"Un lago tiene una forma que aproximadamente es rectangular. Las dimensiones son
"200 metros de ancho por 400 metros de largo. Se realiza una partición (grilla) para
"estimar aproximadamente la profundidad en metros en cada cuadricula de la malla
"como se muestra en la siguiente tabla de datos. Utilice los datos para estimar el
"volumen aproximado de agua que contiene el lago 

from sympy import*
from simpson import*
def simpson2(f,ax,bx,ay,by,mx,my):
        x = Symbol("x")
        dy = (by - ay)/my
        v = ay
        r=[400]
        for i in range (0,my+1):
            def g(x): return f(x,v)
            u = simpson(g,ax,bx,mx)
            r = r+[u]
            v = v + dy
        s = 0
        for 1 in range (1, my):
                s = s + 2(2-(i+1)%2)*r[1]
            s = dy/3*(r[0]+ s+r[my])
            return s