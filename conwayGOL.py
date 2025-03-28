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



# Program that simulates Conway's game of life, printing the board generations on the terminal.

import numpy as np
import os
import time
import sys
import random

def neighborhoodperiodic(M):
	
	N = len(M)
	S = np.zeros([N,N],dtype = int)
	R = np.zeros([N,N],dtype = int)
	
	# inner cells
	
	S[1:-1,1:-1] = M[2:,1:-1] + M[0:-2,1:-1] + M[1:-1,2:] + M[1:-1,0:-2] + M[2:,2:] + M[0:-2,0:-2] + M[2:,0:-2] + M[0:-2,2:]
	
	# boundaries
	
	S[1:-1,0] = S[1:-1,N-2]
	S[1:-1,N-1] = S[1:-1,1]
	S[0,1:-1] = S[N-2,1:-1]
	S[N-1,1:-1] = S[1,1:-1]
	
	S[0,0] = S[N-2,N-2]
	S[N-1,N-1] = S[1,1]
	S[0,N-1] = S[N-2,1]
	S[N-1,0] = S[1,N-2]
	
	R = np.copy(M)
	R = np.where((M == 1) & ((S < 2) | (S > 3)),0,np.where((M == 0) & (S == 3),1,R))
	
	return R


C = 30 # grid size (squared) >= 5
grid0 = np.zeros([C,C],dtype = int)
grid1 = np.zeros([C,C],dtype = int)
parray = np.array([C,C],dtype = str)
gen = 1000 # number of generations

# block test
grid0[12][12] = int(1)
grid0[12][13] = int(1)
grid0[13][12] = int(1)
grid0[13][13] = int(1)

# oscillator/blinker test
grid0[3][4] = int(1)
grid0[4][4] = int(1)
grid0[5][4] = int(1)

# glider test
grid0[26][26] = int(1)
grid0[27][26] = int(1)
grid0[28][26] = int(1)
grid0[26][27] = int(1)
grid0[27][28] = int(1)

for t in range(gen):
	os.system("clear")
	
	# random board (comment if undesired)
	if t == 0:
		grid0 = np.array([[(int(1) if random.random() > 0.5 else int(0)) for i in range(C)] for j in range(C)])
	
	grid1 = neighborhoodperiodic(grid0)
	
	parray = np.where(grid1 == 1,"o",".")
	parray = "\n".join(["".join(["{:2}".format(item) for item in row]) for row in parray])
	print(parray)
	grid0 = np.copy(grid1)
	time.sleep(0.08)
	
