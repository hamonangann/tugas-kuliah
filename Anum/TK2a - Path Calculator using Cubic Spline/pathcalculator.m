# semakin besar dots, semakin kompleks, tapi semakin halus interpolasinya
function p = pathcalculator(x,y,dots)
  n=length(x)-1 # ada n+1 titik input
  t=1:n+1
  sample=linspace(1,n+1,max(dots,n+1))

  xt=spline(dots,t,x) # cari koordinat x(t) dengan spline interpolation
  yt=spline(dots,t,y) # cari koordinat y(t) dengan spline interpolation

  plot(x,y,'o',xt, yt)

