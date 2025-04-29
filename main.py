import math

def count_well_formed_parenthesis(n: int) -> int:
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)