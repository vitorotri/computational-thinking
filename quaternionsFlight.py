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



# Program that shows the flight path between 2 cities on the globe giving their latitude and longitude, 
# using quaternions for the computations.

import matplotlib.pyplot as plt
import numpy as np
import math
import random

def hermitian(Q):
	return np.matrix.trace(Q) - Q

def cartesian(Q):
	Q0 = 0.5*np.matrix.trace(Q)
	Q1 = np.matrix.trace(np.matmul(s1,Q))/2j
	Q2 = np.matrix.trace(np.matmul(s2,Q))/2j
	Q3 = np.matrix.trace(np.matmul(s3,Q))/2j
	return np.array([Q0.real,Q1.real,Q2.real,Q3.real])

def norm(Q):
	S = cartesian(Q)
	return math.sqrt(S[0]**2 + S[1]**2 + S[2]**2 + S[3]**2)

global s1, s2, s3

s1 = np.array([[0,1],[1,0]])
s2 = np.array([[0,-1j],[1j,0]])
s3 = np.array([[1,0],[0,-1]])
I = np.array([[1,0],[0,1]])

# São Paulo
lat_P = -23.57
lon_P = -46.65

# Zürich
lat_Q = 47.36
lon_Q = 8.55
# New York
#lat_Q = 40.74
#lon_Q = -73.98
# # Tokyo
# lat_Q = 35.68
# lon_Q = 139.75

theta_P = math.radians(lat_P-90)
phi_P = math.radians(lon_P-180)
theta_Q = math.radians(lat_Q-90)
phi_Q = math.radians(lon_Q-180)

P1 = math.sin(theta_P)*math.cos(phi_P)
P2 = math.sin(theta_P)*math.sin(phi_P)
P3 = math.cos(theta_P)

Q1 = math.sin(theta_Q)*math.cos(phi_Q)
Q2 = math.sin(theta_Q)*math.sin(phi_Q)
Q3 = math.cos(theta_Q)

P = 1j*np.array(P1*s1 + P2*s2 + P3*s3)
Q = 1j*np.array(Q1*s1 + Q2*s2 + Q3*s3)

# # if P and Q are already on the unit sphere, no need to compute p and q
# p = P/math.sqrt(P1**2 + P2**2 + P3**2)
# q = Q/math.sqrt(Q1**2 + Q2**2 + Q3**2)

# draw unit sphere
fig = plt.figure()
ax = fig.gca(projection='3d')
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="k")

H = (np.matmul(hermitian(P),Q))
phi_H = math.acos(0.5*np.matrix.trace(H).real/norm(H))
i_n = (H - 0.5*np.matrix.trace(H))/math.sqrt(1 - (math.cos(phi_H))**2)

s = 0.0
while s <= 1.0:
	
	H_s = (math.cos(s*phi_H)*I + i_n*math.sin(s*phi_H))
	slerp = np.matmul(P,H_s)
	path = cartesian(slerp)
	s += 0.01
	
	ax.plot3D(path[1],path[2],path[3],".r")	
	plt.pause(0.01)
