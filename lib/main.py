from copy import copy

count = 0
def increment_count():
    global count
    count = count +1
#increment_count() #callfucntion => add +1 to variable "count"
#print(count)


sbox = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
             [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
             [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
             [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
             [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
             [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
             [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
             [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
             [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
             [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
             [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
             [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
             [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
             [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
             [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
             [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

RCon   = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
# each of its blocks contains a column of 16 bytes (4 x 4)
# one byte contains 8 bits
# 4 x 4 array of bytes -> the STATE array in AES
# 1. Input translate it to hex
# 2. first round key (Input round 0)
# 3. Round 1 (subbyte, shift, mixcol, roundkey) - Round 9
# 4. Round 10 (same, without MIXCOL)
# 5. output



bitkey_128 = "Thats my Kung Fu"
plaintext = "Two One Nine Two"



# convert text to matrix-----------------------------------
def text_To_matrix(text):
    matrix = []
    list_text = list(text)
    for i in range(4):
        listrow = []
        for j in range(4):
            # need to increment through list(text) (4 x 4 matrix) 
            letter = list_text[4 * i + j]
            #convert char to hex
            #-> no need "0x"  ex) 0xd4 -> d4
            letter_to_hex = format(ord(letter), '02x')
            #letter_to_hex = hex(ord(letter))[2:]
            listrow.append(letter_to_hex)
        matrix.append(listrow)
    return matrix

bitkey_128_matrix = text_To_matrix(bitkey_128)
plaintext_matrix = text_To_matrix(plaintext)

#print(bitkey_128_matrix)
#print(plaintext_matrix)

#copied from https://www.codegrepper.com/code-examples/python/transpose+matrix+in+python+without+numpy
# need to edit later
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T

#call function

#matrix = text_To_matrix(text)
#print(transpose(matrix))



#matrix = [['00', '3c', '6e', '47'], ['1f', '4e', '22', '74'], ['0e', '08', '1b', '31'], ['54', '59', '0b', '1a']]
#matrix = [['19', 'a0', '9a', 'e9'], ['3d', 'f4', 'c6', 'f8'], ['e3', 'e2', '8d', '48'], ['be', '2b', '2a', '08']]


#subBytes function-----------------------------
def subBytes(matrix):
    for i in range(4):
        for j in range(4):
            # string format so need to convert to integer
            # Ex. (4a -> left digit: 4   rightdigit -> 10)
            left = int(matrix[i][j][0], 16) #leftdigit
            right = int(matrix[i][j][1], 16) #rightdigit
            # replace value by looking at sbox row col  [2: ] ignore "0x"
            matrix[i][j] = format(sbox[left][right], '02x')
    return matrix
#subBytes(matrix)
#print("sub", matrix)

# shiftRows function-----------------------
def shiftRows(matrix):
    matrix[0] = [matrix[0][0],matrix[0][1],matrix[0][2],matrix[0][3]]
    matrix[1] = [matrix[1][1],matrix[1][2],matrix[1][3],matrix[1][0]]
    matrix[2] = [matrix[2][2],matrix[2][3],matrix[2][0],matrix[2][1]]
    matrix[3] = [matrix[3][3],matrix[3][0],matrix[3][1],matrix[3][2]]
    return matrix
#shiftRows(matrix)
#print("shift", matrix)

# Galois Multiplication  
# Reference: https://medium.com/wearesinch/building-aes-128-from-the-ground-up-with-python-8122af44ebf9
def gmul(matrix, fixed):
    if fixed == 2:
        tmp = matrix << 1
        tmp &= 0xff
        if(matrix & 128) != 0:
            tmp = tmp ^ 0x1b
        return tmp
    if fixed == 3:
        return gmul(matrix, 2) ^ matrix

def mix_col_calc(col):
    # make a copy of col matrix
    copycol = copy(col)
    col[0]  = gmul(copycol[0],2) ^ gmul(copycol[1], 3) ^ copycol[2] ^ copycol[3]
    col[1]  = copycol[0] ^ gmul(copycol[1], 2) ^ gmul(copycol[2], 3) ^ copycol[3]
    col[2]  = copycol[0] ^ copycol[1] ^ gmul(copycol[2], 2) ^ gmul(copycol[3], 3)
    col[3]  = gmul(copycol[0],3) ^ copycol[1] ^ copycol[2] ^ gmul(copycol[3], 2)

    col[0]  = format(col[0], '02x')
    col[1]  = format(col[1], '02x')
    col[2]  = format(col[2], '02x')
    col[3]  = format(col[3], '02x')



# mixcolumn function-----------------------
def mix_columns(matrix):
  #convert all numbers to int to do XOR calculation (mix_col_calc)
  col_matrix = []
  for i in range(4):
    tem = []
    for j in range(4):
      tem.append(int(matrix[j][i], 16))
    col_matrix.append(tem)
  # call mix_col_calc to do XOR calculation (calculate it by one by one) 
  #how mixcolumn works: https://www.youtube.com/watch?v=5PHMbGr8eOA
  # need to transpose after calculation (because it's all filled in row-major order -> need to switch it to column-major order)
  for i in range(4):
    mix_col_calc(col_matrix[i])
  newstatematrix = transpose(col_matrix)
  return newstatematrix
#print("mixcol", mix_columns(matrix))


#Addroundkey-------------------------------
#keyschedule (notAddroundkey)
def addRoundKey222(matrix, nextroundmatrix):
  temp_lastcol = []
  temp_lastcol = [matrix[3][1], matrix[3][2], matrix[3][3], matrix[3][0]]
  #subbytes
  for i in range(4):
    left = int(temp_lastcol[i][0], 16)   #leftdigit
    right = int(temp_lastcol[i][1], 16)  #rightdigit
    temp_lastcol[i] = sbox[left][right]  #int format
  temp_lastcol[0] = temp_lastcol[0] ^ RCon[count]
  increment_count() #increment count for next round 
  #convert to int
  for i in range(4):
    for j in range(4):
      matrix[i][j] = int(matrix[i][j], 16)  
  nextroundmatrix[0] = list(a^b for a,b in zip(matrix[0],temp_lastcol))
  nextroundmatrix[1] = list(a^b for a,b in zip(nextroundmatrix[0],matrix[1]))
  nextroundmatrix[2] = list(a^b for a,b in zip(nextroundmatrix[1],matrix[2]))
  nextroundmatrix[3] = list(a^b for a,b in zip(nextroundmatrix[2],matrix[3]))


def addKey1(state, roundkey):  #XOR current round key
  for i in range(4):
    for j in range(4):
      state[i][j]  = int(state[i][j], 16)
      roundkey[i][j] = int(roundkey[i][j], 16)
  state[0] =  list(a^b for a,b in zip(state[0], roundkey[0]))
  state[1] =  list(a^b for a,b in zip(state[1], roundkey[1]))
  state[2] =  list(a^b for a,b in zip(state[2], roundkey[2]))
  state[3] =  list(a^b for a,b in zip(state[3], roundkey[3]))



#TESTING-----------------------------------------------------
#ROUNDKEY 0-------------------------------------------------
nextroundmatrix = [[],[],[],[]]
addRoundKey222(bitkey_128_matrix,nextroundmatrix)
for i in range(4):
  for j in range(4):
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
    nextroundmatrix[i][j] = format(nextroundmatrix[i][j],'02x')

addKey1(plaintext_matrix, bitkey_128_matrix)

for i in range(4):
  for j in range(4):
    plaintext_matrix[i][j]  = format(plaintext_matrix[i][j], '02x')
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
#ROundkey1-----------------------------------------------------
plaintext_matrix = transpose(plaintext_matrix)
print("sub", subBytes(plaintext_matrix))
print("shift", shiftRows(plaintext_matrix))
plaintext_matrix = mix_columns(plaintext_matrix)
print("mix", plaintext_matrix)
bitkey_128_matrix = nextroundmatrix
print("currentroundkey(1)", bitkey_128_matrix)
nextroundmatrix = [[],[],[],[]]
addRoundKey222(bitkey_128_matrix,nextroundmatrix)

for i in range(4):
  for j in range(4):
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
    nextroundmatrix[i][j] = format(nextroundmatrix[i][j],'02x')

print("next", nextroundmatrix)
bitkey_128_matrix = transpose(bitkey_128_matrix)
addKey1(plaintext_matrix, bitkey_128_matrix)
for i in range(4):
  for j in range(4):
    plaintext_matrix[i][j]  = format(plaintext_matrix[i][j], '02x')
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
print("done", plaintext_matrix)
print("roundkey1", bitkey_128_matrix) # roundkey 1
print("roundkey2", nextroundmatrix)   # roundkey 2
#--------------------------------------------
print("sub", subBytes(plaintext_matrix))
print("shift", shiftRows(plaintext_matrix))
plaintext_matrix = mix_columns(plaintext_matrix)
print("mix", plaintext_matrix)
bitkey_128_matrix = nextroundmatrix
print("currentroundkey(2)", bitkey_128_matrix)
nextroundmatrix = [[],[],[],[]]
addRoundKey222(bitkey_128_matrix,nextroundmatrix)
for i in range(4):
  for j in range(4):
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
    nextroundmatrix[i][j] = format(nextroundmatrix[i][j],'02x')
print("next", nextroundmatrix)
bitkey_128_matrix = transpose(bitkey_128_matrix)
addKey1(plaintext_matrix, bitkey_128_matrix)
for i in range(4):
  for j in range(4):
    plaintext_matrix[i][j]  = format(plaintext_matrix[i][j], '02x')
    bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
print("done", plaintext_matrix)
print("roundkey2", bitkey_128_matrix) # roundkey 2
print("roundkey3", nextroundmatrix)   # roundkey 3





#bitkey_128_matrix = transpose(nextroundmatrix)
#print(bitkey_128_matrix)



#addRoundKey(plaintext_matrix, bitkey_128_matrix, nextroundmatrix)
#addKey1(plaintext_matrix, bitkey_128_matrix)


#for i in range(4):
  #for j in range(4):
    #plaintext_matrix[i][j]  = format(plaintext_matrix[i][j], '02x')
    #bitkey_128_matrix[i][j] = format(bitkey_128_matrix[i][j], '02x')
    #nextroundmatrix[i][j] = format(nextroundmatrix[i][j], '02x')

#print("final", plaintext_matrix)




#nextroundmatrix[0] = matrix[0] ^ temp_lastcol
#print(nextroundmatrix[0][0])


#print(int(matrix[0]))








#print(hex(int("b7", 16) ^ 1))




#ENCRYPTION
#def encrypt(text):
  #matrix_form = text_To_matrix(text)
  #state =  transpose(matrix_form)
  #state = addRoundKey(state)
  #for i in range(1, 10):
    #state = subBytes(state)
    #state = shiftRows(state)
    #state = mix_columns(state)
    #state = addRoundKey(state)
  #state = subBytes(state)
  #state = shiftRows(state)
  #state = mix_columns(state)
  #return state


