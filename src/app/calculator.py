def add(a, b):
  
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los valores deben ser numéricos.")

    return a + b
