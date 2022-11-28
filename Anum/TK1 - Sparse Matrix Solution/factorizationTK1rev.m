function [L, idxL, U, idxU, pivot] = factorizationTK1rev(A, idxA)
	n = size(A,1); # n adalah ukuran matriks
  L = eye(n); # matriks identitas nxn
  pivot = 1:n;

  for j = 1:n-1
  	# memilih baris pivot, metode partial pivoting
    selectedPivotVal = 0;
    selectedPivotRow = -1;

    for i = j:n
    	if abs(A(i,j)) > abs(selectedPivotVal)
      	selectedPivotVal = A(i,j);
      	selectedPivotRow = i;
      endif
    endfor

    # tukar baris asal dengan pivot
    for k = 1:n
       temp = A(j,k);
       A(j,k) = A(selectedPivotRow, k);
       A(selectedPivotRow, k) = temp;
    endfor

    temp = idxA{j};
    idxA{j} = idxA{selectedPivotRow};
    idxA{selectedPivotRow} = temp;

    for k = 1:j-1
    	temp = L(j,k);
      L(j,k) = L(selectedPivotRow,k);
      L(selectedPivotRow,k) = temp;
    endfor

  	# catat pertukaran baris pada pivot
    temp = pivot(j);
    pivot(j) = pivot(selectedPivotRow);
    pivot(selectedPivotRow) = temp;

    # lakukan optimasi pada faktorisasi
    for i = j+1:n
    	L(i,j) = A(i,j)/A(j,j);
    	pointerSource = 1; # j adalah source
      pointerTarget = 1; # r adalah target, di mana barisnya akan berubah
      newTargetIdx = zeros(1, n);
      newTargetLen = 0; # untuk slicing nantinya

    	while (pointerTarget <= length(idxA{i}) && pointerSource <= length(idxA{j}))
      	indexTarget = idxA{i}(pointerTarget);
        indexSource = idxA{j}(pointerSource);

      	if (indexTarget == indexSource)
        	# A[i][k] dan A[j][k] sama-sama TIDAK 0 dan hasil operasi pengurangan TIDAK 0
        	if (A(i, indexSource) != L(i,j)*A(j, indexSource))
            A(i,indexSource) = A(i,indexSource) - L(i,j) * A(j, indexSource);
            newTargetLen = newTargetLen +1;
            newTargetIdx(newTargetLen) = indexSource;
          else
            A(i, indexTarget) = 0;
          endif

          pointerSource = pointerSource +1;
          pointerTarget = pointerTarget +1;

        elseif (indexTarget < indexSource)
        	# A[i][k] TIDAK 0 tapi A[j][k] = 0, nilai target tidak berubah
          newTargetLen = newTargetLen +1;
          newTargetIdx(newTargetLen) = indexTarget;

          pointerTarget = pointerTarget +1;

        elseif (indexTarget > indexSource)
        	# A[i][k] = 0 tapi perkalian L[i][j] dengan A[j][k] TIDAK 0, nilai target adalah minus perkalian
          if (L(i,j) * A(j, indexSource) != 0)
            A(i,indexSource) = -(L(i,j) * A(j, indexSource));
            newTargetLen = newTargetLen +1;
            newTargetIdx(newTargetLen) = indexSource;
          endif

          pointerSource = pointerSource +1;
        endif
      endwhile

			while (pointerTarget <= length(idxA{i}))
      	# A[i][k] TIDAK 0 tapi A[j][k] = 0, nilai target tidak berubah
        indexTarget = idxA{i}(pointerTarget);
        newTargetLen = newTargetLen +1;
        newTargetIdx(newTargetLen) = indexTarget;

        pointerTarget = pointerTarget +1;
      endwhile

      while (pointerSource <= length(idxA{j}))
        # A[i][k] = 0 tapi perkalian L[i][j] dengan A[j][k] TIDAK 0, nilai target adalah minus perkalian
        indexSource = idxA{j}(pointerSource);
        if (L(i,j) * A(j, indexSource) != 0)
          A(i,indexSource) = -(L(i,j) * A(j, indexSource));
          newTargetLen = newTargetLen +1;
          newTargetIdx(newTargetLen) = indexSource;
         endif

        pointerSource = pointerSource +1;
      endwhile

      idxA{i} = newTargetIdx(1:newTargetLen);

    endfor
  endfor

  idxL = cell(n,1);
  for i = 1:n
  	idxL{i} = zeros(1,n);
    currentLen = 0;
  	for j = 1:n
    	if (L(i,j) != 0)
      	currentLen = currentLen +1;
        idxL{i}(currentLen) = j;
      endif
    endfor
  	idxL{i} = idxL{i}(1:currentLen);
  endfor

  U = A;
  idxU = idxA;
  #uncomment for lookup
  #U
  #idxU
  #L
  #idxL
  #pivot
