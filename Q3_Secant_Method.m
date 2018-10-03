
% Q3: Secant Method
% Compute root of f(x)=sqrt(x)-e^(-x)

% Function
f = @(x) sqrt(x)-exp(-x);

% Inputs & Initialisation
p0 = 0; % 1st point of initial approximation
p1 = 1; % 2nd point of initial approximation
q0 = f(p0);
q1 = f(p1);
TOL = 0.0000001; % tolerance (i.e. allowed error)
i0 = 1;
iN = 100; % max number of iterations

for i=i0:iN
    
    % Compute p_i
    p = p1 - q1*((p1-p0)/(q1-q0));

    % If within error tolerance, considered successful
    if abs(p-p1) < TOL
        fprintf('Root: %i\n', p);
        fprintf('Iteration: %i\n', i);
        break
    end

    % Preparing for next iteration
    p0 = p1;
    q0 = q1;
    p1 = p;
    q1 = f(p);
    
end
