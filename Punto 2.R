library(dplyr)
library(ggplot2)

####################Formula de euler###################

##############el orden del error es de O(h^2)=O(0.01)#######
myf<-function(x,y){
  return(2*y-2*x^2+x-3)
}
euler<-function(f,x,y,h,m){
  u=matrix(rep(0,m*2),ncol = 2)
  for (i in 1:m) {
    y=y+h*f(x,y)
    x=x+h
    u[i,1]=x
    u[i,2]=y
  }
  return (data.frame(u))
}

puntosPorEuler<-euler(f=myf,x=0,y=1.2,h=0.1,m=2)
puntosPorEuler
##############Fórmula de Heun###############

#####O(h^3)

myf<-function(x,y){
  return(2*y-2*x^2+x-3)
}
heun<-function(f,x,y,h,m){
  u=matrix(rep(0,m*2),ncol = 2)
  for (i in 1:m) {
    barY=y+h*f(x,y)
    y=y+(h/2)*(f(x,y)+f(x+h,barY))
    x=x+h
    u[i,1]=x
    u[i,2]=y
  }
  return (data.frame(u))
}
puntosPorHeun<-heun(f=myf,x=0,y=1.2,h=0.1,m=2)
puntosPorHeun
###################Fórmula de Runge-Kutta de cuarto orden #########
#######orden o(h^5)=O(0.00001) la mas utilizada 
myf<-function(x,y){
  return(2*y-2*x^2+x-3)
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
puntosPorRunge<-rungeKut(f=myf,x=0,y=1.2,h=0.1,m=2)
puntosPorRunge
##################Comparación y(x)=x/2+x^2-11/20e^(2x)+7/4#######

datos<-data.frame(x=seq(0,1,0.01))
datos<-mutate(datos,x,y=x/2+x^2-(11/20)*exp(2*x)+(7/4))
ggplot(data=datos,aes(x,y))+geom_line()

comparativa<-data.frame(cbind(x=puntosPorEuler[,1],
                              euler=puntosPorEuler[,2],
                              heun=puntosPorHeun[,2],
                              kutta=puntosPorRunge[,2]))
comparativa<-mutate(comparativa,
                    x,
                    Sol_Exac=x/2+x^2-(11/20)*exp(2*x)+(7/4))
comparativa

errores<-mutate(comparativa,
                Dif.euler=abs(euler-Sol_Exac),
                Dif.heun=abs(heun-Sol_Exac),
                Dif.kutta=abs(kutta-Sol_Exac))          
errores









