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



# Program that prints the necessary moves for the Tower of Hanoi problem, given a number n of discs. The function
# is recursive, using dynamic programming, and the discs are numbered from top to bottom.

def hanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from",src,"to",dest)
    else:
        hanoi(n-1, src, aux, dest)
        print("Move disk",n,"from",src,"to",dest)
        hanoi(n-1, aux, dest, src)

n = 3
_from = 'A'
_dest = 'C'
_aux = 'B'
hanoi(n, _from, _dest, _aux)
