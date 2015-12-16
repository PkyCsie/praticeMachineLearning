# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:44:15 2015

@author: pky
"""

import matplotlib.pyplot as plt
import numpy as np

howManyNode = 10
right = 8
firstTimeChoice = 1

iteration = 100

plt.xlim(-10,10)
plt.ylim(-10,10)

x = np.random.randint(-5,5,size = (howManyNode)) 
y = np.random.randint(-5,5,size = (howManyNode))





plt.plot(x,y,"o")
plt.plot(x[right],y[right],"yo")



w = np.array([0,0])



w = w + np.sum(w*np.array([x[firstTimeChoice],y[firstTimeChoice]]))\
      - np.sum(w*np.array([x[right],y[right]])) 

get = False
for i in range(iteration):
        value = w[0] * x + w[1] * y
        maxIndex = np.argmax(value)
        if maxIndex == right:
            get = 1
            print "get correct weight in iteration: ",i
            break
        w = w - np.array([x[maxIndex],y[maxIndex]]) + np.array([x[right],y[right]])
if  get==False:
    print "not get the correct weight"
 
w_x =np.array([0,w[0]])
w_y =np.array([0,w[1]])   
plt.plot(w_x,w_y,"r")         
for i in range(len(x)):
    plt.plot([0,x[i]],[0,y[i]],"b")
    
plt.plot([0,x[right]],[0,y[right]],"y")    
plt.plot(w_x,w_y,"r") 
plt.plot(w[0],w[1],"ro")

plt.xlabel("w: red line  yellow : y_hat  blue :others")
plt.show()

