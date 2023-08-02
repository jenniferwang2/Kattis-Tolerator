import sys
while True:
    next_line = sys.stdin.readline() 
    if next_line == "0 0\n": #terminating condition met, break out of reading loop
        break

    #otherwise, go through a test case:
    a, b = map(int, next_line.split())
    jack = set([])
    jill = set([])
    for i in range(a):
        jack.add(int(sys.stdin.readline()))
    for i in range(b):
        jill.add(int(sys.stdin.readline()))
    sys.stdout.write(str(len(jack & jill))  + "\n")