l, r = map(int, input().split())
"""
1. even or odd 
2. points/number of tines 
even: tines is just the sum of l + r
odd: then the tines = 2*greater number 
3. if l and r = 0 0> not even a moss 
"""
if l == 0 and r == 0: 
    print("Not a moose")
elif l == r: #both of these are even numbers: 
    print(f"Even {l+r}")
else: 
    print(f"Odd {2*max(l,r)}")