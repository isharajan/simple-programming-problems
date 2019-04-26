def fermet_check(a,b,c,n):
    if(c2==c1):
        print("true")
    
    if(n>2):
        print("YES")
    else:
        print("NO")

#fermat's thearem  to prove a^n +b^n = c^n

a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
n=int(input("enter n value:"))
c1=c**n
a1=a**n
b1=b**n
#print("c1:",c1)
#print("a1:",a1)
#print("b1:",b1)
c2=a1+b1
if(c2==c1):
    print(c2)
fermet_check(a1,b1,c1,n)


        
        
