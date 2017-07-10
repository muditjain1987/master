function [pA, pB] = regression(X, y, initial_theta, lambda)

% Set Options
options = optimset('GradObj', 'on', 'MaxIter', 400);

% Optimize
[theta, J, exit_flag, output] = ...
 fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);

% Compute accuracy on our training set
[p,pp] = predict(theta, X);

%plotAccuracy(pp,y);

pA = predictionAccuracy(p,y);
pB = mean(double(p == y)) * 100;
precision = pA(1,1)/(pA(1,1)+pA(1,2));
recall = pA(1,1)/(pA(1,1)+pA(2,1));
F1Score = (2*precision*recall)/(precision+recall);
fprintf('Accuracy: %f\n', pB);
fprintf('Precision: %f\n', precision);
fprintf('recall: %f\n', recall);
fprintf('F1Score: %f\n', F1Score);
fprintf('TP: %f\n', pA(1,1));
fprintf('FP: %f\n', pA(1,2));
fprintf('FN: %f\n', pA(2,1));
fprintf('TN: %f\n', pA(2,2));  
end





