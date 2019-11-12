# Alter Bitch
def seq_condition(sequence):
    seq_typ = True
    
    for i in range(len(sequence)):
        #make sure all inputs are integers aka no symbols
        if  (int(sequence[i]) > 1):
           seq_typ = False
    return seq_typ

def alter(sequence):
    intyp = 'r'
       
    while((intyp != 'n') | (intyp != 'm') | (intyp != 'r')):
        intyp = input('Alter: What type of error is desired? (No error "n", Manual error "m", Random error "r"): ') 
        if intyp == 'n':
            sequence = sequence
        elif intyp == 'm':
            errseq = ' '
            while(len(errseq) != len(sequence)):
                errseq = input('Alter: Type Error Sequence (Must be same length as codeword): ')
                while (seq_condition(errseq) != True):
                    errseq = input('Alter: Type Error Sequence of only "0"s and "1"s: ')
            sequence = errseq
        elif intyp == 'r':
            print('Alter: random')
    
        return sequence

# def snr_noise(sequence,SNR)



