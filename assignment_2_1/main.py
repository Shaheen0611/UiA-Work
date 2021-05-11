
count = 0
num = []
sum = 0
avg = 0
sort = []
result = []
med = 0
j = 0


while num != 0:

    j = int(input())#FUNCTION TO CALCULATE AVERAGE
    if j == 0:
        break
    num = j
    sort.append(num)
    sum += num
    count += 1
    avg = sum / count

for x in range(len(sort)): #FUNCTION TO SORT NUMBERS IN DECENDING ORDER
    y = max(sort)
    sort.remove(y)
    result.append(y)
z = ' '.join(str(num) for num in result)


print("Average :",avg)

c = int(count) #FUNCTION TO FIND OUT THE MEDIAN
m = 0
if (c % 2) == 0:
    n = int(c/2)
    m = (result[n-1] + result[n])/2
    print("Median :" ,round(m,2))
if (c % 2) == 1:
    n = (c/2) + 0.5
    t = int(n)
    m = result[t - 1]
    print("Median :" ,round(m,2))



print("Descending :",z)
















