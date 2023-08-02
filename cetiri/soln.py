
# a, b, c = sorted(map(int, input().split())) 
# s, l = min(c- b, b - a), max(c-b, b-a)
# if s == l:
#     print(c+s)
# elif l == b - a: 
#     print(a+s)
# else:
#     print(b+s)

# a,b,c=sorted(map(int,input().split()))
# s,l=min(c-b,b-a),max(c-b,b-a)
# print((a if l==b-a else b)+s if s!=l else c+s)

a,b,c=sorted(map(int,input().split()));d,e=sorted([c-b,b-a]);print((b if d==e else a)+d)
