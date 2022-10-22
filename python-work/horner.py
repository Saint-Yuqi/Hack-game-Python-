import sys
import stdio
import stdarray
import math

def evaluate(a,x):
    total=0.0
    for item in a[::-1]:  # a[::-1] it starts from the end. [1,2,3,4] it will output '4,3,2,1' .
        total = item +x*total
    return total
def exp( n):
    total=() # it's a tuple 
    term =1.0
    for i in range (1,n+1):
        total += (term,)  #???????
        term *=1/i
    return total



x = float(sys.argv[1])
e=math.exp(x)
print(evaluate(exp(100),x))
print(e)
