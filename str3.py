def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1

    
    
    while j > 0:
        print i,j
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
        
    return True



word1 = 'pots'
word2= 'stop'
is_reverse(word1, word2)

