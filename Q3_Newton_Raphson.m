
% Q3: Newton_Raphson Method
% Compute root of f(x)=sqrt(x)-e^(-x)

% Function and its derivative
f = @(x) sqrt(x)-exp(-x);
df = @(x) exp(-x) + 1/(2*sqrt(x)); 

% Inputs & Initialisation
p0 = 1; % initial approximation
TOL = 0.0000001; % tolerance (i.e. allowed error)
i0 = 1;
iN = 100; % max number of iterations

for i=i0:iN
    
    p = p0 - f(p0)/df(p0);
   
    % If within error tolerance, considered successful
    if abs(p-p0) < TOL
        fprintf('Root: %i\n', p);
        fprintf('Iteration: %i\n', i);
        break
    end
    
    % Preparing for next iteration
    p0 = p;
    
end
