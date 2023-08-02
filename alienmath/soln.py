#base
base = int(input()) 

#store digits
digits = []
for i in input().split():
    digits.append(i)

#sep number by digits
number = input()
sep_num = []
while number:
    for digit in digits: 
        if number.startswith(digit):
            sep_num.append(digit)
            number = number.replace(digit, "", 1)

#find value
value = 0
power = len(sep_num) - 1 #i * base^(3-1), ...2-1, 0-1
for _ in sep_num: 
    value += digits.index(_) * base ** power
    power -= 1
print(value)