#https://gist.github.com/JonCooperWorks/5314103

import datetime
import random
import math
from math import log
import time

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

'''
Euclid's algorithm for finding the multiplicative inverse of two numbers
'''
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        #print('modular inverse does not exist')
        kit = 0
    else:
        return x % m


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


'''
Determines if two numbers are coprime
'''
def is_corpime(a, b):
    return gcd(a, b) == 1

'''
Returns the coprime number of n
'''
def get_coprime(n,z,coprime):
    while coprime<z:
        if is_corpime(coprime,n) and is_prime(coprime):
            #print("\nthe CoPrime number is:",coprime)
            return coprime
        coprime += 1


'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


'''
Tests to see if a number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

'''
Gets the integer e, thats coprime with n and the multiplicative inverse
of this e
'''
def getED(n,z):
    e = 2
    # This loop makes sure that the coprime generated (e)
    # also has a multiplicative inverse ((d*1)mod phi = 1 )
    while True:
        e = get_coprime(n,z,e)
        d = modinv(e, z)
        if d != None:
            return e,d
        e+=1

def int2baseTwo(x):
    '''x is a positive integer. Convert it to base two as a list of integers
    in reverse order as a list.'''
    # repeating x >>= 1 and x & 1 will do the trick
    assert x >= 0
    bitInverse = []
    while x != 0:
        bitInverse.append(x & 1)
        x >>= 1
    return bitInverse

def modExp(a, d, n):
    '''returns a ** d (mod n)'''
    # a faster algorithms discussed in CIT 592 class
    assert d >= 0
    assert n >= 0
    base2D = int2baseTwo(d)
    base2DLength = len(base2D)
    modArray = []
    result = 1
    for i in range(1, base2DLength + 1):
        if i == 1:
            modArray.append(a % n)
        else:
            modArray.append((modArray[i - 2] ** 2) % n)
    for i in range(0, base2DLength):
        if base2D[i] == 1:
            result *= base2D[i] * modArray[i]
    return result % n

def generate_keypair(p, q):
    # p and q should be not equal, prime numbers
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Get e and integer thats coprime to phi
    # Use Euclid's Algorithm to generate the private key
    e,d = getED(n,phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into its components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #cipher = [(1256**key)%n]
    # Return the array of bytes
    return cipher

def encryptBytes(pk,plaintext):
    key,n = pk
    cipher = (plaintext**key) % n
    return cipher

def decryptBytes(pk,ciphertext):
    key, n = pk
    plaintext = modExp(ciphertext, key, n)
    return plaintext

def  slow_decrypt(pk,ciphertext):
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    #plain = [chr((char ** key) % n) for char in ciphertext]
    '''modExp(a, d, n):
            returns a ** d (mod n)     ---->    mod(char,key,n) '''
    # plain = [chr(modExp(char,key,n)) for char in ciphertext]
    plain = []
    for char in ciphertext:
        # plain.append(chr((char ** key) % n))
        plain.append(chr(modExp(char, key, n)))
    # Return the array of bytes as a string
    return ''.join(plain)


'''
Returns the number of bytes in a string
'''
def utf8len(s):
    return len(s.encode('utf-8'))



def bytes_needed(n):
    if n == 0:
        return 1
    return int(log(n, 256)) + 1

def get_digits_amount(n):
    c = 0
    while n > 0:
        n = n//10
        c+=1
    return c


def baseMainSlowDecryp(message,loops):
    print("SLOW RSA Encrypter/ Decrypter")
    # p = 36568813
    # q = 36568627
    #p = 28724974744256171210604537402133690870051111739655285872546166668885450610413079893885519106791870497
    #q = 28554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153
    #p = 11
    #q = 5
    #p = 53
    #q = 61
    p = 821
    q = 811
    c = 0
    for i in message:
        c += 1
    print("Amount of chars", c)
    # print("Amount of Bytes:",bytes_needed(message))
    start = time.process_time()
    for i in range(loops):
        public, private = generate_keypair(p, q)
        encrypted_msg = encrypt(public, message)
        slow_decrypt(private, encrypted_msg)
    end = (time.process_time()) - start
    #print("TOTAL TIME:", end)
    print("AVG TIME:", (end / loops))


def baseMainSmallPrimes(message,loops):
    print("RSA Encrypter/ Decrypter")
    # p = 36568813
    # q = 36568627
    p = 821
    q = 811
    #p = 53
    #q = 61
    c = 0
    for i in message:
        c+=1
    print("Amount of chars",c)
    #print("Amount of Bytes:",bytes_needed(message))
    start = time.process_time()
    for i in range(loops):
        public, private = generate_keypair(p, q)
        encrypted_msg = encrypt(public, message)
        decrypt(private, encrypted_msg)
    end = (time.process_time()) - start
    #print("TOTAL TIME:", end)
    print("AVG TIME:", (end /loops))

def baseMain(message,loops):
    print("RSA Encrypter/ Decrypter")
    # p = 36568813
    # q = 36568627
    p = 28724974744256171210604537402133690870051111739655285872546166668885450610413079893885519106791870497
    q = 28554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153
    c = 0
    for i in message:
        c+=1
    print("Amount of chars",c)
    #print("Amount of Bytes:",bytes_needed(message))
    start = time.process_time()
    for i in range(loops):
        public, private = generate_keypair(p, q)
        encrypted_msg = encrypt(public, message)
        decrypt(private, encrypted_msg)
    end = (time.process_time()) - start
    print("TOTAL TIME:", end)
    print("AVG TIME:", (end /loops))


def main(message):
    print("TIME STARTED:", datetime.datetime.now().time())
    print(datetime.datetime.now().time())
    print("RSA Encrypter/ Decrypter")
    # p = 53
    # q = 61
    p = 28724974744256171210604537402133690870051111739655285872546166668885450610413079893885519106791870497
    q = 28554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153
    # message = "Message sent so the experiment can be made, there should be more bytes.\
    #          47 bytes is not enough.five.Message sent so the experiment can be made, there should be more bytes. 47 bytes is not enough.five."
    # print("My original message is:",message)
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    print("Number of bytes in the message:", utf8len(message))
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
    print("TIME FINISHED:", datetime.datetime.now().time())


def only_one_encrypt(message):
    print("RSA Encrypter/ Decrypter")
    # p = 36568813
    # q = 36568627
    p = 28724974744256171210604537402133690870051111739655285872546166668885450610413079893885519106791870497
    q = 28554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153
    if (p*q < m):
        print("WONT WORK")
    #print(get_digits_amount(q))
    #message = 2855485774340213530577428341258821872585835054280096549765171646333142907314476525515859307059809215328554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153
    print("Amount of Digits:", get_digits_amount(m))
    #start = datetime.datetime.now()
    start = time.process_time()
    for i in range(100):
        public, private = generate_keypair(p, q)
        encrypted_msg = encryptBytes(public, message)
        k = decryptBytes(private, encrypted_msg)
    if k == m:
        print("SUCCESS")
    end = (time.process_time() ) - start
    print("TOTAL TIME:", end)
    print("AVG TIME:", (end / 100))



if __name__ == '__main__':
    #m = 28554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598095497651716463331429073144765255158593070598092153285548577434021353057742834125882187258583505428009654976517164633314290731447652551585930705980921532855485774340213530577428341258821872585835054280096549765171646333142907314476525515859307059809215328554857743402135305774283412588218725858350542800965497651716463331429073144765255158593070598092153652551585930705980921532855485774340213530577428341258821872585835054280096549765171646333142907314476447652551585935255158593070598092153
    #m = 55158593070598092153652551585930705980921532855485774340213530577428341258821872585835054280096549765171646333142907314476447652551585935255158593070598092153
    #m = 35054280096549765171646333142907314476447652551585935255158593070598092153

    m = 12345
    print("USING A LITTLE BIGER BUT SMAL PRIME NUMBERS TO ENCRYPT AND DECRYPT",53,61)
    print("\n")
    #only_one_encrypt(m)
    baseMainSlowDecryp("a",2)
    baseMainSlowDecryp("aaaaaa", 2)
    baseMainSlowDecryp("aaaaaaaaaaaa", 2)
    baseMainSlowDecryp("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 2)
    baseMainSlowDecryp("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 2)
    baseMainSlowDecryp("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 2)
    print("----"*10)
    baseMainSmallPrimes("a", 100)
    baseMainSmallPrimes("aaaaaa", 100)
    baseMainSmallPrimes("aaaaaaaaaaaa", 100)
    baseMainSmallPrimes("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100)
    baseMainSmallPrimes("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 100)
    baseMainSmallPrimes("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                       100)

'''
    print("TIME STARTED:", datetime.datetime.now().time())
    start = datetime.datetime.now()
    print("RSA Encrypter/ Decrypter")
    p = 36568813
    q = 36568627
    #p = 6073
    #q = 2371
    #p = 821
    #q = 811
    #p = 31
    #q = 57
    #message = input("Enter a message to encrypt with your private key: ")
    #message = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #message = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    message = "a"
    print("My original message is:",message)
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    print("Number of bytes in the message:",utf8len(message))
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))
    print("TIME FINISHED:",datetime.datetime.now().time())
    end = (datetime.datetime.now()) - start

    print("Microseconds:",end.microseconds)
    print("Seconds:",end.seconds)
    print("Seconds:",end.seconds)

