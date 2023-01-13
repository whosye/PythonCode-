from math import cos, sin, pi 
import numpy as np 
import matplotlib.pyplot as plt
from itertools import count 
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

width, height = 500, 500

# parametry
r1=1
r2=0.5
#interval reseni
beta1_start=90*pi/180
beta1_end = 20*pi/180
beta2_start=20*pi/180
beta2_end = 60*pi/180
xm0=cos(beta1_start)*r1+cos(beta2_start)*r2
ym0=sin(beta1_start)*r1+sin(beta2_start)*r2
# kroky
h1 = 100
h2 = 100
step1 = (beta1_end-beta1_start)/(h1)
step2 = (beta2_end-beta2_start)/(h2)
#vektor závislých 
z=np.zeros([2,1000])
z[0,0]=xm0
z[1,0]=ym0
X_cor = []
Y_cor = []
X_cor.append(xm0)
Y_cor.append(ym0)
q1 = []
q2 = []
for i in np.arange(beta1_start,beta1_end,step1):
    q1.append(i)
for i in np.arange(beta2_start,beta2_end,step2):
    q2.append(i)
for i in range(len(q1)):
    iterace = 1 
    res=1
    while res > 0.01:
        Fx = cos(q1[i])*r1 + cos(q2[i])*r2 +cos(3/4*pi)*z[0,i]-z[1,i]
        Fy = sin(q1[i])*r1 + sin(q2[i])*r2+sin(3/4*pi)*z[0,i]
        F = np.array([[Fx],[Fy]]); 

        J = np.array([[cos(3/4*pi), -1],[sin(3/4*pi) ,0]])
        J_in =np.linalg.inv(J)

        z = z - np.dot((J_in),F)
        
        res = np.linalg.norm(F);   
        iterace +=1
   
        if iterace > 20:
            print('Překročen počet iterací')
            break
    z[0,i+1] = z[0,i]
    z[1,i+1] = z[1,i]
    X_cor.append(z[0,i])
    Y_cor.append(z[1,i])

    
    #print('Z vysledek' +str(z[0,i+1])) 
    #print('Z vysledek' +str(z[1,i+1]))   
X1 = []
Y1 = []
X2 = []
Y2 = []
for j  in range(len(q1)):
    Xold1 = cos(q1[j])*r1
    Yold1 = sin(q1[j])*r1
    Xold2 = cos(q1[j])*r1+cos(q2[j])*r2
    Yold2 = sin(q1[j])*r1+sin(q2[j])*r2
    X1.append(Xold1)
    Y1.append(Yold1)
    X2.append(Xold2)
    Y2.append(Yold2)



"""
WIP
index = count()
x_vals1 = []
y_vals1 = []

x_vals2 = []
y_vals2 = []
def animate(i):
    idx = next(index)
    x_vals1.append(X1[idx])
    y_vals1.append(Y1[idx])
    x_vals2.append(X1[idx]+X2[idx])
    y_vals2.append(Y1[idx]+Y2[idx])
    plt.cla()
    plt.plot(x_vals1,y_vals1)
    plt.plot(x_vals2,y_vals2)
    x_vals1.clear
    y_vals1.clear

ani = FuncAnimation(plt.gcf(), animate, interval = 250)
plt.tight_layout()
plt.show()

"""