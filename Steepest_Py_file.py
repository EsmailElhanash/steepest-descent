from sympy import *

p0 = [0, 0]
x, y, lam = symbols("x y lam")
f = x - y + 2 * x ** 2 + 2 * x * y + y ** 2
delF = [diff(f, x).subs({x: p0[0],y:p0[1]}), diff(f, y).subs({x: p0[0],y:p0[1]})]
print("delF0=" + str(delF))
p1 = [p0[0] - lam * delF[0] , p0[1] - lam * delF[1]]
lam1 = solve(diff(f.subs({x:p1[0],y:p1[1]}),lam))
p1 = [p0[0] - lam1[0] * delF[0] , p0[1] - lam1[0] * delF[1]]
print("p1=" + str(p1))



x, y, lam = symbols("x y lam")
f = x - y + 2 * x ** 2 + 2 * x * y + y ** 2
delF2 = [diff(f, x).subs({x: p1[0],y:p1[1]}), diff(f, y).subs({x: p1[0],y:p1[1]})]
p2 = [p1[0] - lam * delF2[0] , p1[1] - lam * delF2[1]]
lam2 = solve(diff(f.subs({x:p2[0],y:p2[1]}),lam))
print("lam2=" + str(lam2))
p2 = [p1[0] - lam2[0] * delF2[0] , p1[1] - lam2[0] * delF2[1]]
print("p2=" + str(p2))

x, y, lam = symbols("x y lam")
f = x - y + 2 * x ** 2 + 2 * x * y + y ** 2
delF3 = [diff(f, x).subs({x: p2[0],y:p2[1]}), diff(f, y).subs({x: p2[0],y:p2[1]})]
p3 = [p2[0] - lam * delF3[0] , p2[1] - lam * delF3[1]]
lam3 = solve(diff(f.subs({x:p3[0],y:p3[1]}),lam))
print("lam3=" + str(lam3))
p3 = [p2[0] - lam3[0] * delF3[0] , p2[1] - lam3[0] * delF3[1]]
print("p3=" + str(p3))



