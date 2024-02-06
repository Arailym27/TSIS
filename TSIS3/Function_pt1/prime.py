def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = filter(is_prime, numbers)
    return list(prime_numbers)

numbers_input = input()
numbers = list(map(int, numbers_input.split()))
#map-переводит числа в листе в инт 
prime_numbers = filter_prime(numbers)

print(prime_numbers)
