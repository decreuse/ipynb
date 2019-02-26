#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:29:45 2018

@author: laurent
"""

from numpy import *
import numpy as np
import matplotlib.pyplot as plt


def initialisation(r):
    t=np.zeros((r,2))
    for i in np.arange(r):
        t[i,0]=1
        t[i,1]=i+1
    return t

def transition(t,r):
    s=np.zeros((1,2))
#    if np.random.rand()<= (t[0,1]-(t[r-1,0]-t[0,0]))/t[0,1]:
    if np.random.rand()<= t[r-1,1]/(t[r-1,1]+t[r-1,0]-t[0,0]):   
        s[0,0]=t[r-1,0]+1
        s[0,1]=t[r-1,1]
    else:
        s[0,0]=t[r-1,0]
        s[0,1]=t[r-1,1]+1
    #print(s)
    return np.concatenate((t[1:r,:], s))


def f(r,N):
    t=initialisation(r)
    for i in np.arange(N):
        t=transition(t,r)
    return t[r-1,:]


    #print(t)
#print("last vector",t[r-1,:])
#print("nb of validations during last r steps ",t[r-1,0]-t[0,0] )
#print("percentage of free nodes ", t[r-1,1]/np.sum(t[r-1,:])*np.log10(N))
#print(t[r-1,:],,t[r-1,0]*r*1./N)

x=[]    
dim=9
for i in np.arange(dim):
   z=f(3,10**i) 
   x+=[z[1]]
plt.plot(np.arange(dim),x)
plt.show()
      