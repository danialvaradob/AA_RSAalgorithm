#https://gist.github.com/JonCooperWorks/5314103

import datetime
import random
import math

'''
Algorithm used to get different prime numbers. 



'''
#10 ** 100, 10 ** 101,
# a , b
def newKey(a, b):
        ''' Try to find two large pseudo primes roughly between a and b.
        Generate public and private keys for RSA encryption.
        Raises ValueError if it fails to find one'''
        try:
            p = findAPrime(a, b, 50)
            while True:
                q = findAPrime(a, b, 50)
                if q != p:
                    break
        except:
            raise ValueError
        n = p * q
        return (p,q)



def findAPrime(a, b, k):
    '''Return a pseudo prime number roughly between a and b,
    (could be larger than b). Raise ValueError if cannot find a
    pseudo prime after 10 * ln(x) + 3 tries. '''
    x = random.randint(a, b)
    for i in range(0, int(10 * math.log(x) + 3)):
        if millerRabin(x, k):
            return x
        else:
            x += 1
    raise ValueError


def millerRabin(n, k):
    '''
    Miller Rabin pseudo-prime test
    return True means likely a prime, (how sure about that, depending on k)
    return False means definitely a composite.
    Raise assertion error when n, k are not positive integers
    and n is not 1
    '''
    assert n >= 1
    # ensure n is bigger than 1
    assert k > 0
    # ensure k is a positive integer so everything down here makes sense

    if n == 2:
        return True
    # make sure to return True if n == 2

    if n % 2 == 0:
        return False
    # immediately return False for all the even numbers bigger than 2

    extract2 = extractTwos(n - 1)
    s = extract2[0]
    d = extract2[1]
    assert 2 ** s * d == n - 1

def extractTwos(m):
    '''m is a positive integer. A tuple (s, d) of integers is returned
    such that m = (2 ** s) * d.'''
    # the problem can be break down to count how many '0's are there in
    # the end of bin(m). This can be done this way: m & a stretch of '1's
    # which can be represent as (2 ** n) - 1.
    assert m >= 0
    i = 0
    while m & (2 ** i) == 0:
        i += 1
    return (i, m >> i)



print(newKey(10*2,10*3))