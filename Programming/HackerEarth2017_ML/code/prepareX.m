function [Z] = prepareX(filename)

% 1) Read Sparse Data.
sparsedata = load (filename);
X = spconvert(sparsedata);
clear sparsedata;


% 2) preprocess before normalize
X = nthroot(X,3);

X1 = X(:,1:5000);
X2 = X(:,5001:10000);
X3 = X(:,10001:end);
clear X;

X1(:,~any(X1,1)) = [];
X1 = normalizeFeature(X1);
[U1, S1] = pca(X1);
K = 2250;
Z1 = projectData(X1, U1, K);
clear X1 U1 S1;

X2(:,~any(X2,1)) = [];
X2 = normalizeFeature(X2);
[U2, S2] = pca(X2);
K = 3000;
Z2 = projectData(X2, U2, K);
clear X2 U2 S2;

X3(:,~any(X3,1)) = [];
X3 = normalizeFeature(X3);
[U3, S3] = pca(X3);
K = 2800;
Z3 = projectData(X3, U3, K);
clear X3 U3 S3;

Z = [Z1 Z2 Z3];
clear Z1 Z2 Z3;


Xones = ones(size(Z(:,1)));
Z = [Xones Z];
 
 
end