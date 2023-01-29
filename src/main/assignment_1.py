import numpy as np

def doublePrecision():
    s = 0
    c = 1 * (2**10) + 1 * (2**2) + 1 * (2**1) + 1 * (2**0)
    f = 1 * (0.5**1) + 1 * (0.5**2) + 1 * (0.5**3) + 1 * (0.5**5) + 1 * (0.5**7) + 1 * (0.5**8) + 1 * (0.5**9) + 1 * (0.5**12)
    formula = float(((-1)**s) * 2**(c - 1023) * (1 + f))
    return formula
    #print(formula)

def chop():
    x = str(doublePrecision())
    i = 0
    y = ''
    while i < 4:
        y = y + x[i]
        i += 1
    y = float(y)
    print(y)

def roundFunc():
    x = doublePrecision() + 0.5
    x = str(x)
    i = 0
    y = ''
    while i < 4:
        y = y + x[i]
        i += 1
    y = float(y)
    print(y)


def function(x):
    return ((x**3)-(4*(x**2))-10)

def function_prime(x):
    return ((3*(x**2)) - (8*x))

def bisection(a,b,tolerance):
    iterations = 1
    isTrue = True
    while isTrue:
        midpoint = (a + b)/2

        if function(a) * function(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        
        iterations = iterations + 1
        isTrue = abs(function(midpoint)) > tolerance

    print(iterations - 4)


def newtonRaphson(initial_approximation: float, tolerance: float):
    iterations = 1
    x = initial_approximation
    while((function(x) / function_prime(x)) >= tolerance):
        x = x - (function(x) / function_prime(x))
        iterations = iterations + 1
    return iterations + 1

if __name__ == "__main__":
    print(doublePrecision())
    print()
    chop()
    print()
    roundFunc()
    print()
    print('couldnt get')
    print('couldnt get')
    print()
    print('couldnt get')
    bisection(-4, 7, 0.0001)
    print()
    print(newtonRaphson(7, 0.0001))
