n = int(input())
scores = map(int, input().split())
sum = 0
for score in scores:
    if score == -1:
        n -= 1
    else: 
        sum += score
print(sum/n)
