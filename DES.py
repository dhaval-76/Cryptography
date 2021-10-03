shift_table = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]

key_compression = [14, 17, 11, 24, 1, 5,
                   3, 28, 15, 6, 21, 10,
                   23, 19, 12, 4, 26, 8,
                   16, 7, 27, 20, 13, 2,
                   41, 52, 31, 37, 47, 55,
                   30, 40, 51, 45, 33, 48,
                   44, 49, 39, 56, 34, 53,
                   46, 42, 50, 36, 29, 32]

exp_box = [32, 1, 2, 3, 4, 5, 4, 5,
           6, 7, 8, 9, 8, 9, 10, 11,
           12, 13, 12, 13, 14, 15, 16, 17,
           16, 17, 18, 19, 20, 21, 20, 21,
           22, 23, 24, 25, 24, 25, 26, 27,
           28, 29, 28, 29, 30, 31, 32, 1]

sboxes = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]

perm_box = [16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25]

final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]


def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    binary = ""
    for i in range(len(s)):
        binary = binary + mp[s[i]]
    return binary


def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i:i + 4]
        hex = hex + mp[ch]
    return hex


def shift_left(k, n_shift):
    temp = ""
    for i in range(n_shift):
        for j in range(1, len(k)):
            temp = temp + k[j]
        temp = temp + k[0]
        k = temp
        temp = ""
    return k


def permutation(msg, initial_perm, n):
    permutate = ""
    for i in range(0, n):
        permutate = permutate + msg[initial_perm[i] - 1]
    return permutate


def xor(a, b):
    value = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            value = value + "0"
        else:
            value = value + "1"
    return value


def bin2dec(n):
    return int(n, 2)


def sbox(binary):
    rows = []
    cols = []
    sbox_val = ""
    for i in range(0, len(binary), 6):
        row = bin2dec(binary[i] + binary[i + 5])
        col = bin2dec(binary[i + 1:i + 5])
        rows.append(row)
        cols.append(col)

    for i in range(len(rows)):
        r = rows[i]
        c = cols[i]
        value = bin(sboxes[i][r][c])
        bin_val = value[2:]
        sbox_val = sbox_val + bin_val.zfill(4)
    return sbox_val


msg = "7291649ABC8EF6AB"
key = "5D1A8F29F74EA9BC"
hex_msg = hex2bin(msg)
hex_key = hex2bin(key)

# transform the 64 bit key into 56 bit key
key56 = ""
for i in range(0, len(hex_key), 8):
    key56 = key56 + hex_key[i:i + 7]

print("Length of the transformed key: ", len(key56))
# key into 2 parts of 28 bits
k1 = key56[0:28]
k2 = key56[28:56]

# transform 56 bit key into 16 48-bit keys
key_bin = []
key_hex = []
for i in range(0, 16):
    left = shift_left(k1, shift_table[i])
    right = shift_left(k2, shift_table[i])
    combine = left + right
    round_key = permutation(combine, key_compression, 48)
    key_bin.append(round_key)
    key_hex.append(bin2hex(round_key))


def encryption(hex_msg, key_bin, key_hex):

    # initial permutation
    perm_msg = permutation(hex_msg, initial_permutation, 64)
    print("After first permutation the message is: ", bin2hex(perm_msg))

    # fiestel round starting...
    # break the 64 bit message into 2 parts of 32 bit each
    l1 = perm_msg[0:32]
    r1 = perm_msg[32:64]
    # expansion box - 32 bit message part into 48 bit to XOR with key
    r1_48 = permutation(r1, exp_box, 48)

    # XOR (48 bit msg, 48 bit key)
    # substitution box - 48 bit message into 32 bit
    # 1 permutation
    # a for loop for 16 such rounds of Expansion, XOR, Sbox, Permutation
    # XOR of output and the left half
    # swap of left and right values for 16 rounds
    print("Round\t   \tLeft Half\t   \tRight Half\t    \tHex Key")
    for i in range(0, 16):
        xor_key_msg_48 = xor(r1_48, key_bin[i])
        sbox_msg_32 = sbox(xor_key_msg_48)
        func_output = permutation(sbox_msg_32, perm_box, 32)
        result = xor(l1, func_output)
        l1 = result
        if i != 15:
            l1, r1 = r1, l1
        print(" ", i + 1, "\t\t", bin2hex(l1), "\t\t", bin2hex(r1), "\t\t", key_hex[i])

    cipher = l1 + r1
    cipher = permutation(cipher,final_perm,64)
    return cipher


cipher_text = encryption(hex_msg,key_bin,key_hex)
print("\nFinal Cipher is :", bin2hex(cipher_text))

print("\n---------------CHECKING DECRYPTION---------------\n")
bin_key_rev = key_bin[::-1]
hex_key_rev = key_hex[::-1]
decipher = encryption(cipher_text,bin_key_rev,hex_key_rev)
print("\nGot the message back as: ", bin2hex(decipher))