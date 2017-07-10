y = load('.\\data\\Y.txt');
sparsedata = load (".\\data\\X_5_g_c_d_t_t_sparse.txt");
X = spconvert(sparsedata);
clear sparsedata;
X = nthroot(X,3);
X = full(X);

X(:,~any(X,1)) = [];

[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));
clear all;