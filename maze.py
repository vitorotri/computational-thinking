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



# Program to find shortest path between two points in a weighted connected graph, exemplified as a maze,
# using Prim's algorithm for maze generation and Dijkstra's algorithm for finding the shortest path.
# It shows the generated maze, the user closes the window, and then it prompts the user with the desired
# initial and final positions.

import numpy as np
import matplotlib.pyplot as plt
import adjustText
import copy
import random
import math

# undirected weighted graph
	
def mymin(d,Q,N):
	aux = np.inf
	for i in range(N):
		if d[i] < aux and Q[i] == True:
			aux = d[i]
			idx = i
			
	return idx

def plotgraph(W,N):
	edges = [[],[],[],[]]
	for i in range(N):
		for j in range(i+1,N):
			# plots graph edge
			if W[i,j] < np.inf:
				# optim
				edges[0].append(V[i,0])
				edges[1].append(V[j,0])
				edges[2].append(V[i,1])
				edges[3].append(V[j,1])
	plt.style.use('dark_background')
	# plots graph edges
	plt.plot([edges[0],edges[1]],[edges[2],edges[3]],"w-",linewidth=7)

def flat(X,i,j):
	return X*i + j

def check_list(v,x,y):
	tst = False
	for i in range(len(v)):
		if v[i][0] == x and v[i][1] == y:
			tst = True
	return tst

# main

L = 21 # grid side
N = L**2 # numbers of vertices/cells

V = np.zeros([N,2]) # vertex coordinates
W = np.inf*np.ones([N,N]) # adjacency matrix (start as walls)
F = [] # frontier for Prim's algorithm
prev = -1*np.ones(N) # previous vertex array

Q = np.ones(N,dtype = bool) # unvisited set

d = np.zeros(N) # shortest distances array
d[:] = np.inf
	
# attributes values (positions) to vertices
for i in range(L):
	for j in range(L):
		V[flat(L,i,j)][0] = i
		V[flat(L,i,j)][1] = j
		
# Maze generation (Prim's algorithm)

start_i = random.choice(np.arange(L))
start_j = random.choice(np.arange(L))

M = [] # Maze
M.append([start_i,start_j])

t = 0
while(len(F) != 0 or t == 0):
	
	# compute Frontier cells
	if (start_i+1 < L) and ([start_i+1,start_j] not in M):
		F.append([start_i+1,start_j])
	if (start_j+1 < L) and ([start_i,start_j+1] not in M):
		F.append([start_i,start_j+1])
	if (start_i-1 >= 0) and ([start_i-1,start_j] not in M):
		F.append([start_i-1,start_j])
	if (start_j-1 >= 0) and ([start_i,start_j-1] not in M):
		F.append([start_i,start_j-1])
	
	# randomly chooses one of the elements of F to go to
	start_x,start_y = random.choice(F)
	
	M_bounds = []
	if [start_x+1,start_y] in M:
		M_bounds.append([start_x+1,start_y])
	if [start_x-1,start_y] in M:
		M_bounds.append([start_x-1,start_y])
	if [start_x,start_y+1] in M:
		M_bounds.append([start_x,start_y+1])
	if [start_x,start_y-1] in M:
		M_bounds.append([start_x,start_y-1])
		
	[aux_x,aux_y] = random.choice(M_bounds)
	
	# "Every edge connects two nodes, if only one of the two is part of the maze,
	# then mark the edge and node as part of the maze"
	
	if [start_x,start_y] not in M:
		W[flat(L,aux_x,aux_y)][flat(L,start_x,start_y)] = 1
		W[flat(L,start_x,start_y)][flat(L,aux_x,aux_y)] = 1
	start_i = copy.deepcopy(start_x)
	start_j = copy.deepcopy(start_y)
	
	# append value on M
	M.append([start_x,start_y])
	# remove value from F
	F.remove([start_x,start_y])
	
	t = 1
		
# end Prim's	
 
plotgraph(W,N)
plt.gca().set_aspect('equal')
plt.show()

print("\nPlease, input integer numbers between 0 and " + str(L-1) + "\n")
src_x = int(input("Initial vertex x: ")) # initial vertex x
src_y = int(input("Initial vertex y: ")) # initial vertex y
rec_x = int(input("Final vertex x: ")) # final vertex x
rec_y = int(input("Final vertex y: ")) # final vertex y
src = flat(L,src_x,src_y)
rec = flat(L,rec_x,rec_y)
assert(src < N and rec < N and src >= 0 and rec >=0),"[!] vertex values must be integers the range [0,N-1]\n"
d[src] = 0
S = [] # path

# Dijkstra start

while np.any(Q) == True:
# for t in range(N):
	u = mymin(d,Q,N)
	
	if u == rec:
		break
	
	Q[u] = False
	
	for v in range(N):
		# if W[u,v] != 0 and Q[v] == True:
		if Q[v] == True:
			L = d[u] + W[u,v]
			if L < d[v]:
				d[v] = L
				prev[v] = u

# traversal for path

S = []
u = rec
if prev[u] >= 0:
	while u >= 0:
		S.append(int(u))
		u = prev[int(u)]

S.reverse()

plotgraph(W,N)

# plot path
for i in range(len(S)-1):
	# plots graph edge
	plt.plot([V[S[i],0],V[S[i+1],0]],[V[S[i],1],V[S[i+1],1]],"b-",linewidth=5)

plt.gca().set_aspect('equal')
plt.show()
