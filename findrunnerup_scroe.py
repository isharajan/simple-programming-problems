def sort(a):
    l=len(a)
    for i in range(l):
        for j in range(l):
            if(a[i]<a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
                

n = int(input("enter no.of.elements:"))
a =[]
for i in range(n):
    inp = int(input())
    a.append(inp)
print a
res =sort(a)
print(res)
print("the runner up score is ",res[-2])
