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



# Program that prints all possible permutations of a string, using Heap's algorithm.

import time

def toString(List): 
    return ''.join(List) 
  
#
# Function to print permutations of a string.
# This function takes three parameters: 
#
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string.
#
def heap_permute(a, size):
    if size == 1:
        print(toString(a))
    else:
        for i in range(size):
            heap_permute(a, size - 1)
            if size % 2 == 1:  # If size is odd, swap the first and last element
                a[0], a[size - 1] = a[size - 1], a[0]
            else:  # If size is even, swap the current element with the last element
                a[i], a[size - 1] = a[size - 1], a[i]
  
  
# Driver code 
string = "ABC"
n = len(string) 
a = list(string) 
  
# Function call
tic = time.time()
heap_permute(a, n)
toc = time.time()

print()
print(toc - tic)
