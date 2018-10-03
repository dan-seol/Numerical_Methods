fixed.point_lambda<- function(x0, TOL=1E-12 ,N=100) {
  
  i <- 1; x1 <- x0
  arr1 <- numeric(N)
  while (i<=N) {
    #First iteration step given
    x1 <- (cos(x0)*x0+1-sin(x0))/(1+cos(x0)) 
    
    arr1[i] <- x1
    i <- i + 1
    if (abs(x1-x0) < TOL) break
    x0 <- x1
  }
  #Displaying the iteration steps in an array
  return(arr1[1:(i-1)])
}
fixed.point_lambda(0.8)
