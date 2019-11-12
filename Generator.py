
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

from Verifier import *
from Receiver import *
from Alter import *

message = input('Generator: Enter a k-bit message of 0s and 1s: ')
sequence = input('Generator: Enter an (n+1)-bit generator pattern: ')

while ((int(sequence) * 1) == 0 ):
    print('Generator Error: Cannot use an all-zero sequence! Please try again')
    sequence = input('Generator: Enter an (n+1)-bit generator pattern: ') 

dividend = message.ljust(len(message)+len(sequence)-1,'0')
divisor = sequence

print('Generator: Dataword is: ' + message)
print('Generator: Augmented Dataword is: ' + dividend)
print('Generator: n-bit Sequence is: ' + divisor)

remainder = mod2divide(dividend,divisor)

print('Generator: ' + dividend + ' / ' + divisor + ' Has remainder: ' + remainder)

codeword = message + remainder
print('Generator: The Codeword to be sent is: ' + codeword)
print(' ')

codeword = alter(codeword)
verified = verifyRemainder(codeword,divisor)

if ((int(verified) * 1) == 0):
    receiveData(codeword,divisor, message, sequence)