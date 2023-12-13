[(x,str(x)) for x in range(10)]


t = []
for i in range(10):
    t.append([i , str(i)])
print(t)








s = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

[(car, weight) for car, weight in s.items() if weight > 5000]

[x for x in s.keys() if s[x] > 5000]