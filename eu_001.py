# https://projecteuler.net/problem=1

until_10 = [n for n in range(10) if (n%3 == 0 or n%5 == 0)]

print(f"All the natural numbers that are multiples of 3 and 5 under 10 are {until_10}, and their sum is {sum(until_10)}.")

until_1000 = [n for n in range(1000) if (n%3 == 0 or n%5 == 0)]

print(f"\nSum of all the natural numbers that are multiples of 3 and 5 under 1000 is {sum(until_1000)}.")
