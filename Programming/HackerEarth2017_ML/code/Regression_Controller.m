
y = load('.\\data\\Y.txt');

X = load('.\\data\\X_2_g_d.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

X = load('.\\data\\X_2_g_t.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

X = load('.\\data\\X_2_g_c.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

X = load('.\\data\\X_3_g_d_t.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

X = load('.\\data\\X_3_g_c_t.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

X = load('.\\data\\X_3_g_c_d.txt');
[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));
