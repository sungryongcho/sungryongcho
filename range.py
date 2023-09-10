print(list(range(20, 30)))

print()

a = list(range(40, 80))
b = []
for num in a :
    if(num % 7==0) :
        b.append(num)

print(b)