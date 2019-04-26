def has_no_e(word):
   # if 'e' in word:
    #    return False
    #else:
     #   return True
    
    for letter in range(len(word)):
        #count = 0
        if (letter != 'e'):
            #count = count + 1
            return True
        #else:
         #   print(count)
    print("no of letters does not contains:",count)
            
        
        
word = "eclipsed"
has_no_e(word)
print(has_no_e)
