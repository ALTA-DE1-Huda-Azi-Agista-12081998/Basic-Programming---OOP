def primeX(x):
    def is_prime(num):
        return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    primes = []
    num = 2
    while len(primes) < x:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes[-1]

print(primeX(1))
print(primeX(5))
print(primeX(8))
print(primeX(9))
print(primeX(10))