
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

def verifyRemainder(alteredCodeword, divisor):
    remainder = mod2divide(alteredCodeword,divisor)

    if ((int(remainder) * 1) != 0):
        print('Verifier: There was an error in the division')
        print('Verifier: Altered Codeword: ' + alteredCodeword + '| Remainder: ' + mod2divide(alteredCodeword,divisor)[0:len(divisor)-1])
    return remainder