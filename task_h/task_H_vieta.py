# ax^3+bx^2+cx+d = 0 /a
# x^3+a1x^2+b1x+c1 = 0
# in(640 794 42 7) out(-1.1933 -0.0237+i0.0928 -0.0237-i0.0928 ) S<0
# in(943 414 -8 -4) out(-0.4362 0.0972 -0.1000) S>0
import math
import numpy as np
a = 640
b = 794
c = 42
d = 7
#
a1=b/a
b1=c/a
c1=d/a
a=a1
b=b1
c=c1
#

Q = (a**2-3*b)/9
R = (2*a**3-9*a*b+27*c)/54
S = Q**3-R**2

if (S>0):
    fi = 1/3*math.acos(R/Q**(3/2))
    print (R/Q**(2/3))
    print (math.acos(R/Q**(2/3)))
    x1 = -2*Q**(0.5)*math.cos(fi)-a/3
    x2 = -2*Q**(0.5)*math.cos(fi+2/3*math.pi)-a/3
    x3 = -2*Q**(0.5)*math.cos(fi-2/3*math.pi)-a/3
    print(x1,x2,x3)
elif(S<0):
    if(Q>0):
        fi = 1/3*math.acosh(abs(R)/Q**(3/2))
        x1 = -2*np.sign(R)*Q**0.5*math.cosh(fi)-a/3
        x2 = complex((np.sign(R)*Q**0.5*math.cosh(fi)-a/3),(3**(0.5)*Q**(0.5)*math.sinh(fi)))
        x3 = complex((np.sign(R)*Q**0.5*math.cosh(fi)-a/3),(-3**(0.5)*Q**(0.5)*math.sinh(fi)))
        print(x1,x2,x3)