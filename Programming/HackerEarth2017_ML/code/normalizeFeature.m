function X_norm = normalizeFeature(X)
 
mu = sum(X);
for i = 1:length(mu)
  mu(i,1) = mu(i,1)/
  
  
end  

X_norm = bsxfun(@minus, X, mu);


range = (max(X) .- min(X));
X_norm = bsxfun(@rdivide, X_norm, range);

end

%-----------------------extra code-----------------
%mu = mean(X);
%X_norm = bsxfun(@minus, X, mu);

%sigma = std(X_norm);
%X_norm = bsxfun(@rdivide, X_norm, sigma);

%Xones = ones(size(X(:,1)));
%X = [Xones X];

%mu = mean(X);
%mu(1) = 0;
%X_norm = bsxfun(@minus, X, mu);
%sigma = std(X);
%sigma(1) = 1;
%X_norm = bsxfun(@rdivide, X_norm, sigma);

%X_norm = (X .- min(X))./(max(X) .- min(X));

%X_norm = bsxfun(@minus, X, min(X));