function pA = predictionAccuracy(p,y)
  
  pA = [0,0;0,0];
  m = size(y,1);


  for i = 1:m
    
    if p(i,1) == 1
      
      if y(i,1) == 1
        pA(1,1) = pA(1,1) + 1; %true positive
      else
        pA(1,2) = pA(1,2) + 1; %false positive
      endif  
    
    elseif p(i,1) == 0
      
      if y(i,1) == 1
        pA(2,1) = pA(2,1) + 1; %false negative
      else
        pA(2,2) = pA(2,2) + 1; %true negative
      endif
    
    endif  
  endfor
  
end