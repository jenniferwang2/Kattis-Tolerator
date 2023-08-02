n, t = map(int, input().split())
list = []
list.extend(map(int, input().split()))
ALPHA = "abcdefghijklmnopqrstuvwxyz"
length = len(list)

if t == 1:
    print("7")
elif t == 2:
    if list[0] > list[1]:
        print("Bigger")
    elif list[0] == list [1]:
        print("Equal")
    else:
        print("Smaller")  
elif t == 3:
    x = sorted(list[:3])
    print(x[1])
elif t == 4:
    print(sum(list))
elif t == 5:
    print(sum(i for i in list if i % 2 == 0))
elif t == 6:
    print(''.join(ALPHA[i % 26] for i in list))
else:
    unique = set([0])
    og = 0 
    while True:
        next_index = list[og]
        old = len(unique)
        unique.add(next_index)
        if len(unique) == old:
            print("Cyclic")
            break
        if next_index < 0 or next_index >= length:
            print("Out")
            break
        elif next_index == length - 1:
            print("Done")
            break
        og = next_index
    

