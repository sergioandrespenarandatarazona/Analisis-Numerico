library(dplyr)
library(ggplot2)

####################Formula de euler###################

##############el orden del error es de O(h^2)=O(0.01)#######

myf<-function(x,y){
  return(2*x-5*y+1)
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

puntosPorEuler<-euler(f=myf,x=0,y=2,h=0.1,m=10)
puntosPorEuler
###################Gráfica########################
datos<-data.frame(x=seq(0,1,0.01))
datos<-mutate(datos,x,y=(2/5)*x+(47/25)*exp(-6*x)+(3/25))
ggplot(data=datos,aes(x,y))+geom_line()+geom_point(data=puntosPorEuler,aes(X1,X2),colour="red")
#########Comparativa###############
error<-data.frame(x=puntosPorEuler[,1],euler=puntosPorEuler[,2])
error<-mutate(error,Sol_Exac=(2/5)*x+(47/25)*exp(-6*x)+(3/25),Error=abs(euler-Sol_Exac))
error
#####el comportamiento del que el error disminuya es que el de orden 




