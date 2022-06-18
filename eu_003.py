# https://projecteuler.net/problem=3

def sieve(n):
    f_prims = []
    
    f = 2
    while n > 1:
        if not n%f:
            n /= f
        else:
            f += 1
    return f
    
    
print(sieve(600851475143))
        