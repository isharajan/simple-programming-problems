def mysort(a):
    l=len(a)
    for i in range(l):
        for j in range(l):
            if(a[j]<a[i]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

a = [800,50,700,45,100,70]
sorta = mysort(a)
print(sorta)
