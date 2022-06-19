# https://projecteuler.net/problem=6

n_100 = range(1,101)
print(sum(n_100)**2 - sum([x**2 for x in n_100]))