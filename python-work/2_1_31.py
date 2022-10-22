import math

n = 10    #int(input('how many throw:'))
k = 5     #int(input('how many times eagle?:'))
p = 0.4   #float(input('probability of eagle'))

def binomail(n, k, p):
    y, x, z = 1, 1, 1
    approximatey = 0
    approximatex = 0
    approximatez = 0

    for i in range(1, n + 1):
        y *= i
    for i in range(1, y + 1):
        approximatey += math.log(i)

    for i in range(1, n - k + 1):
        x *= i
    for i in range(1, x + 1):
        approximatex += math.log(i)

    for i in range(1, k + 1):
        z *= i
    for i in range(1, z + 1):
        approximatez += math.log(i)

    a = p ** k * (1 - p) ** (n - k) * approximatey / (approximatez * approximatex)
    b = math.log(a)
    e = math.exp(b)
    return e
print(binomail(n, k, p))






















'''
average_eagle = 0

for i in range(n):
    pro_0 = p *
    pro_1 = p *
print(average_eagle)
'''
