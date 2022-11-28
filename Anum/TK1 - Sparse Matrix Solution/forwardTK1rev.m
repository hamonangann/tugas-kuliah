function x = forwardTK1rev(L, idxL, b)
  n = size(L, 1); # n adalah ukuran matriks
  x = zeros(1, n);
  for i = 1:n
    sum = 0;
    pointerTarget = 1;
    if length(idxL{i}) > 0
      indexTarget = idxL{i}(1);
      while indexTarget < i
        indexTarget = idxL{i}(pointerTarget);
        sum = sum + L(i,indexTarget)*x(indexTarget);
        pointerTarget = pointerTarget +1;
      endwhile
    endif
    x(i) = (b(i)-sum)/L(i,i);
  endfor

