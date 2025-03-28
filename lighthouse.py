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



# Program that simulates the Gull's Lighthouse problem, using Bayesian inference.

import numpy as np
import matplotlib.pyplot as plt

N = 350 # maximum number of flashes
x0, y0 = 1.5, 2.0 # known x and y, we will try to predict this based on the a's captured in x
theta = np.random.uniform(-np.pi/2, np.pi/2, N) # generate thetas based on the random uniform assumption
a = x0 + y0*np.tan(theta) # generate a's based on known positions of x and y (despite trying to find x and y)

# values for plotting the map
grid_size = 200
x = np.linspace(0, 3, grid_size)
y = np.linspace(0, 3, grid_size)
X, Y = np.meshgrid(x, y)

prior = np.ones((grid_size, grid_size)) # initial uniform prior

fig, ax = plt.subplots()

for i in range(N):
    # Work on meshgrid (X,Y) to visualize posterior
    posterior = (1/np.pi)*Y/(Y**2 + (a[i] - X)**2) * prior
    
    # Normalize the posterior
    posterior /= np.sum(posterior)
    
    # Update prior
    prior = posterior
    
    # Clear axes and reset properties
    ax.cla()
    ax.grid(True)
    ax.set_aspect('equal')
    
    # Plot elements
    ax.plot(x0, y0, 'ok')  # Plot known position
    ax.contourf(X, Y, posterior, levels=30, cmap='magma')
    ax.set_xlim([0, 3])
    ax.set_ylim([0, 3])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f"Step {i+1}")
    
    plt.pause(0.01)

# Compute estimates
x_estimate = np.sum(X * posterior)
y_estimate = np.sum(Y * posterior)
print(f'Expected value estimate of lighthouse position: x = {x_estimate}, y = {y_estimate}')

plt.show()
