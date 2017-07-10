y = load('.\\data\\Y.txt');
%X = load("-ascii",'.\\data\\X_4_g_c_t_d.txt');
%X = dlmread(".\\data\\X_4_g_c_t_d.txt")
#X = textscan(".\\data\\X_4_g_c_t_d.txt");
#X = importdata(".\\data\\X_4_g_c_t_d.txt");

%f = fopen(".\\data\\X_4_g_c_t_d.txt","r");
f = fopen(".\\data\\X_1_t.txt","r");
C = textscan(f,"%f",'delimiter', ',');
fclose(f);

Xp = cell2mat(C);

m = size(y,1);
n = size(Xp,1)/m;
X = (reshape(Xp,n,m))';
clear Xp;

%ss = sum(X.^2);
%min1 = min(X);
%max1 = max(X);
%X_1 = zeros(m,1);
%ii = 1;
%for index = 1:n
%  if ss(1,index) != 0
%    X_1(:,ii) = X(:,index);
%    ii = ii+1;
%  elseif min1(1,index) != max1(1,index)
%    X_1(:,ii) = X(:,index);
%    ii = ii+1;
%  endif
%endfor  

%clear ss;
%clear min1;
%clear max1;
%clear X;

X(:,~any(X,1)) = [];


%[R,basiccol] = rref(X);
%X_new = X(:,basiccol);

[pA, pB] = regression(X,y);
fprintf('Train Accuracy: %f\n', pB);
fprintf('True Positive: %f\n', pA(1,1));
fprintf('False Positive: %f\n', pA(1,2));
fprintf('False Negative: %f\n', pA(2,1));
fprintf('True Negative: %f\n', pA(2,2));

clear all;
