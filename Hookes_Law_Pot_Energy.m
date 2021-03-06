%% Plot Potential Energy of Hooke's Law
%  -------------------------------------

% Mass on end of spring experiencing SMH moves +-1m away from equilibrium
x = linspace(-1, 1, 1000);

% Spring Constant (N/m)
k = 0.5;

% Energy function for Hooke's Law
U = (1/2)*k*x.^2;

% Plot Energy as function of distance x from equilibrium
plot(x, U);
title("Hooke's Law Potential Energy");
xlabel("Distance from equilibrium (m)");
ylabel("Pot Energy (J)");