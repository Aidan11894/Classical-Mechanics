%% Damped Oscillators Plots
%  ---------------------------------
%
% Suppose the parameter B(the damping constant) < w (the natural frequency)
% This condition is known as underdamping.
% This describes SHM of frequency w1 with an exponentially decreasing
% amplitude A*exp(-Bt), where the larger the B, the more rapidly the
% oscillations die out.

% ------------------------------------------------------------------------
% Declare Initial Conditions
t = linspace(1,100,10000);
A = 1;
B = 0.08;
w1 = 4;
S = 1;
x = (A.*exp(-B*t)).*cos(w1*t - S);

% Plot underdamped oscillations
figure(1)
plot(t,x);
xlim([-11.15 111.15]) % Increase plot dimensions
ylim([-1.15 1.15])
xline(0); % X axis
yline(0); % Y axis
title("Underdamped Oscillator's Motion")
xlabel("Time (s)")
ylabel("Displacement from equilibrium in y direction (m)")