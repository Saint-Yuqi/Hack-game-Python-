import sys
import stdio
import math
import random
import stdarray

m=int(sys.argv[1])
n=int(sys.argv[2])
p=int(sys.argv[3])
a=stdarray.create2D(m+2,n+2,'·')
for i in range(1,m+1):
    
    for k in range(1,n+1):
        r=random.randrange(0,100)
        if (r<=p):             #judge the element be a boom
            a[i][k]='*'
        elif (r > p):
            a[i][k]='·'
        stdio.write(a[i][k]) #appear the graph
        stdio.write('       ')
    stdio.writeln()

for i in range(1,m+1):
    for k in range (1,n+1):
        count= 0
        if a[i][k] == '·':
            if a[i-1][k]=='*':count +=1
            if a[i+1][k]=='*':count +=1
            if a[i][k-1]=='*':count +=1
            if a[i][k+1]=='*':count +=1
            if a[i-1][k-1]=='*':count +=1
            if a[i-1][k+1]=='*':count +=1
            if a[i+1][k-1]=='*':count +=1
            if a[i+1][k+1]=='*':count +=1
            a[i][k]= count
            stdio.write(str(a[i][k]))
            stdio.write('    ')
        if  a[i][k]=='*':
            stdio.write(str(a[i][k]))
            stdio.write('    ')
    stdio.writeln()
    


