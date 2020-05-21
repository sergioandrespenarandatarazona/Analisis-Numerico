install.packages("dplyr",dependencies = T)
install.packages("ggplot2",dependencies = T)

library(dplyr)
library(ggplot2)


myf<-function(x,y){
  return(y-x^2+x+1)
}
mydf<-function(x,y){
  return(y-x^2-x+2)
}

taylor<-function(f,df,x,y,h,m){
  u=matrix(rep(0,m*2),ncol = 2)
  for (i in 1:m) {
    y=y+h*f(x,y)+(h^2/2)*df(x,y)
    x=x+h
    u[i,1]=x
    u[i,2]=y
  }
  return (data.frame(u))
}

puntos<-taylor(f=myf,df=mydf,x=0,y=1,h=0.1,m=2)
puntos
#######Comparemos con la solución ######### y(x)=e^x+x+x^2

datos<-data.frame(x=seq(0,1,0.01))
datos<-mutate(datos,x,y=exp(x)+x+x^2)
ggplot(data=datos,aes(x,y))+geom_line()+geom_point(data=puntos,aes(X1,X2),colour="red")


#############################################################################################################

myf<-function(x,y){
  return(2*x-2*y^2-3)
}
mydf<-function(x,y){
  return(2-8*x*y+8*y^3+12*y)
}

taylor<-function(f,df,x,y,h,m){
  u=matrix(rep(0,m*2),ncol = 2)
  for (i in 1:m) {
    y=y+h*f(x,y)+(h^2/2)*df(x,y)
    x=x+h
    u[i,1]=x
    u[i,2]=y
  }
  return (data.frame(u))
}

puntos<-taylor(f=myf,df=mydf,x=0,y=1,h=0.1,m=2)
puntos
#####podemos obtener un bosquejo de la curva solución ampliando los puntos  y haciendo h mas pequeña
######RIccatI se soluciona con una soluci´pion particular 

##probar para 5 10 y 5 puntos y ver la divergencia de la solución

puntosCurva<-taylor(f=myf,df=mydf,x=0,y=1,h=0.1,m=5)
ggplot(puntosCurva,aes(x=X1,y=X2))+geom_point()+geom_line()
