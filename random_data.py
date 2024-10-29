import random
x = int(input())
print("ID    date     Time  ")
for i in  range(x):
    id = i
    if id < 10:
        id = "0" + str(id)
    year = random.randint(0,24)
    if year < 10:
        year = "20" + "0" + str(year)
    else:
        year = "20" + str(year)
    month = random.randint(1,12)
    if month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
    elif month in [4,6,9,11]:
        day = random.randint(1,30)
    else:
        day = random.randint(1,28)
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    hour = random.randint(0,23)
    if hour < 10:
        hour = "0" + str(hour)
    min = random.randint(0,59)
    if min < 10:
        min = "0" + str(min)
    print(str(id) + " " + str(year) + ":" + str(month) + ":" + str(day) + "   " + str(hour) + ":" + str(min))