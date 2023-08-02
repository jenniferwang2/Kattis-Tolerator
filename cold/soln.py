n = input()
temps = input().split()
days = 0
for i in range(int(n)):
    if int(temps[i]) < 0:
        days +=1
print(days)