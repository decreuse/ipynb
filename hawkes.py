from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tikzplotlib




def h(t):
    return np.exp(-t)

def intensite(sauts,nu,g, t):
    c=nu
    for s in sauts:
        if (s<=t):
            c+=g(t-s)
    return c

sauts=[]
horizon=20.

t=0.
while(t<=horizon):
    M=intensite(sauts,1.,h,t)
    t+=-np.log(np.random.rand())/M
#    print(M,t)
    while(M*np.random.rand()>intensite(sauts,1.,h,t)):
        t+=-np.log(np.random.rand())/M
#        print("fail")
    sauts+=[t]

x=np.linspace(0,20,101)
y=[]
for u in x:
    y+=[intensite(sauts,1.,h,u)]

plt.clf()
plt.plot(x,y)
plt.plot(sauts,np.zeros(len(sauts)),'bo',ms=2,lw=0.5)
plt.show()
#tikzplotlib.save("myhawkes.tex")


## Hawkes 2-dimensionel

sauts1=[]
sauts2=[]

horizon=20.
temps=0
while(temps<=horizon):
    M1=intensite(sauts2,1.,h,temps)
    M2=+intensite(sauts1,1.,h,temps)
    t1=-np.log(np.random.rand())/M1
    t2=-np.log(np.random.rand())/M2
    while(M1*np.random.rand()>intensite(sauts2,1.,h,temps+t1)):
        t1+=-np.log(np.random.rand())/M1
    while(M2*np.random.rand()>intensite(sauts1,1.,h,temps+t2)):
        t2+=-np.log(np.random.rand())/M2
    if (t1<=t2):
        sauts1+=[temps+t1]
        temps+=t1
    else:
        sauts2+=[temps+t2]
        temps+=t2

sauts2=np.asarray(sauts2)
sauts1=np.asarray(sauts1)
x=np.linspace(0,horizon,1001)
y=[]
for l in x:
    y+=[np.sum(sauts1<=l)-np.sum(sauts2<=l)]
plt.clf()
plt.plot(x,y)
#plt.show()
tikzplotlib.save("my_carnet_dordre.tex")
