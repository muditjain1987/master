y = load('..\\data\\Y.txt');
m = length(y);
X = prepareX("..\\data\\X_5_g_c_d_t_t_sparse.txt");

initial_theta = ones(size(X, 2), 1);
initial_theta = initial_theta .* -2;
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = ones(size(X, 2), 1);
initial_theta = initial_theta .* -1;
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = ones(size(X, 2), 1);
initial_theta = initial_theta .* -0.1;
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = zeros(size(X, 2), 1);
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = ones(size(X, 2), 1);
initial_theta = initial_theta .* 0.1;
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = ones(size(X, 2), 1);
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

initial_theta = ones(size(X, 2), 1);
initial_theta = initial_theta .* 2;
lambda = 0;
[pA, pB] = regression(X,y,initial_theta,lambda);

a=1; %just to hold on the data
clear all;