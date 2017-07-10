function plotAccuracy(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.
%
% Note: This was slightly modified such that it expects y = 1 or y = 0

% Find Indices of Positive and Negative Examples
pos = find(y == 1); neg = find(y == 0);

% Plot Examples
plot(1, X(pos, 1), 'k*','MarkerFaceColor', 'b','LineWidth', 1, 'MarkerSize', 7)
hold on;
plot(0, X(neg, 1), 'ko', 'MarkerFaceColor', 'y', 'MarkerSize', 7)
hold off;

end