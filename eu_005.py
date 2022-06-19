# https://projecteuler.net/problem=5

def checker(n, divs = range(11,21)[::-1]):
    out = True
    for div in divs:
        if n%div != 0:
            out = False
            break
    return out

m = 2520
while checker(m) == False:
    m += 10
    
print(m)