function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

h_theta_x = sigmoid(X*theta);                   % m*1 matrix
l1 = log(h_theta_x);                            % m*1 matrix
l2 = log(1-h_theta_x);                          % m*1 matrix
Reg = (lambda/(2*m))*(sum(theta.^2) - theta(1,1)^2);

J = (-1/m)* ((y' * l1)+((1-y')*l2)) + Reg;

%f = fopen(".\\J.txt","a");
%fprintf(f,"%d\n",J);
%fclose(f);
 
grad = ((1/m)*((X') * (h_theta_x - y))) + ((lambda/m)*theta);
grad(1,1) = grad(1,1) - ((lambda/m)*theta(1,1));








% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta






% =============================================================

end
