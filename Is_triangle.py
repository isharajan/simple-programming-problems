def Istriangle(a,b,c):
    res1 = a+b
    res2 = b+c
    res3 = c+a
    if(c>=res1):
        print("No")
    elif(a>=res2):
        print("No")
    elif(b>=res3):
        print("No")
    else:
        print("yes")



a = int(input("enter a value:"))
b = int(input("enter b value:"))
c = int(input("enter c value:"))
Istriangle(a,b,c)
