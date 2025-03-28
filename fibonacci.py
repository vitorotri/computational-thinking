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



# Program that computes the Fibonacci sequence using recursion versus memoization, as well as the elapsed times.

import time

def fib(n):
	if (n <= 1):
		return n
	else:
		return fib(n-1) + fib(n-2)

def fib_memo(n):
	if n <= 1:
		return n
	elif n in cache:
		return cache[n]
	else:
		cache[n] = fib_memo(n-1) + fib_memo(n-2)
		return cache[n]

def print_seq(foo,N):
	for i in range(N):
		print(foo(i))

def time_foo(foo,N):
	tic = time.perf_counter()
	foo(N)
	toc = time.perf_counter()
	print(str(toc-tic) + " s")

N = 35
cache = {}

print_seq(fib,N)
print()
print_seq(fib_memo,N)

print()

time_foo(fib,N)
print()
time_foo(fib_memo,N)


