def is_divisible(x,y):
     if(x%y==0):
         return True
     else:
         return False

x=int(input("enter x value:"))
y=int(input("enter y value:"))
is_divisible(x,y)
print(is_divisible(x,y))       

if is_divisible(x,y):
    print("x is divisible by y")
else:
    print("x is not divisible by y")
