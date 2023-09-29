def vector_multiply(a, b):
    """Multiply two vectors a and b"""
    if len(a) != len(b):
        raise ValueError("Vectors must be of equal length")
    
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result