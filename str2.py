prefixes = 'JKLMNOPQ'
suffix = 'ack'
suf = 'uack'
for letter in prefixes:
    if(letter == 'O'):
        print letter + suf
    elif(letter == 'Q'):
        print letter + suf
    else:
        print letter + suffix
