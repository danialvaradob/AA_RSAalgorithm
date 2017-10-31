#https://gist.github.com/JonCooperWorks/5314103

import datetime


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
    #cipher = [(10**key)%n]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
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
    p = 6073
    q = 2371
    #message = input("Enter a message to encrypt with your private key: ")
    message = "aaa"
    print("My original message is:",message)
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    print("Number of bytes in the message:",utf8len(message))
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
    print("TIME FINISHED:",datetime.datetime.now().time())




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