import sys
import stdio
import math
import random
import stdarray

n=int(sys.argv[1])
enterPeople =1
count=0
average=float(0)
birthday=stdarray.create1D(365,False)
  
              
     

for k in range(n):
    count=0
    for i in range(365):
        birthday[i]=0
    Birthday=random.randrange(0,365)
    while birthday[Birthday] <1:
        birthday[Birthday]+=1
        count +=1
        Birthday=random.randrange(365)
    average=(average*k+count)/(k+1)
stdio.writeln('Average:'+str(average))
