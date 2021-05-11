import json
from school import *

min = 1000
max = -1000
avg = 0
count = 0
total= 0
list = []
number = 0

with open('students.json') as json_file:
    root = json.load(json_file) #ROOT REPERSENT JSON FILE

    for row in root:
        id = row['id']
        name = row['name']
        age = int(row['age'])
        attendance = row['attendance']
        student = Student(id, name, age, attendance)

        if age < min:
            min = age
            youngest = name


        if age > max:
            max = age
            oldest = name


        if attendance < 30:
            list.append(name)


        count += 1
        total += age
    avg = total/count



    print("Youngest:", youngest)
    print("Oldest:" ,oldest)
    print("Average age:" ,round(avg-0.5))

    for attendant in list:
        number += 1
        print("Bad student:", list[number - 1])








