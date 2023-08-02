n = int(input())
  
def years(p, r, f):
    if p > f: 
        return 0
    else:
        years = 1
        while True:  
            if p * r > f: #if next year is unsustainable
                break
            else: #otherwise another sustainable year
                p = p * r
                years += 1
        return years

for i in range(n):
    population, growth_rate, food = map(int, input().split())
    print(years(population, growth_rate, food))
  