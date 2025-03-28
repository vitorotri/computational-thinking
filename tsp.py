# BSD 0-Clause License

# Copyright (c) 2025 Vito Romanelli Tricanico

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.



# Program that tackles the Travelling Salesmam Problem, given a number of cities,
# using simulated annealing with the Metropolis-Hastings algorithm. After cooling,
# the animation will converge to the optimal route.

from numba import jit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math

@jit(nopython=True)
def Energy(x,y):
	E = 0
	for i in range(0,len(x)-1):
		E += math.sqrt((x[i+1] - x[i])**2.0 + (y[i+1] - y[i])**2.0)
	E += math.sqrt((x[-1] - x[0])**2.0 + (y[-1] - y[0])**2.0)
	return E

# euclidean distance
@jit(nopython=True)
def d(i,j,x,y):
	return math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

# metropolis algorithm for 1 temperature
@jit(nopython=True)
def metropolis(N,x,y,T,kB):
	L = len(x)
	xx = np.copy(x)
	yy = np.copy(y)
	xx_best = np.copy(xx)
	yy_best = np.copy(yy)
	E_best = Energy(xx,yy)
	EE = E_best
	
	for n in range(N):
		i, j = np.random.randint(0,len(x)+1,size=2)
		i = i % len(x)
		j = j % len(x)
		DE = d(i,j,xx,yy) + d(i+1,j+1,xx,yy) - d(i,i+1,xx,yy) - d(j,j+1,xx,yy) # delta E
		
		if (DE < 0) or (random.random() < math.exp(-DE/(kB*T))):
			
			# de facto swap segmentss
			if i > j:
				i, j = j, i
			xx[(i+1)%L:(j+1)%L] = xx[(i+1)%L:(j+1)%L][::-1]
			yy[(i+1)%L:(j+1)%L] = yy[(i+1)%L:(j+1)%L][::-1]
			
			# cycle condition
			xx[0], yy[0] = xx[-1], yy[-1]
			
			EE += DE
			
			if EE < E_best:
				E_best = EE
				xx_best = np.copy(xx)
				yy_best = np.copy(yy)
				
	return xx_best,yy_best

# generate random city coordinates instead of reading file
num_cities = 130  # Adjust this number as needed
x = np.random.uniform(0, 700, num_cities)  # X-coordinates between 0-700
y = np.random.uniform(0, 700, num_cities)  # Y-coordinates between 0-700

# close the cycle by appending first coordinate
x = np.append(x, x[0])
y = np.append(y, y[0])


# constants

N = 1000*len(x)
FACTOR = 0.98
kB = 1.0	

# cycle
x = np.append(x,x[0])
y = np.append(y,y[0])

# initial T
T0 = []
for _ in range(100):
	i, j = np.random.randint(0,len(x)+1,size=2)
	i = i % len(x)
	j = j % len(x)
	DE = d(i,j,x,y) + d(i+1,j+1,x,y) - d(i,i+1,x,y) - d(j,j+1,x,y) # delta E
	T0.append(DE)

T = max(T0) # initial temperature
while T > 0.01:
	x,y = metropolis(N,x,y,T,kB)
	T *= FACTOR
	plt.clf()
	plt.plot(x,y,"ko-")
	plt.pause(0.01)

plt.show()
#plt.savefig("Final_Tour.png")
