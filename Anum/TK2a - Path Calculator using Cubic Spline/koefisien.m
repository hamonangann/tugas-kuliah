function k = koefisien(x,y)
  n=length(x)-1 # ada n+1 titik x
  k=zeros(n+1,1)

  # natural splines, k di ujung sama dengan 0
  k(1)=0 # octave gabisa mulai dr index 0 :"
  k(n+1)=0

  A=zeros(n-1) # buat matriks untuk menghitung k2 hingga kn
  b=zeros(n-1) # ruas kanan

  for i=1:n-1:
    b(i)=6*(((y(i)-y(i+1))/((x(i)-x(i+1))^2))-((y(i+1)-y(i+2))/((x(i+1)-x(i+2))^2)))
  endfor

  A(1,1) = 2*(x(1)-x(3))
  A(1,2) = x(2)-x(3)
  for i=2:n-2:
    A(i,i-1)=x(i)-x(i+1)
    A(i,i)=2*(x(i)-x(i+2))
    A(i,i+1)=x(i+1)-x(i+2)
  endfor
  A(n-1,n-2)=x(n-1)-x(n)
  A(n-1,n-1)=2*(x(n-1)-x(n+1))

  k(2:n)=A\b # selesaikan persamaan (bisa diimprovisasi)
