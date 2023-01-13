from Matice import Tphi, Ty, Tx, rovnice, J
import matplotlib as plot
from math import cos, sin, pi 
import numpy as np 
from scipy.linalg import svd
### Dimensions
l2 = 1
l3 = 0.6
l4=0.3
### Circle trajectory 
h= 50
start =0
step  =((2*pi)/h)
xkk=[]
ykk=[]
for phi in np.arange(start,2*pi,step):
    Rk = 0.2
    xk =0.319+cos(phi)*Rk
    yk =1.16+sin(phi)*Rk 
    xkk.append(xk)
    ykk.append(yk) 

### Starting conditions 
fi20=30*pi/180
fi30=0*pi/180
fi40=-30*pi/180
fi50=0*pi/180
s0 = np.array([[fi20], [fi30], [fi40], [fi50]])
solution = []
i=0
eps = 10**-10
err = 1
s_new = []
Jk = J(s0[0],s0[1],s0[2],s0[3],xkk[i],ykk[i])
f  = rovnice(s0[0],s0[1],s0[2],s0[3],xkk[i],ykk[i])
f=f[:, np.newaxis] 
u, s, vt = svd(Jk)
u= -np.transpose(u) #
pp= np.dot(u,f)
s=s[:, np.newaxis] 
p = np.array([pp[0]/s[0],pp[1]/s[1],pp[2]/s[2],pp[3]/s[3]])
vt= -np.transpose(vt) #
s_new = np.dot(vt,p) + s0
err = np.linalg.norm(np.dot(vt,p))




