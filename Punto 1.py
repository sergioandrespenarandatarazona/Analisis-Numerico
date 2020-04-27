Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
#Punto 1 /Dados los n + 1 puntos distintos (xi, yi) el polinomio interpolante que incluye a todos los puntos es ´unico
import numpy as np
import sympy as sym

# INGRESO
x = sym.Symbol('x')
fx = sym.cos(x)

#muestras = es los puntos unicos
x0 = 0          
n  = 3  # Grado polinomio Taylor ene este caso utilizaremos de grado 2, pero se puede realizar un cambio

k = 0 # contador de términos
polinomio = 0
while (k <= n):
    derivada   = fx.diff(x,k) #
    derivadax0 = derivada.subs(x,x0)
    divisor   = np.math.factorial(k)
    terminok  = (derivadax0/divisor)*(x-x0)**k
    polinomio = polinomio + terminok
    k = k + 1

print(polinomio)