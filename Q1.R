Lag_Poly<- function(yi, x=0.0015, xi, xj1, xj2, xj3, xj4){
  yi*((x - xj1)*(x - xj2)*(x - xj3)*(x - xj4))/((xi - xj1)*(xi - xj2)*(xi - xj3)*(xi - xj4))
}
xList <- c(0.001, 0.002, 0.003, 0.004, 0.005)
sinList <- c(0.001000, 0.002000, 0.003000, 0.004000, 0.005000)
cosList <- c(1.000000, 0.999998, 0.999996, 0.999992, 0.999988)
cotList <- c(1000.0, 499.999, 333.332, 249.999, 199.998)

Lag_Polycot <- c();
n <- length(xList)
for(i in 1:5){

  zList <- xList[-i];
  Lag_Polycot <- append(Lag_Polycot,Lag_Poly(cotList[i],0.0015,xList[i], 
                                             zList[1], zList[2], zList[3], zList[4]))
}
paste(c("Our lagrange polynomials for cot(0.0015) is "),t(Lag_Polycot), 
      c("giving the approximation of cot(0.0015)"),sum(Lag_Polycot))


Lag_Polysin <- c();
for(i in 1:5){
  
  zList <- xList[-i];
  Lag_Polysin <- append(Lag_Polysin,Lag_Poly(sinList[i],0.0015,xList[i], 
                                             zList[1], zList[2], zList[3], zList[4]))
}
paste(c("Our lagrange polynomials for sin(0.0015) is "),t(Lag_Polysin), 
      c("giving the approximation of sin(0.0015)"),sum(Lag_Polysin))



Lag_Polycos <- c();

Lag_Polysin <- c();
for(i in 1:5){
  
  zList <- xList[-i];
  Lag_Polycos <- append(Lag_Polycos,Lag_Poly(cosList[i],0.0015,xList[i],
                                             zList[1], zList[2], zList[3], zList[4]))
}
paste(c("Our lagrange polynomials for cos(0.0015) is "),t(Lag_Polycos),
      c("giving the approximation of cos(0.0015)"),sum(Lag_Polycos))

paste(c("Our approximation for cot(0.0015) is "), 0.999999871875/0.0015)
paste(c("Our built-in function gives cot(0.0015) is approximately"), cos(0.0015)/sin(0.0015))

