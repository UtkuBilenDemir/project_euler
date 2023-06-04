# https://projecteuler.net/problem=10
def eratosthenes(n):
    sum, sieve = 0, [True] * (n+1)
    for i in range(2, n+1):
        if sieve[i]:
            sum += i
            for j in range(i**2, n+1, i):
                sieve[j] = False
    return sum


print(eratosthenes(2000000))
