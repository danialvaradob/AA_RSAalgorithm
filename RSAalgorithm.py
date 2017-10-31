#https://gist.github.com/JonCooperWorks/5314103

import datetime
import random

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


def coprime(L):
    '''returns 'True' if the values in the list L are all co-prime
       otherwier, it returns 'False'. '''

    for i in range(0, len(L)):
        for j in range(i + 1, len(L)):
            if euclid(L[i], L[j]) != 1:
                return False

    return True

def euclid(a, b):
    '''returns the Greatest Common Divisor of a and b'''
    a = abs(a)
    b = abs(b)
    # make sure the algorithms still works even when
    # some negative numbers are passed to the program

    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def modInv(a, m):
    '''returns the multiplicative inverse of a in modulo m as a
       positve value between zero and m-1'''
    # notice that a and m need to co-prime to each other.
    if coprime([a, m]) == False:
        return 0
    else:
        linearcombination = extendedEuclid(a, m)
        return linearcombination[1] % m


def extendedEuclid(a, b):
    '''return a tuple of three values: x, y and z, such that x is
       the GCD of a and b, and x = y * a + z * b'''
    footprint = []

    # the boolean flag is used to make sure this function can return
    # right answer no matter which is bigger.
    if a < b:
        isASmallerThanB = True
        a, b = b, a
    else:
        isASmallerThanB = False
    while b != 0:
        footprint.append((a % b, 1, a, -(a // b), b))
        # for each tuple in list footprint
        # footprint[i][0] == footprint [i][1] * footprint[i][2]
        #                  + footprint [i][3] * foorprint[i][4]
        # and
        # footprint[i][4] == footprint[i+1][0]
        # this two equations are key to generate the linear combination
        # of a and b so that the result will be their GCD (or GCF).
        a, b = b, a % b

    # Start work backward to compute the linear combination
    # of a and b so that this combination gives the GCD of a and b
    footprint.reverse()
    footprint.pop(0)
    # print (footprint)
    x = footprint[0][1]
    y = footprint[0][3]
    # print (x, y)
    for i in range(1, len(footprint)):
        x_temp = x
        y_temp = y
        x = y_temp * footprint[i][1]
        y = y_temp * footprint[i][3] + x_temp
        # print (x, y)

    if (isASmallerThanB != True):
        return (a, x, y)
    else:
        return (a, y, x)


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

'''
Returns the coprime number of n
'''
def get_coprime(n,z,coprime):
    while coprime<z:
        if is_corpime(coprime,n) and is_prime(coprime):
            #print("\nthe CoPrime number is:",coprime)
            return coprime
        coprime += 1


def get_coprime2(n):
    while True:
        e = random.randint(1, n)
        if coprime([e, n]):
            break
    return e
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
def getED(n,phi):
    e = 3
    # This loop makes sure that the coprime generated (e)
    # also has a multiplicative inverse ((d*1)mod phi = 1 )
    while True:
        #e = get_coprime(n,phi,e)
        e = get_coprime2(n)
        d2 = multiplicative_inverse(e,phi)
        #d = modinv(e, phi)
        d = modInv(e,n)
        if d != None:
            return e,d
        e+=1



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
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    '''modExp(a, d, n):
        returns a ** d (mod n)     ---->    mod(char,key,n) '''
    plain = [chr(modExp(char,key,n)) for char in ciphertext]

    #plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


'''
Returns the number of bytes in a string
'''
def utf8len(s):
    return len(s.encode('utf-8'))

if __name__ == '__main__':
    print("TIME STARTED:", datetime.datetime.now().time())
    print(datetime.datetime.now().time())
    print("RSA Encrypter/ Decrypter")
    #p = 53
    #q = 61
    p = 6073
    q = 2371
    message = input("Enter a message to encrypt with your private key: ")
   # message = "Message sent so the experiment can be made, there should be more bytes.\
     #          47 bytes is not enough.five.Message sent so the experiment can be made, there should be more bytes. 47 bytes is not enough.five."
    #print("My original message is:",message)
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