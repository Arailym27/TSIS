def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
#вводим как стр но потом через пробел на цифры
numbers=input().split()
#map(во что конвер,что именно)
numbers=list(map(int,numbers))
#lambda arguments: expression
#filter(function, iterable)
#filter(lambda,iterable)
prime_num=list(filter(lambda x:is_prime(x),numbers))

print(prime_num)