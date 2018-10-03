#Fixed Point method number 1
fixed.point_1<- function(p0, TOL=1E-12 ,N=100) {

  i <- 1; p1 <- p0
  arr1 <- numeric(N)
  while (i<=N) {
    #First iteration step given
    p1 <- exp(-2*p0) 
    
    arr1[i] <- p1
    i <- i + 1
    if (abs(p1-p0) < TOL) break
    p0 <- p1
  }
  #Displaying the iteration steps in an array
  return(arr1[1:(i-1)])
}

fixed.point_2 <- function(q0, TOL=1E-12, N=20){
  i<-1; q1 <- q0
  arr2 <- numeric(N)
  while ( i<=N){
     q1 <- -(1/2)*log(q0)
     arr2[i] <- q1
     i <- i + 1
     if(abs(q1-q0) < TOL) break
     q0 <- q1
  }
    return(arr2[1:i-1])
  
}
#Let's say our initial guess is 0.6

fixed.point_1(0.6)
fixed.point_2(0.6)

