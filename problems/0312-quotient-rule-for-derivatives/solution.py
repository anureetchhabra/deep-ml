import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    a = 0
    g = len(g_coeffs)
    h = len(h_coeffs)
    ad = 0
    bd = 0

    for i in range(g):
        a += g_coeffs[i] * x**(g - i-1)
        if (g - i - 2)<0:
            continue
        ad += (g - i -1) * g_coeffs[i] * x**(g - i - 2)
    

    b = 0
    for i in range(h):
        b += h_coeffs[i] * x**(h - i -1)
        if (h- i - 2)<0:
            continue
        bd += (h - i -1 ) * h_coeffs[i] * x**(h - i - 2)
    # print(a,ad,b,bd)

    # b = h_coeffs[0] * x**2 + h_coeffs[1] * x + h_coeffs[2] 
    # bd = 2 * h_coeffs[0] * x + h_coeffs[1]

    return (ad*b - bd*a) / (b**2)