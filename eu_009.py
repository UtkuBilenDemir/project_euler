# https://projecteuler.net/problem=9

n_range = range(1, 1000)
for a in n_range:
    for b in n_range:
        c = (a**2 + b**2)**(1/2)
        if c == int(c) and a + b + c == 1000:
            print(f"a: {a}\nb: {b}\nc: {c}\nabc: {a*b*c}")