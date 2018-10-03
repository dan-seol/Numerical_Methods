
% Q4: Fixed Point Iteration
% Computer root of f(x)=sqrt(x)-e^(-x)

% Two fixed point iterations
g = @(x) exp(-2*x);
h = @(x) (-1/2)*log(x);

% Inputs & Initialisation
p0 = 0.5; % initial approximation
TOL = 0.0000001; % tolerance (i.e. allowed error)
i0 = 1;
iN = 100; % max number of iterations

for i=i0:iN
    
    p = j(p0);
    
    % If within error tolerance, considered successful
    if abs(p-p0) < TOL
        fprintf('Root: %i\n', p);
        fprintf('Iteration: %i\n', i);
        break
    end
    
    % Preparing for next iteration
    p0 = p;
    
end
