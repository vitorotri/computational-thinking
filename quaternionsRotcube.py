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



# Program that shows the animation of a rotating cube with edges of 4 different colors, using quaternions
# for the computations.

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

def hermitian(Q):
	return np.matrix.trace(Q) - Q

def cartesian(Q):
	Q1 = np.matrix.trace(np.matmul(s1,Q))/2j
	Q2 = np.matrix.trace(np.matmul(s2,Q))/2j
	Q3 = np.matrix.trace(np.matmul(s3,Q))/2j
	return np.array([Q1.real,Q2.real,Q3.real])

def norm(Q):
	S = cartesian(Q)
	return math.sqrt(S[0]**2 + S[1]**2 + S[2]**2 + S[3]**2)

global s1, s2, s3

s1 = np.array([[0,1],[1,0]])
s2 = np.array([[0,-1j],[1j,0]])
s3 = np.array([[1,0],[0,-1]])
I = np.array([[1,0],[0,1]])

Q1 = 1j*np.array(1*s1 + 1*s2 + 1*s3)
Q2 = 1j*np.array(1*s1 -1*s2 + 1*s3)
Q3 = 1j*np.array(-1*s1 + 1*s2 + 1*s3)
Q4 = 1j*np.array(-1*s1 -1*s2 + 1*s3)
Q5 = 1j*np.array(1*s1 + 1*s2 -1*s3)
Q6 = 1j*np.array(1*s1 -1*s2 -1*s3)
Q7 = 1j*np.array(-1*s1 + 1*s2 -1*s3)
Q8 = 1j*np.array(-1*s1 -1*s2 -1*s3)

Q = np.array([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8])

plt.style.use('dark_background')
fig1 = plt.figure(1)
ax = plt.axes(projection="3d")

theta = 0.0
stepx = 0.02*np.pi
stepy = 0.02*np.pi

n = np.array(1*s1 + 0*s2 + 0*s3) # around x axis
Ux = math.cos(stepx)*I + 1j*n*math.sin(stepx)
Uxh = math.cos(stepx)*I - 1j*n*math.sin(stepx)
n = np.array(0*s1 + 1*s2 + 0*s3) # around y axis
Uy = math.cos(stepy)*I + 1j*n*math.sin(stepy)
Uyh = math.cos(stepy)*I - 1j*n*math.sin(stepy)

while theta <= 20*np.pi:
	C = np.zeros([8,3])
	for i in range(8):
		R0 = Ux @ Q[i] @ Uxh
		R1 = Uy @ R0 @ Uyh
		C[i,:] = cartesian(R1)
		Q[i] = np.copy(R1)
	ax.clear()
	ax.plot3D([C[0,0],C[2,0]],[C[0,1],C[2,1]],[C[0,2],C[2,2]],"-c")
	ax.plot3D([C[0,0],C[1,0]],[C[0,1],C[1,1]],[C[0,2],C[1,2]],"-c")
	ax.plot3D([C[0,0],C[4,0]],[C[0,1],C[4,1]],[C[0,2],C[4,2]],"-c")
	ax.plot3D([C[5,0],C[1,0]],[C[5,1],C[1,1]],[C[5,2],C[1,2]],"-b")
	ax.plot3D([C[5,0],C[4,0]],[C[5,1],C[4,1]],[C[5,2],C[4,2]],"-b")
	ax.plot3D([C[5,0],C[7,0]],[C[5,1],C[7,1]],[C[5,2],C[7,2]],"-b")
	ax.plot3D([C[6,0],C[4,0]],[C[6,1],C[4,1]],[C[6,2],C[4,2]],"-r")
	ax.plot3D([C[6,0],C[2,0]],[C[6,1],C[2,1]],[C[6,2],C[2,2]],"-r")
	ax.plot3D([C[6,0],C[7,0]],[C[6,1],C[7,1]],[C[6,2],C[7,2]],"-r")
	ax.plot3D([C[3,0],C[1,0]],[C[3,1],C[1,1]],[C[3,2],C[1,2]],"-g")
	ax.plot3D([C[3,0],C[2,0]],[C[3,1],C[2,1]],[C[3,2],C[2,2]],"-g")
	ax.plot3D([C[3,0],C[7,0]],[C[3,1],C[7,1]],[C[3,2],C[7,2]],"-g")
	ax.axis('off')
	ax.set_xlim(-1.5,1.5)
	ax.set_ylim(-1.5,1.5)
	ax.set_zlim(-1.5,1.5)
	theta += stepx
	plt.pause(0.05)
