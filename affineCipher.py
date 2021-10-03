# Affine cipher

validKey1 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def encrypt():
    eText = []
    pText = input("Enter plain text: ").lower()
    key1 = int(input("Enter key 1: "))
    key2 = int(input("Enter key 2: "))

    if(not pText.isalpha()):
        print("Plain Text should be an alphabet without space")
        exit()
    if(key1 not in validKey1):
        print("key 1 is invalid")
        exit()

    # print(ord("a"), ord("A"))
    for c in pText:
        c = ord(c) - 97
        t = (c*key1) % 26
        e = (t + key2) % 26
        eText.append(chr(e+65))
    
    eText = "".join(eText)
    print("Encrypted Text: " + eText)

def decrypt():
    pText = []
    eText = input("Enter cipher text: ").upper()
    key1 = int(input("Enter key 1: "))
    key2 = int(input("Enter key 2: "))

    if(not eText.isalpha()):
        print("Cipher Text should be an alphabet without space")
        exit()
    if(key1 not in validKey1):
        print("key 1 is invalid")
        exit()

    for x in range(1, 26):
        if (((key1 % 26) * (x % 26)) % 26 == 1):
            inverseKey1 = x

    for c in eText:
        c = ord(c) - 65
        t = (c - key2) % 26
        p = (t * inverseKey1) % 26
        pText.append(chr(p + 97))
    
    pText = ''.join(pText)
    print("Plain Text: " + pText)

print("Affine Cipher: \n1. for Encryption \n2. for decryption")
choice = int(input("Enter choice: "))

if(choice == 1):
    encrypt()
elif(choice == 2):
    decrypt()
else:
    print("Enter correct choice")