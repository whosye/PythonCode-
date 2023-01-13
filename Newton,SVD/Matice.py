import numpy as np 
from math import cos, sin, pi
### Dimensions
l2 = 1
l3 = 0.6
l4=0.3

def Ty(y):
    return np.array([[1, 0, 0],[0,1,y],[0,0,1]])
def Tx(x):
    return np.array([[1, 0, x],[0,1,0],[0,0,1]])
def Tphi(phi):
    return np.array([[cos(phi),-sin(phi),0],[sin(phi),cos(phi),0],[0,0,1]])
def J(fi2,fi3,fi4,fi5,x_q,y_q):
    A1 =sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    A2 =sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    A3 =sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    A4 =sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    B1=cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    B2=cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    B3=cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    B4=cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    C1=x_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))) - l4*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - l2*cos(fi2) - l3*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - y_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))))
    C2= x_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))) - l4*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - l3*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - y_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))))
    C3=x_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))) - l4*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - y_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))))
    C4=x_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))) - y_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))))
    D1=- cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    D2=- cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    D3=- cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    D4=- cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    E1=sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    E2=sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    E3=sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    E4= sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    F1=x_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))) - l4*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - l2*sin(fi2) - l3*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + y_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))))
    F2=x_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))) - l4*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - l3*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + y_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))))
    F3= x_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))) - l4*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + y_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))))
    F4=x_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))) + y_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))))
    A =(A1,A2,A3,A4)
    B =(B1,B2,B3,B4)
    C =(C1,C2,C3,C4)
    D =(D1,D2,D3,D4)
    E =(E1,E2,E3,E4)
    F =(F1,F2,F3,F4)
    return np.array([A,B,C,D,E,F])

def rovnice(fi2,fi3,fi4,fi5,x_q,y_q):
    R1= - cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - 1
    R2= sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))
    R3= x_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)))) - l4*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - l2*sin(fi2) - l3*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + y_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))))
    R4= cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))
    R5= - cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) - sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - 1
    R6= l3*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) + l4*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) + l2*cos(fi2) - x_q*(cos(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))) - sin(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)))) + y_q*(cos(fi5)*(cos(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3)) + sin(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2))) + sin(fi5)*(cos(fi4)*(cos(fi2)*sin(fi3) + cos(fi3)*sin(fi2)) - sin(fi4)*(sin(fi2)*sin(fi3) - cos(fi2)*cos(fi3))))
    return np.array([R1,R2,R3,R4,R5,R6])
   




