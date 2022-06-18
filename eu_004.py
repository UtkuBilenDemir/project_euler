# https://projecteuler.net/problem=4

# solution without using itertools
range_3 = range(100, 1000)
palin = 0
for n_1 in range_3:
    for n_2 in range_3:
        prod = str(n_1*n_2)
        if prod == prod[::-1]:
            palin = max(palin, int(prod))
            
print(palin)