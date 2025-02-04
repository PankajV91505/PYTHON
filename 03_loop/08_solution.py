number = 28
is_prime_num = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime_num = False
            break
        
    print(is_prime_num , "is a prime number")