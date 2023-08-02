n = int(input())
w = input()

c = n
for i in range(n):

    if c == 1:
        print("1 bottle of {} on the wall, 1 bottle of {}.".format(w, w))
        print("Take it down, pass it around, no more bottles of {}.".format(w))
        continue

    else:
        print("{} bottles of {} on the wall, {} bottles of {}.".format(c, w, c, w))
        if c == 2:
            print("Take one down, pass it around, 1 bottle of {} on the wall.\n\n".format(w))
            c -= 1
        else:
            c -= 1
            print("Take one down, pass it around, {} bottles of {} on the wall.\n\n".format(c, w))


       