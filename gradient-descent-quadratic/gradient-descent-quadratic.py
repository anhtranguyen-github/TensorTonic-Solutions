def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    while steps >= 0:
        gd = 2*a*x0 + b
        x0 -= lr*gd
        steps -= 1
    return x0