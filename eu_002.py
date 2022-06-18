# https://projecteuler.net/problem=2

n1, n2 = (0,1)
summ = 0

while n2 < 4000000:
    if not n2%2:
        summ += n2
    n1, n2 = n2, n1+n2

print(summ)