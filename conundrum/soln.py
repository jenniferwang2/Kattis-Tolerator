n = input()
split = []
for i in range(0,len(n),3):
    split.append(n[i : i + 3])
days = 0
for i in split:
    if i[0] != "P":
        days += 1
    if i[1] != "E":
        days += 1
    if i[2] != "R":
        days += 1
print(days)