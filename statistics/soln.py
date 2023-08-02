import sys
case_number = 1
for i in sys.stdin:
    line = list(map(int, i.split()[1:]))
    minimum = min(line) #converted to a list because a map objects empties itself after you iterate through it once, returning in an valueerror on line 10
    maximum = max(line)
    range = maximum - minimum
    print(f"Case {case_number}: {minimum} {maximum} {range}")
    case_number +=1 
