# we are discovered saved yourself
def columnar_encrypt(text, key):
  rows = [list(text[j:j+len(key)]) for j in range(0, len(text), len(key))]
  if len(rows[-1]) < len(key):
      while len(rows[-1]) != len(key):
          rows[-1].append('_')

  eText = ''
  sortedKey = sorted(list(key))
  
  for i in range(len(key)):
    curr_i = key.index(sortedKey[i])
    eText += ''.join([ row[curr_i] for row in rows ])

  print("Encrypted Text: ", eText)
  
def columnar_decrypt(cipher, key):
  if len(cipher) < len(key):
    key = key[:len(cipher)]

  n = len(cipher) // len(key)
  sortedKey = sorted(list(key))
  
  pText = []
  cText = list(cipher)
  msg_indx = 0
  for _ in range(n):
    pText += [[None] * len(key)]

  for i in range(len(key)):
    curr_i = key.index(sortedKey[i])
    for j in range(n):
      pText[j][curr_i] = cText[msg_indx]
      msg_indx += 1
  
  pText = ''.join([ ''.join(i) for i in pText])
  null_count = pText.count('_')
  if(null_count > 0):
    pText = pText[:-null_count]

  print("Plain Text: ", pText)

def row_encrypt(text, key):
  rows = [list(text[j:j+len(key)]) for j in range(0, len(text), len(key))]
  if len(rows[-1]) < len(key):
    while len(rows[-1]) != len(key):
      rows[-1].append('_')

  eText = [[] for _ in range(len(rows))]
  sortedKey = sorted(list(key))
  for i in range(len(rows)):
    for j in range(len(key)):
      curr_i = key.index(sortedKey[j])
      eText[i].append(rows[i][curr_i])

  eText = ''.join([''.join(i) for i in eText])

  print("Encrypted Text: ", eText)

def row_decrypt(cipher, key):
  if len(cipher) < len(key):
    key = key[:len(cipher)]

  rows = [list(cipher[j:j +len(key)]) for j in range(0, len(cipher), len(key)) ]

  pText = [[] for _ in range(len(rows))]
  sortedKey = sorted(list(key))
  for i in range(len(rows)):
    for j in range(len(key)):
      curr_i = sortedKey.index(key[j])
      pText[i].append(rows[i][curr_i])

  pText = ''.join([''.join(i) for i in pText])  
  null_count = pText.count('_')
  if(null_count > 0):
    pText = pText[:-null_count]

  print("Plain Text: ", pText)

print("Transposition Cipher: \n1. for Simple Columnar \n2. for Row")
choice = int(input("Enter choice: "))

if(choice == 1):
  print("Simple Columnar Encryption -->")
  columnar_encrypt(input("Enter plain text: "), input("Enter Key: "))
  print("Simple Columnar Decryption -->")
  columnar_decrypt(input("Enter cipher text: "), input("Enter Key: "))
elif(choice == 2):
  print("Row Encryption -->")
  row_encrypt(input("Enter plain text: "), input("Enter Key: "))
  print("Row Decryption -->")
  row_decrypt(input("Enter cipher text: "), input("Enter Key: "))
else:
    print("Enter correct choice")