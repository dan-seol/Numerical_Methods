# Newton-Raphson Method
g <- function(x){
  sqrt(x) - exp(-x)
}
n.raphson<- function(p0, f, TOL=1E-12,N=20) {
  h <- 0.000000001
  i <- 1; p1 <- p0
  a <- numeric(N)
  while (i<=N) {
    df.dx <- (f(p0+h)-f(p0))/h
    p1 <- (p0 - (f(p0)/df.dx))
    a[i] <- p1
    i <- i + 1
    if (abs(p1-p0) < TOL) break
    p0 <- p1
  }
  return(a[1:(i-1)])
}
n.raphson(0.5, g)

