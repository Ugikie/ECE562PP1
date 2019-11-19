from Verifier import *
from Alter import *

def verifyLength(alteredCodeword, codeword):
    if (len(alteredCodeword) == (len(codeword))):
        return True
    else:
        print('Receiver Error: Receieved message length differs from that of original sequence! Please retry transmission.')
        return False

def printSequences(alteredCodeword, codeword, divisor):
    print('Receiver: Altered Codeword: ' + alteredCodeword + '| Syndrome: ' + mod2divide(alteredCodeword,divisor)[0:len(divisor)-1])
    print('Receiver: Original Codeword: ' + codeword + '| Syndrome: ' + mod2divide(codeword,divisor)[0:len(divisor)-1])

def receiveData(alteredCodeword, divisor, codeword, sequence):    
    print('\n')
    remainder = mod2divide(alteredCodeword,divisor)
    if (verifyLength(alteredCodeword,codeword) == False):
        printSequences(alteredCodeword,codeword,divisor)
        

    if ((int(remainder) * 1) != 0):
        print('Receiver: Able to detect an error that was present. Syndrome: ' + remainder + ' Error Pattern: ' + string_xor(alteredCodeword,codeword))
        printSequences(alteredCodeword,codeword,divisor)
        
    else:
        for i in range(len(alteredCodeword)):
            if (alteredCodeword[i] != codeword[i]):
                print('Receiver: Unable to detect an error that was present. Syndrome: ' + remainder)
                printSequences(alteredCodeword,codeword,divisor)
                
        
        print('Receiver: No errors detected because there were none present!')
        printSequences(alteredCodeword,codeword,divisor)

    
    
        

 