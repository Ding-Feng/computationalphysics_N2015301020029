# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:01:40 2017

@author: MSI
"""
import math
import matplotlib.pyplot as plt
#calculate the trajectory
def Trajectory(v,theta,B,T0,choice):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt,y0,a,alpha=0.01,10**4,6.5*10**(-3),2.5
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    if choice<0:            #negative for isothermal approximation
        def rho(height):
            return math.exp(-height/y0) #(2.23)
    else:                   #non-negative for adiabatic approximation
        def rho(height):
            return (1-a*height/T0)**alpha #(2.24)
    while y>= 0:
        a_x3, a_y3=-B*rho(y)*v*v_x,-9.8-B*rho(y)*v*v_y
        x=x+v_x*dt
        v_x=v_x+a_x3*dt
        y=y+v_y*dt
        v_y=v_y+a_y3*dt
        t=t+dt
        v=math.sqrt(v_x**2+v_y**2)
        distance[0].append(x/1000) 
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance
#plot the isothermal case
velocity=700 #kilometer
B=4*10**(-5)
T0=300
plt.subplot(1,2,1)
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle,B,T0,-1)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label=angle)
    #print angle,d[0][-1],d[2][0]    
plt.grid(True,color='k')
plt.title('Cannon Trajectory')
plt.text(30,6,'Isothermal',fontsize=15)
plt.text(30,5,'v0=700m/s')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.xlim(0,40)
plt.ylim(0,14)
plt.legend()
#plot the adiabatic case
plt.subplot(1,2,2)
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle,B,T0,1)
    plt.plot(d[0],d[1],linestyle='--',linewidth=1.0,label=angle)
    #print angle,d[0][-1],d[2][0]   
plt.grid(True,color='k')
plt.title('Cannon Trajectory')
plt.text(30,6,'Adiabatic',fontsize=15)
plt.text(30,5,'v0=700m/s')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.xlim(0,40)
plt.ylim(0,14)
plt.legend()
plt.show()