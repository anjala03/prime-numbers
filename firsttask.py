def prime_numbers(n):
    primes=[]
    for num in range(2, n+1):
        is_prime=True
        for i in range (2, num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes

def print_primes(n):
    primes= prime_numbers(n)
    with open("prime.txt", "w") as f:
        for elements in primes:
            f.write(str(elements) +"\n")

numbers= int(input("Take input from user: "))
print_primes(numbers)
