%% Function Handles and Integrals

% We define a function handle using @(variable)(function of variable)
% After, we use the function 'integral' which takes in a function handle
% then the lower and upper bounds

f = @(x)(sin(x).^3);
I = rat(integral(f, 0, pi));

% We use the dot before the index as sin(x) creates a matrix of sin values
% and we don't want to multiply 3 matrices, we want to cube each element.
% rat function turns decimals into rationals