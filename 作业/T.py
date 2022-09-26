#-*- coding=utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,3,1000)
y=0.04*np.cos(2*np.pi*x+np.pi*16.8)

plt.figure()
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.plot(x,y,"r--",alpha=0.6)
plt.plot(x*0,y,"b-")
plt.plot(x,y*0,"b-")
plt.show()
