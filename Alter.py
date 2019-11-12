# Alter Bitch

def alter(sequence):
    intyp = 'r'
       
    while(intyp == 'n' | intyp == 'm' | intyp == 'r'):
        intyp = input('What type of error is desired? (no error "n", manual error "m", random error "r")') 
        if intyp is 'n':
            sequence = sequence
        elif intyp is 'm':
            errseq = ' '
            while(len(errseq) != len(sequence)):
                errseq = input('Type Error Sequence')
        elif intyp is 'r':
            print('random')

    print(sequence)