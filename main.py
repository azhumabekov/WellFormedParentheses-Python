from count import countWellFormedParenthesis

n = int(input("Введите количество пар скобок (n): "))
result = countWellFormedParenthesis(n)
print(f"Количество корректных скобочных выражений для n={n}: {result}")