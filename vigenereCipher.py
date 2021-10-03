# Vigenere Cipher

def keyInput(text):
  key = input("Enter key: ").lower()
  if(not key.isalpha()):
    print("Key should be an alphabet without space")
    exit()
  
  if len(text) == len(key):
    return key
  else:
    quot = len(text) // len(key)
    rem = len(text) % len(key)
    return key * quot + key[:rem]

def encrypt():
  eText = []
  pText = input("Enter plain text: ").lower()
  if(not pText.isalpha()):
    print("Plain Text should be an alphabet without space")
    exit()
  
  key = keyInput(pText)
  for t, k in zip(pText, key):
    t = ord(t) - ord('a')
    k = ord(k) - ord('a')
    e = (t + k) % 26
    eText.append(chr(e + ord('a')))
  
  eText = "".join(eText)
  print("Encrypted Text: " + eText)


def decrypt():
  pText = []
  eText = input("Enter cipher text: ").lower()
  if(not eText.isalpha()):
    print("Cipher Text should be an alphabet without space")
    exit()
  
  key = keyInput(eText)
  for e, k in zip(eText, key):
    e = ord(e) - ord('a')
    k = ord(k) - ord('a')
    t = (e - k) % 26
    pText.append(chr(t + ord('a')))

  pText = "".join(pText)
  print("Plain Text: " + pText)

print("Vigenere Cipher: \n1. for Encryption \n2. for Decryption")
choice = int(input("Enter choice: "))

if(choice == 1):
  encrypt()
elif(choice == 2):
  decrypt()
else:
  print("Enter correct choice")
