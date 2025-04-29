import math

def countWellFormedParenthesis(n):
    if n < 0:
        return 0
    return math.comb(2 * n, n) // (n + 1)

if __name__ == "__main__":
    n = int(input("Введите количество пар скобок (n): "))
    result = countWellFormedParenthesis(n)
    print(f"Количество корректных скобочных выражений для n={n}: {result}")