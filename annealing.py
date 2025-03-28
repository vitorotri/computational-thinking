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



# Program to find a global optimum of a function using simulated annealing.

import random
import numpy as np
import matplotlib.pyplot as plt

# example function to optimize: f(x,y) = x^2 + y^2
def energy(x,y):
	return x*x + y*y
	
# function to try new solution
def attempt(x,y,param):
	x += param*(-1)**random.randint(1,10)
	y += param*(-1)**random.randint(1,10)
	return x,y

T, T_min = 100, 0.001 # initial temperature, minimum temperature
x0, y0 = 4.0, 4.0 # initial position
x, y = x0, y0 # initial values
E = energy(x,y) # initial energy
a = 0.98 # cooling factor
param = 0.1 # parameter for energy function

# simulated annealing algorithm
while(T > T_min):
	xn, yn = attempt(x,y,param)
	En = energy(xn,yn)
	DE = En - E
	if (DE < 0) or (random.random() < np.exp(-DE/T)):
		x, y = xn, yn
		E = En	
			
	T *= a
	
	if (E < 1e-10):
		break
		
	# plot	
	plt.clf()
	plt.xlim([-10,10])
	plt.ylim([-10,10])
	plt.plot(0,0,'*b') # goal in this particular case
	plt.plot(x,y,'*r')
	plt.grid(True)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.pause(0.01)
	
plt.show()
