library(Matrix)
library(linSolve)
library(BB)

installed.packages("RlinSolve")
installed.packages("BB")


x <- c(4,2,2)
y <- c(2,5,4)
z <- c(5,1,3)
#resultado <-(18,27.3,16.2)

ma <- matrix(c(x,y,z),
             nrow = 4,
             nrow = 3)

prot(ma)
ma
A = c(18,27.3,16.2)
A
det(ma.matrix= TRUE)

solve(ma)
#A matriz de coeficiente diagonal dominante
#Diagonal(matri, a)
diagonal <- function(M){
  M[col(M) != row(S)] <- 0
  return(M)
}
diagonal(M)

#B matriz de transicion por el metodo de Jacobi y metodo converge
C = diagonal(ma)
L = tril(A,k = -1, diag =FALSE)
U = triu(A,k= 1, diag = FALSE)
C+L+U
T1 = (-solve(C))%°%(L+U)
T1
print(norm(T1,"I"))

w <- T1
proces(w)
# Teorema de convergencia
solucion <- itersolve(ma, A,nmax = 3000,
                      tol = 0.000001,
                      method = "Jacobi")

solucion

solucion_1 <- itersolve(ma,A,nmax = 5000,
                        tol = 0.000001,
                        method = "Gauss- Seidel")

solucion_1

