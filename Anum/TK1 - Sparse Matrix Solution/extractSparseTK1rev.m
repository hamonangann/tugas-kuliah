function [A, idxA] = extractSparseTK1rev(A)
  # agar optimal, A haruslah sparse
  n = size(A,1);
  idxA = cell(n,1);
  for i = 1:n
  	idxA{i} = zeros(1,n);
    currentLen = 0;
  	for j = 1:n
    	if (A(i,j) != 0)
      	currentLen = currentLen +1;
        idxA{i}(currentLen) = j;
      endif
    endfor
  	idxA{i} = idxA{i}(1:currentLen);
  endfor
