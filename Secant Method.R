#Secant Method
g <- function(x){
  sqrt(x) - exp(-x)
}
secant.mtd <- function(f, p0, p1, TOL=1E-12,N=20){
  i <- 1
  q0 <- f(p0)
  q1 <- f(p1)
 b <- numeric(N)
  while(i <= N){
    p <- p1 - q1*(p1-p0)/(q1-q0)
    b[i] <- p
    i <- i+1
    if(abs(p-p1) < TOL) break
    p0 <- p1
    q0 <- q1
    p1 <- p
    q1 <- f(p)
  }
 return(b[1:i-1])
}
secant.mtd(g, 0.4, 0.6)

