left, right = map(int, input().split())
s = 0


def return_prime_numbers(n):
    prime = []
    for i in range(1, n + 1):
        if n % i == 0:
            prime.append(i)
    return len(prime)


for i in range(left, right+1):
    if return_prime_numbers(i) % 2 == 0:
        s += i
    else:
        s -= i
    #print(i, s)

print(s)

