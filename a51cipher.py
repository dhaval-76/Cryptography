import sys

x = [int(i) for i in "1010101010101010101"]
y = [int(i) for i in "1100110011001100110011"]
z = [int(i) for i in "11100001111000011110000"]

def validateInput(pText):
  if not pText.isdigit():
    print("Enter plain text only in 0 and 1")
    sys.exit()

  for p in pText:
    if not int(p) in [0,1]:
      print("Enter plain text only in 0 and 1")
      sys.exit()

  return [int(i) for i in pText]

def major(xyz):
  bitCount = {0: 0, 1: 0}
  for i in xyz:
    bitCount[i] += 1

  if bitCount[0] > bitCount[1]:
    return 0
  else:
    return 1

def a51Cipher(x, y, z):
  pText = input("Enter the plain text: ")

  pText = validateInput(pText)
  n = len(pText)
  keyStream = []
  cText = []
  
  for i in range(n):
    maj = major([ x[8], y[10], z[10] ])
    if x[8] == maj:
      t = x[13] ^ x[16] ^ x[17] ^ x[18]
      x = [t] + x[:-1]
    if y[10] == maj:
      t = y[20] ^ y[21]
      y = [t] + y[:-1]
    if z[10] == maj:
      t = z[7] ^ z[20] ^ z[21] ^ z[22]
      z = [t] + z[:-1]

    key = x[18] ^ y[21] ^ z[22]
    print("key at ", i + 1, " position = ", key)
    keyStream.append(key)
    cText.append(pText[i] ^ key)

  print("Cipher Text =  ", "".join([str(i) for i in cText]))

a51Cipher(x, y, z)