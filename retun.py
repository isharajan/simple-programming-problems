def compare(x,y):
        
            if(x>y):
                return 1
        
            if(x<y):
                return -1
        
            if(x==y):
                return 0

    
     

x = int(input("enter a x value:"))
y = int(input("enter a y value:"))
print(compare(x,y))
