def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
    # while bil <= number:
    #     if number % bil == 0:
    #         print(f'{number} is not a prime number')
    #         break
    #     else:
    #         print(f'{number} is a prime number')
    #     bil += 1


n = int(input("Check this number: "))
prime_checker(number=n)