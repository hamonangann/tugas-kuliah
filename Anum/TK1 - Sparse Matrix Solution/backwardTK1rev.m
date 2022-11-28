function x = backwardTK1rev(U, idxU, b)
  n = size(U, 1); # n adalah ukuran matriks
  x = zeros(1, n);
  for i = n:-1:1
    sum = 0;
    pointerTarget = length(idxU{i}); # hanya menunjuk indeks berisi elemen tak 0 pada tiap baris
    if length(idxU{i}) > 0
      indexTarget = idxU{i}(pointerTarget);
      while indexTarget > i
        indexTarget = idxU{i}(pointerTarget);
        sum = sum + U(i,indexTarget)*x(indexTarget);
        pointerTarget = pointerTarget -1;
      endwhile
    endif
    x(i) = (b(i)-sum)/U(i,i);
  endfor

