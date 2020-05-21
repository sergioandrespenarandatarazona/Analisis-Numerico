# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
#Runge Kutta de cuarto orden para n EDO's 
import sympy as sp 
import numpy as np
import pylab as pl 
def rk4n(F,V,U,h,m):     
    nF=len(F)     
    nV=len(V)     
    K1=np.zeros([nF],dtype=sp.Symbol)     
    K2=np.zeros([nF],dtype=sp.Symbol)     
    K3=np.zeros([nF],dtype=sp.Symbol)     
    K4=np.zeros([nF],dtype=sp.Symbol)     
    rs=np.zeros([m,nV],dtype=float)          
    for p in range(m):         
        for i in range(nF):             
            K1[i]=F[i]             
            K2[i]=F[i]             
            K3[i]=F[i]             
            K4[i]=F[i]         
        for i in range(nF):             
            for j in range(nV):                 
                K1[i]=K1[i].subs(V[j],float(U[j]))             
            K1[i]=h*K1[i]         
        for i in range(nF):             
            K2[i]=K2[i].subs(V[0],float(U[0])+h/2)
            for j in range(1,nV):    
                K2[i]=K2[i].subs(V[j],float(U[j])+K1[j-1]/2)  
            K2[i]=h*K2[i]         
        for i in range(nF): 
            K3[i]=K3[i].subs(V[0],float(U[0])+h/2) 
            for j in range(1,nV):                 
                K3[i]=K3[i].subs(V[j],float(U[j])+K2[j-1]/2)   
            K3[i]=h*K3[i]    
        for i in range(nF):   
            K4[i]=K4[i].subs(V[0],float(U[0])+h) 
            for j in range(1,nV): 
                K4[i]=K4[i].subs(V[j],float(U[j])+K3[j-1])
            K4[i]=h*K4[i] 
        U[0]=U[0]+h
        rs[p,0]=U[0]
        for i in range(nF):
             U[i+1]=U[i+1]+1/6*(K1[i]+2*K2[i]+2*K3[i]+K4[i])
             rs[p,i+1]=U[i+1]
    return rs


#implemetacion
x,y,z=sp.symbols('x,y,z')
f=z
g=z+sp.sin(x)-y-1
rs=rk4n([f,g],[x,y,z],[0,1.5,2.5],0.1,2)
np.set_printoptions(precision=10)
print(rs) 
pl.plot(rs[:,0],rs[:,1:3],'o')   #Gráfico de y(x), z(x) 
pl.grid(True) 
pl.show()

#######Usand Odeint########################}
from scipy.integrate  import odeint 
def fun(v0,x):         #Definición del sistema de EDO         
    y=v0[0]         
    z=v0[1]         
    vec=[z,z+sp.sin(x)-y-1]         
    return vec 
x=pl.arange(0,2.1,0.1) #Variable independiente 
v0=[1.5,2.5]
vsol=odeint(fun,v0,x)  #Vectores solución
pl.plot(x,vsol,'o') #  Gráficos de los vectores 
pl.grid(True)
pl.show()















