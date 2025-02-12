def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n   
    res = 1
    mult = x
    while n > 0:
        if n % 2 == 1:
            res *= mult
        mult *= mult
        n //= 2
    return res