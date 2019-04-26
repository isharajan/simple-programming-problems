from cal_fn import addition, subtraction, multiplication, division


print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = int(input("select your choice:1,2,3,4"))
value1 = int(input("enter value  of a:"))
value2 = int(input("enter value  of b:"))


if(choice == 1):
    result = addition(value1,value2)
    print("add =",result)

    
elif(choice == 2):
    result = subtraction(value1,value2)
    print("subtract  =", result)

   
elif(choice == 3):
    result = multiplication(value1,value2)
    print("mulply =", result)
   
elif(choice == 4):
    result = division(value1,value2)
    print("divide =",result)


elif(choice<=0 & choice>4):
    print("invalid choice")

else:
    print("invalid choice")
    
