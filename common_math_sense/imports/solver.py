from sympy import symbols, solve as sympy_solve, sympify
import re


def solve(equation):
    left, right = equation.split("=")

    expression = sympify(left) - sympify(right)

    letters = set(re.findall(r'\b[a-zA-Z]\b', equation))
    variable = symbols(next(iter(letters)))

    answer = sympy_solve(expression, variable)

    print(f"{variable} = {answer}")