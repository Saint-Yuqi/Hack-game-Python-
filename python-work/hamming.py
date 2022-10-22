import stdio
def Hamming(string, distance):
    if distance == 0: return [string]
    if not string: return []
    return ['0' + item for item in Hamming(string[1:], distance -
        (int(string[0]) ^ 0))] + ['1' + item for item in Hamming(string[1:],
        distance - (int(string[0]) ^ 1))]

def main():
    stdio.writeln(Hamming("1100", 2))

if __name__ == "__main__": main()
