import math
c1=int(input())
g1=int(input())
c2=int(input())
g2=int(input())
c3=int(input())
g3=int(input())
c4=int(input())
g4=int(input())
c5=int(input())
g5=int(input())
sgpa=(c1*g1+c2*g2+c3*g3+c4*g4+c5*g5)/(c1+c2+c3+c4+c5)
print(math.trunc(100*sgpa)/100)

