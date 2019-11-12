# Alter Bitch

import random
import numpy as np
import math

# Initially, sequence & snr_dB in 'strings'
def snr_noise(seq,snr_dB):
    snr_dB = float(snr_dB)
    snr = 10**(snr_dB/10)
    var = 1/snr
    sigma = math.sqrt(var)

    # err_seq will be 'list' of 'strings' (decimal values)
    err_seq = np.random.normal(0, sigma, len(seq))

    alt_seq = ''
    for k in range(len(seq)):

        # seq_temp will hold the kth decision value of seq
        seq_temp = float(seq[k]) + float(err_seq[k])
        if seq_temp <= 0.5:
            seq_temp = '0'  # decision 1
        else:
            seq_temp = '1'  # decision 0
        alt_seq = alt_seq + seq_temp

    return alt_seq



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
            snr = input('Alter: What is the desired SNR (dB) level?')
            sequence = snr_noise(sequence,snr)
            print(sequence)
    
        return sequence

# def snr_noise(sequence,SNR)



