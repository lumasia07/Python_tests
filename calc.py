"""Module to calc"""
def add(x, y):
    """Add Function"""
    return x + y

def sub(x, y):
    """Sub func"""
    return x - y

def mul(x, y):
    """Mul func"""
    return x * y

def div(x, y):
    """Div func"""
    if y == 0:
        raise ValueError("No div by zero")
    return x / y
