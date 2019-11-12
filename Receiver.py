from Verifier import *

def verifyLength(codeword, message, sequence):
    if (len(codeword) == (len(message) + len(sequence) - 1)):
        return 1
    else:
        print('Error: Receieved message length differs from that of original sequence! Please retry transmission.')
        return 0

def receiveData(codeword, divisor, message, sequence):
    if(input('Type 0 for error sequence, or 1 for error-free sequence: ') == '0'):
        verifyLength(codeword, message, sequence)
    
    remainder = mod2divide(codeword,divisor)

    if ((int(remainder) * 1) != 0):
        print('There was an error in the division')
    else:
        print('Nicely done')
    return remainder


def gitHubTest():
    print('test success')