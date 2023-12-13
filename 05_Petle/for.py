for i in range(12):
    print(i)

for i in range(3, 12):
    print(i)

for i in range(3, 12, 2):
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

for number in range(10, 100):
    suma = 0
    for c in str(number):
        suma += int(c)
    if (suma % 7 == 0 and number % 2 == 0):
        print(number)




number = input()
suma = 0
for c in str(number):
    print(f"to jest znak-> {c} \nto jest suma-> {suma}")
    suma += int(c)    # suma = suma + c
print(suma)
