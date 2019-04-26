def count():
    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print ("the no of a is ",count,"in the string")

count()    
