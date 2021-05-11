print("Numbers 1 to 10")
for i in range (1, 11):
    print(i, end=" ")

print()
print("Numbers 1 to 20, only even numbers")
for s in range (1, 21):
    if s % 2 == 0:
        print(s,end=" ")

print()
print("Numbers 1 to 20, only odd numbers")
for t in range (1, 21):
    if t % 2 != 0:
        print(t,end=" ")

print()
print("Numbers 1 to 50, every third numbers")
for p in range (1, 51)[::3]:
        print (p,end=" ")

print()
print("Numbers 1 to 40, in reverse every fourth numbers")
a = [*range(1, 41,)]
b = []
a.reverse()
for x in a:
    if (x%4) == 0:
        b.append(x)
for x in b:
    print(x,end=" ")

print()
print("Numbers 1 to 100, only prime numbers")
y = 1
while(y <= 100):
    count = 0
    o = 2
    while (o <= y // 2):
        if (y %o == 0):
            count = count + 1
            break
        o = o + 1

    if (count == 0 and y != 1):
        print("%d"% y,end=" ")
    y = y + 1

