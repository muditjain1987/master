
y = load('.\\data\\Y.txt');


X0 = prepareX(".\\data\\X_5_g_c_d_t_t.txt0");
X1 = prepareX(".\\data\\X_5_g_c_d_t_t.txt1");
X2 = prepareX(".\\data\\X_5_g_c_d_t_t.txt2");
X3 = prepareX(".\\data\\X_5_g_c_d_t_t.txt3");
X4 = prepareX(".\\data\\X_5_g_c_d_t_t.txt4");
X5 = prepareX(".\\data\\X_5_g_c_d_t_t.txt5");
X6 = prepareX(".\\data\\X_5_g_c_d_t_t.txt6");
X7 = prepareX(".\\data\\X_5_g_c_d_t_t.txt7");
X8 = prepareX(".\\data\\X_5_g_c_d_t_t.txt8");
X9 = prepareX(".\\data\\X_5_g_c_d_t_t.txt9");


X = [X0' X1' X2' X3' X4' X5' X6' X7' X8' X9']';

clear X0 X1 X2 X3 X4 X5 X6 X7 X8 X9;


X(:,~any(X,1)) = [];

[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

clear all;