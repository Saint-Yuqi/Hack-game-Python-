def exp( n):
    total=() # it's a tuple 
    term =1.0
    for i in range (1,n+1):
        total += (term,)  #list all the elements
        term *=1/i
    return total

print(exp(5))