from Verifier import *

def verifyLength(codeword, message, sequence):
    if (len(codeword) == (len(message) + len(sequence) - 1)):
        return 1
    else:
        print('Receiver Error: Receieved message length differs from that of original sequence! Please retry transmission.')
        return 0

def receiveData(codeword, divisor, message, sequence):    
    remainder = mod2divide(codeword,divisor)

    if ((int(remainder) * 1) != 0):
        print('Receiver: There was an error in the division')
    else:
        print('Receiver: Dataword "' + codeword[0:len(divisor)] + '" was recieved in success')
    return remainder