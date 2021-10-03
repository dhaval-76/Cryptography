import sys
import random

def isPrime(n):
  for i in range(2, n//2 + 1):
    if(n%i == 0):
      return False
  return True

def gcd(a, b):
  while(b != 0):
    a, b = b, a % b
  return a

def gcdExtended(a, b): 
  lastremainder, remainder = abs(a), abs(b)
  x, lastx, y, lasty = 0, 1, 1, 0
  while remainder:
    lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
    x, lastx = lastx - quotient*x, x
    y, lasty = lasty - quotient*y, y
  return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)

def generateKeys(p,q):
  n = p * q
  phi = (p-1) * (q-1)
  e = random.randrange(1, phi)
  g = gcd(e, phi)

  while g != 1:
    e = random.randrange(1, phi)
    g = gcd(e, phi)
  g, x, y = gcdExtended(e, phi)
  if g != 1:
    print("Modular inverse does not exist")
    sys.exit()
  d =  x % phi

  return (e, d, n)

def getInput():
  p = input("Enter first prime number: ")
  q = input("Enter second prime number: ")

  if (not p.isdigit()) or (not q.isdigit()):
    print("Data should be an intgers")
    sys.exit()
  p = int(p)
  q = int(q)
  if(not isPrime(p)) or (not isPrime(q)):
    print("p, q should be an prime numbers")
    sys.exit()

  return (p, q)

def encrypt(privKey, n):
  mesg = int(input("Enter a message to encrypt with your private key: "))
  cipher = pow(mesg,privKey,n)
  print("Your encrypted message is: ")
  print(cipher)
  return cipher
   
def decrypt(key, n, ciphertext):
  plain = pow(ciphertext,key,n)

  print("Your decrypted message is:")  
  print(plain)

print("Digital Signature using RSA")
p, q = getInput()
print("Value of p, q: ", p, q)
privKey, publickey, n = generateKeys(p, q)
encrypted_msg = encrypt(privKey, n)
decrypt(publickey, n, encrypted_msg)