import math

def ehPrimo(n):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range (5, math.ceil(n / 2), 2):
            if (n % i == 0):
                return False
            else:
                continue
        return True
