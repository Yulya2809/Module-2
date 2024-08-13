numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    print(i)
for i in range(len(numbers)):
    is_prime = True
    if numbers[i] < 2:
        continue
    if numbers[i] >= 2:
        for a in range(2, int(numbers[i] - 1)):
            if numbers[i] % a == 0:
                is_prime = False
                break
        if not is_prime:
           not_primes.append(numbers[i])
        else:
            primes.append(numbers[i])
is_prime = True
print('Primes:', primes)
print('Not Primes:', not_primes)
