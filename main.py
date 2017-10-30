import random

from math import gcd

def isCoprime(a, b):
    return gcd(a, b) == 1

def isPrime(number):
    divisor = 2
    while divisor < number:
        if (number % divisor) == 0:
            return False
        divisor += 1
    return True

def getCoprime(n,z):
    while True:
        coprime = random.randint(2,z-1)
        if isCoprime(coprime,n) and isPrime(coprime):
            print("\nthe CoPrime number is:",coprime)
            return coprime
        coprime += 1

def getCoprime2(n,z):
    coprime = 2
    while coprime<z:
        if isCoprime(coprime,n) and isPrime(coprime):
            print("\nthe CoPrime number is:",coprime)
            return coprime
        coprime += 1

def getD(e,z):
    '''
    Returns the private key D
    :param e: the coprime number and also PUBLIC KEY
    :param z: Constant
    :return: return private key D
    '''
    d = 1
    while True:
        x = (d*e)%z
        if x == 1 and isPrime(d):
            print("\nD is:",d)
            return d
        d+= 1


def getD2(e,z):
    '''
    Returns the private key D
    :param e: the coprime number and also PUBLIC KEY
    :param z: Constant
    :return: return private key D
    '''
    d = 1
    while d<z:
        x = (d*e)%z
        if x == 1 and isPrime(d):
            print("\nD is:",d)
            return d
        d+= 1



def RSA():
    p = 3
    q = 11
    #working with 3 and 11
    #p = getPrimeNumber()
    #while True:
    #    q = getPrimeNumber()
    #    if q != p:
    #        break

    n = p * q
    z = (p - 1) * (q - 1)
    #e = getCoprime(n,z)
    e = 7
    #if gcd(e,n) == 1:
    #    print('Es coprimo')
    #d = getD(e,z)
    # Message to be encrypted
    d = 3
    msg = 89
    print("\nMessage = ", msg)
    c = msg**e
    c = c % n
    print("\nEncrypted data =", c)
    m = c**d
    m = m % n
    print("\nOriginal Message Sent = ", m)

def RSA1():
    #p = 547
    #q = 557
    #p = 53
    #q = 59
    p = 179425579
    q = 179426549
    n = p*q
    z = (p-1)*(q-1)
    e = 3
    #e = getCoprime2(n,z)
    d = getD2(e,z)
    #e = 3
    #d = 2011
    msg = 3126
    print("\nMessage = ", msg)
    encryptedData = (msg**e)%n
    print("\nEncrypted data =", encryptedData)
    decryptedData = ((encryptedData)**d)%n
    print("\nOriginal Message Sent = ", decryptedData)


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp




def getPrimeNumber():
    while True:
        prime = random.randint(100,100000)
        if isPrime(prime):
            return prime



def string2integer(string):
    result = ''
    print(string)
    for i in string:
        value = ord(i) - 90
        result += str(value)
    print(result)
    return int(result)


def integer2string(integer):
    integer = str(integer)
    print(integer)
    result = ''
    for i in integer:
        value = int(i)+90
        c = chr(value)
        result += c
    print(result)
    return result

def getKeys():
    prime1 = getPrimeNumber()
    prime2 = getPrimeNumber()
    #prime1 = 3
    #prime2 = 11
    n = prime1 * prime2
    z = (prime1 - 1) * (prime2 - 1)
    e = getE(z)
    #e = 7
    d = getD(e, z)
    #d = 3
    publicKey = [e, n]
    privateKey = [d, n]

    return publicKey,privateKey

def encryptMessageRSA(message):
    '''
    Encrpyts a message
    :param message: message string to be encrypted
    :return: returns the message encrypted in integers and public key [e,n]
    '''
    publicKey, privateKey = getKeys()
    #msg = string2integer(message)
    msg = message
    n1 = msg**publicKey[0]
    encryptedMsg = n1%publicKey[1]
    print("Message Encrypted",encryptedMsg)
    #encryptedMsg = ((msg**publicKey[0])%publicKey[1])
    return encryptedMsg,privateKey


def decryptMessageRSA(encryptedMsg,privateKey):
    #originalMsgInt = ((encryptedMsg**privateKey[0])%privateKey[1])
    n1 = encryptedMsg**privateKey[0]
    originalMsgInt = n1%privateKey[1]
    #originalmsg = integer2string(originalMsgInt)
    return originalMsgInt



def getE(z):
    e = 2
    while e < z:
        if gcd(e, z) == 1:
            break
        else:
            e += 1
    return e



def RSAmain():
    '''
    while True:
        try:
            msg = int(input('Digite: '))
            break
        except:
            continue
    '''
    msg = 2
    print(msg)
    e,pk = encryptMessageRSA(msg)
    omsg = decryptMessageRSA(e,pk)
    print(omsg)


def RSA2():
    p = 3
    q = 7
    n = p * q
    e = 2
    z = (p - 1) * (q - 1)
    while e < z:
        if gcd(e, z) == 1:
            break
        else:
            e += 1

    k = 2  # Constan value
    d = (1 + (k * z)) / e

    # Message to be encrypted
    msg = 18
    print("\nMessage = ", msg)
    c = msg**e
    c = c % n
    print("\nEncrypted data =", c)
    m = c**d
    m = int(m % n)
    print("\nOriginal Message Sent = ", m)

    return 0


RSA()