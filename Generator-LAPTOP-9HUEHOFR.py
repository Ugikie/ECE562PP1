''' import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

message = input('Enter the message to be sent: ')
bits = text_to_bits(message)
print(bits)
decodedMessage = text_from_bits(bits)
print(decodedMessage) '''

def string_xor(a,b):
    output = ''
    for k in range(len(a)):
        output = output + str((int(a[k]) ^ int(b[k])))
    return output

def shift_string_left(a,inbit = '-1'):
    output = ''
    for k in range(len(a)-1):
        output = output + str(a[k+1])
    if (inbit != '-1'):
        return (output + inbit)
    else:
        return (output)

def mod2divide(dvd,dvs):
    itr = 0
    remainder = dvd
    while (len(remainder) >= len(dvs)):
        itr = itr + 1
        if (int(remainder[0]) == int(dvs[0])):
            if ((len(dvs) + itr) <= len(dvd)):
                remainder = shift_string_left(string_xor(remainder[0:len(dvs)],dvs),dvd[len(dvs) - 1 + itr])
            else:
                remainder = shift_string_left(string_xor(remainder[0:len(dvs)],dvs))
        else:
            if ((len(dvs) + itr) <= len(dvd)):
                remainder = shift_string_left(remainder,dvd[len(dvs) - 1 + itr])
            else:
                return remainder[1:len(remainder)]
    
    return remainder
message = input('Enter a k-bit message of 0s and 1s: ')
sequence = input('Enter an (n+1)-bit generator pattern: ')

while ((int(sequence) * 1) == 0 ):
    print('Error: Cannot use an all-zero sequence! Please try again')
    sequence = input('Enter an (n+1)-bit generator pattern: ') 

dividend = message.ljust(len(message)+len(sequence)-1,'0')
divisor = sequence

print(dividend)
print(divisor)

remainder = mod2divide(dividend,divisor)

# newdivid = ''

# # if (int(dividend[0]) >= int(divisor[0])):
# #     for i in range(len(divisor)):
# #         result = int(dividend[i]) - int(divisor[i])
# #         newdivid = newdivid + str(abs(result))
# #     newdivid = newdivid[1:len(newdivid)] + dividend[len(divisor)]
# # else:    
# #     remainder = dividend
# newdivid = dividend
# for k in range(len(divisor)-1):
#     tmpdivid = newdivid
#     newdivid = ''
#     if (int(tmpdivid[0]) >= int(divisor[0])):
#         for i in range(len(divisor)):
#             result = int(tmpdivid[i]) ^ int(divisor[i])
#             newdivid = newdivid + str(abs(result))
#         newdivid = newdivid[1:len(newdivid)] + dividend[len(divisor) + k]
#     else:    
#         for i in range(len(divisor)):
#             result = int(tmpdivid[i]) - 0
#             newdivid = newdivid + str(abs(result))
#         newdivid = newdivid[1:len(newdivid)] + dividend[len(divisor) + k]

# tmpdivid = newdivid
# if (int(tmpdivid[0]) >= int(divisor[0])):
#         for i in range(len(divisor)):
#             result = int(tmpdivid[i]) ^ int(divisor[i])
#             newdivid = newdivid + str(abs(result))
#         remainder = newdivid[1:len(newdivid)]
# else:    
#     remainder = newdivid[1:len(newdivid)]

print(dividend + ' / ' + divisor + ' Has remainder: ' + remainder)

