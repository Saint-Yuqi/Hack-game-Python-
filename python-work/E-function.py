import sys
import stdio

def gcd (a,b):
   if a==0:
       return b
   return gcd(b%a,a)

def phi(n):
    result =1
    for i in range(2,n):
        if (gcd(i,n) ==1):
            result+=1
    return result

k= int(sys.argv[1])
phi(k)
stdio.writeln("phi= "+ str(phi(k)))
    



