import math

def countWellFormedParenthesis(n):
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)