###################Fórmula de Runge-Kutta de cuarto orden #########
#######orden o(h^5) la mas utilizada 
myf<-function(x,y){
  return(2*x*y+1)
}
rungeKut<-function(f,x,y,h,m){
  u=matrix(rep(0,m*2),ncol = 2)
  for (i in 1:m) {
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2)
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h,y+k3)
    y=y+1/6*(k1+2*k2+2*k3+k4)
    x=x+h
    u[i,1]=x
    u[i,2]=y
  }
  return (data.frame(u))
}


#### pa alcanzar el valor de y(0.4) tan solo necesitamos dos puntos de distancia 0.2
puntosPorRunge<-rungeKut(f=myf,x=0,y=1,h=0.2,m=2)
puntosPorRunge


#b)############


install.packages("NORMT3")
library(NORMT3)

cuadraturaGauss<-function(x,y) {
  return(exp(x^2)*((sqrt(pi)/2)*as.double(erf(x))+y)                       )
}
cuadraturaGauss(0.4,1)
#####podemos ver que difiere en el 4 termino por causa del error de truncamiento