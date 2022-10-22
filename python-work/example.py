import sys
import stdio


n = int(sys.argv[1])
a = int(sys.argv[2])
b = int(sys.argv[3])

for i in range(0,100):
    i+=1
    while ((n * i-a)%b == 0):
        stdio.writeln(i)
        break