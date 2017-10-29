import random


def gcd(a, h):
    while True:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp


def isPrime(number):
    divisor = 2
    while divisor < number:
        if (number % divisor) == 0:
            return False
        divisor += 1
    return True


def getPrimeNumber():
    while True:
        prime = random.randint(2, 10)
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
    #prime1 = getPrimeNumber()
    #prime2 = getPrimeNumber()
    prime1 = 3
    prime2 = 11
    n = prime1 * prime2
    z = (prime1 - 1) * (prime2 - 1)
    #e = getE(z)
    e = 7
    #d = getD(e, z)
    d = 3
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


def getD(e,z):
    '''
    Returns the private key D
    :param e: the coprime number and also PUBLIC KEY
    :param z: Constant
    :return: return private key D
    '''
    d = 1
    while True:
        if (d*e)%z == 1:
            return d
        d+= 1

def RSAmain():
    while True:
        try:
            msg = int(input('Digite: '))
            break
        except:
            continue

    print(msg)
    e,pk = encryptMessageRSA(msg)
    omsg = decryptMessageRSA(e,pk)
    print(omsg)


def RSA():
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
    msg = 22
    c = msg**e
    c = c % n
    print("\nEncrypted data =", c)
    m = c**d
    m = int(m % n)
    print("\nOriginal Message Sent = ", m)

    return 0


RSAmain()