import sys
import stdio

def combinations(str1, index, curr): 
    k = len(str1) 
  
    if (index == k): return
  
    stdio.writeln(curr) 

    for i in range(index + 1, n): 
        curr += str1[i] 
        combinations(str1, i, curr) 
  
        curr = curr.replace(curr[len(curr) - 1], "") 
  
    return

str = "abcdefghijklmn"
n =3
combinations(str[0:n], -1, "") 
  
