def print_table(r,c,d=['+','-','|',' '],rl=3,cl=4):
       l1 = (d[0]+d[1]*cl)*c+d[0]+'\n'
       l2 = (d[2]+d[3]*cl)*c+d[2]+'\n'
       return "%s%s"%(("%s%s"%(l1,l2*rl))*r,l1)

r = 3
c = 3
d2 = ['#','*','#',' ']
print print_table(r,c,d2)
