a = 4

# IF
if a == 3:
    print("Then shalt thou count to three, no more, no less.")
    print("Three shall be the number thou shalt count, and the number of the counting shall be three.")
    print("Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. ")
else:
    print('Not three')

if a == 3:
   print("three")
else:
   if a == 4:
       print("four")
   else:
       print('Not three or four')


n = int(input('Podaj liczbę'))
print(n)

# ELSE
if n == 1:
    print('Jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

# Warunki logiczne

if (n == 17) or not (n == 17):
    print("Tertium non datur")
    print("Innej opcji nie ma")
n = 5
if n == 17 or n != 17:
    print("Tertium non datur")
    print("Innej opcji nie ma")

# := "Walrus" operator
if (i := int(input("podaj liczbę naturalną"))) % 2 == 0:
    print(f'{i} jest parzyste')
else:
    print(f'{i} jest nieparzyste')














a = int(input("podaj liczbe"))
b = int(a/10) # b = a // 10
c = a%10
i = b+c
if(i % 7 == 0 and a % 2 == 0):
    print("liczba jest dobra")
else:
    print("liczba jest zla")