%% Two Dimensional Oscillators Plots
%  ---------------------------------

% The simplest 2D/3D oscillator is the isotropic harmonic oscillator, for
% which the restoring force is proportional to the displacement from
% equilibrium, with the same constant of proportionality k in all
% directions: F = -kr.
%
% Important 3D examples of such oscillators are an atom vibrating near its
% equilibirum in a symmetrical crystal, and a proton (or neutron) as it
% moves inside a nucleus.
% ------------------------------------------------------------------------
% Declare initial conditions

A = 1; % Amplitude
t = linspace(0,10,1000); % Time (s)
w1 = 10; % Angular Freq (rad/s)
w2 = 5;
w3 = sqrt(2);
w4 = 1;
S = [0, pi/2, pi/4]; % Make a list then loop through for each plot
numS = length(S); % Allows for any number of values of S

% ------------------------------------------------------------------------
% Plot 2D isotropic oscillator with different relative phases
% Hold must be on otherwise each plot overrides the last

figure(1)
for i=1:numS
x = A*cos(w2*t);
y = A*cos((w2*t) - S(i));
plot(x,y,'-'); hold on 
end
xlim([-1.15 1.15]) % Increase plot dimensions
ylim([-1.15 1.15])
xline(0); % X axis
yline(0); % Y axis
title("2D Isotropic Oscillator's Motion (With Same Ang. Freq)")
xlabel("Displacement from equilibrium in x direction (m)")
ylabel("Displacement from equilibrium in y direction (m)")

% If w1/w2 is rational then the motion is periodic
figure(2)
for i=1:numS
x = A*cos(w1*t);
y = A*cos((w2*t) - S(i));
plot(x,y,'-'); hold on 
end
xlim([-1.15 1.15])
ylim([-1.15 1.15])
xline(0);
yline(0);
title("Period Motion")
xlabel("Displacement from equilibrium in x direction (m)")
ylabel("Displacement from equilibrium in y direction (m)")

% If w1/w2 is irrational then the motion never repeats itself
% This type of motion is called quasiperiodic
%The motion of x and y is periodic, but because the two periods are
%... incompatible, r = (x,) is not
figure(3)
for i=1:numS
x = A*cos(w3*t);
y = A*cos((w4*t) - S(i));
plot(x,y, '-'); hold on 
end
xlim([-1.15 1.15])
ylim([-1.15 1.15])
xline(0);
yline(0);
title("Quasiperiod Motion")
xlabel("Displacement from equilibrium in x direction (m)")
ylabel("Displacement from equilibrium in y direction (m)")
