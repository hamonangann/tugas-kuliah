# x,y adalah sample
# di mana untuk program pathcalculator, kita ingin mencari f(t)=x
# sehingga disini x diganti dengan t, y dengan x
# oleh karena itu, pemanggilannya harusllah spline(xs,t,x)
# kemudian, t itu cukup 0,1,2,3,..,n+1
# satu lagi untuk mencari g(t) =y panggillah spline(xs,t,y)

function ys=spline(xs,x,y)
  n=length(x)-1 # ada n+1 titik disediakan
  k=koefisien(x,y) # cari dulu koefisien k
  ys=zeros(n,1)

  for i=1:n:
    A=((y(i+1)-y(i))/(x(i+1)-x(i))) - ((1/6)*(k(i+1)-k(i))*((x(i+1)-x(i))^2))
    B=y(i) - ((k(i)/6)*((x(i)-x(i+1))^2)) - (A*x(i))
    ys(i) = ((k(i)/6*(x(i)-x(i+1)))*((xs-x(i+1))^3))
    ys(i) = ys(i) + ((k(i+1)/6*(x(i+1)-x(i)))*((xs-x(i))^3))
    ys(i) = + (A*x) + B
  endfor

