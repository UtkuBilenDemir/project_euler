# https://projecteuler.net/problem=12

def primeFactor(p, n=2, li=[]):
    if p == 1:
        return li

    elif p % n == 0:
        p = p//n
        li.append(n)

    else:
        n += 1

    print(p)
    primeFactor(p=p, n=n, li=li)

print(primeFactor(57))
