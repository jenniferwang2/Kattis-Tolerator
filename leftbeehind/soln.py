import sys
while True: 
    line = sys.stdin.readline() 
    if line == "0 0\n":
        break 
    else: 
        sweet, sour = map(int, line.split())
        if sweet + sour == 13: 
            print("Never speak again.")
        elif sweet > sour:
            print("To the convention.")
        elif sweet < sour:
            print("Left beehind.")
        elif sweet == sour: 
            print("Undecided")
        
            