'''








''' 
First Time: HI
TIME STARTED: 19:22:54.737357
19:22:54.737402
RSA Encrypter/ Decrypter
My original message is: a
Generating your public/private keypairs now . . .
Your public key is  (7, 14399083)  and your private key is  (8223223, 14399083)
Number of bytes in the message: 1
Your encrypted message is: 
26144
Decrypting message with public key  (7, 14399083)  . . .
Your message is:
a
TIME FINISHED: 19:23:22.755519

TIME STARTED: 21:05:44.725552
21:05:44.725597
RSA Encrypter/ Decrypter
My original message is: aa
Generating your public/private keypairs now . . .
Your public key is  (7, 14399083)  and your private key is  (8223223, 14399083)
Number of bytes in the message: 2
Your encrypted message is: 
2614426144
Decrypting message with public key  (7, 14399083)  . . .
Your message is:
aa
TIME FINISHED: 21:06:40.742093

TIME STARTED: 21:07:40.114061
21:07:40.114105
RSA Encrypter/ Decrypter
My original message is: aaa
Generating your public/private keypairs now . . .
Your public key is  (7, 14399083)  and your private key is  (8223223, 14399083)
Number of bytes in the message: 3
Your encrypted message is: 
261442614426144
Decrypting message with public key  (7, 14399083)  . . .
Your message is:
aaa
TIME FINISHED: 21:09:19.062076



'''