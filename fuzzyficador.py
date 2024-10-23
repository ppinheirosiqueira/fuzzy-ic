import math

def func_triangular(x,a,b,c) -> float:
    if x <= a or x >= c:
        return 0.0

    if x <= b:
        return (x - a) / (b - a)
    
    return (c - x) / (c - b)

def func_trapezoidal(x,a,b,c,d) -> float:
    if x <= a or x >= d:
        return 0.0

    if x <= b:
        return (x - a) / (b - a)
    
    if x <= c:
        return 1.0

    return (d - x) / (d - c)

def func_gaussiana(x, c, sigma) -> float:
    return math.e**((-(x-c)**2)/2*sigma**2)

def func_sigmoidal(x, a, c) -> float:
    return 1/(1 + math.e**(-a*(x - c)))

def func_sino(x,a,b,c) -> float:
    return 1/(1 + abs((x-c)/a)**(2*b))

def func_z_shaped(x, a, b) -> float:
    if x <= a:
        return 1.0
    
    b_menos_a = b - a

    if x <= (a + b)/2:
        return 1 - 2*((x-b)/(b_menos_a))**2
    
    if x <= b:
        return 2*((b-x)/b_menos_a)**2

    return 0.0

def func_s_shaped(x, a, b) -> float:
    if x <= a:
        return 0.0
    
    b_menos_a = b - a

    if x <= (a + b)/2:
        return 2*((x-b)/b_menos_a)**2    
    
    if x <= b:
        return 1 - 2*((b-x)/(b_menos_a))**2

    return 1.0

def func_cauchy(x, a, c) -> float:
    return 1/(1 + ((x-c)/a)**2)

def func_gaussiana_dupla(x, A, B, c1, c2, sigma1, sigma2) -> float:
    gauss1 = A * math.e**(-((x - c1)**2) / (2 * sigma1**2))
    gauss2 = B * math.e**(-((x - c2)**2) / (2 * sigma2**2))
    return gauss1 + gauss2

def func_pi_shaped(x,a,b,c,d) -> float:
    if x <= a or x >= d:
        return 0.0
    
    if x <= (a+b)/2:
        return 2*((x-a)/(b-a))**2

    if x <= b:
        return 1 - 2*((x-b)/(b-a))**2

    if x <= c:
        return 1.0
    
    if x <= (c+d)/2:
        return 1 - 2*((x-c)/(d-c))**2
    
    return 2*((x-d)/(d-c))**2

def func_exponencial(x,a,c) -> float:
    return math.e**(-abs((x - c) / a))