s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
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

s2 = {'d': 4}
s | s2

s |= {'e': 5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}

lista = []
s = {}
counter = 0
while True:
    lst = input("wpisz cos albo enter")
    if (lst == ""):
        break
    counter = s.get(lst, 0)
    counter += 1
    s[lst] = counter

liczba = input("podaj liczbe od 1-999")
lenght = len(str(liczba))
digits = {1: 'jeden',
          2: 'dwa',
          3: 'trzy',
          4: ['cztery', 'czter'],
          5: ['piec', 'piet'],
          6: 'szesc',
          7: 'siedem',
          8: 'osiem',
          9: ['dziewiec', 'dziewiet'],
          10: 'dziesiec'}

if lenght == 2:
    if (liczba[0] != 4 or liczba[0] != 9):
        print(f"{digits[int(liczba[1])]}nascie")
    else:
        print(f"{digits[int(liczba[1][1])]}nascie")

# -------------------------------------------------------------------------
nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",

                  9: "dziewięć"}

dziesiatki = {10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",

              60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}

nastki = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie",

          16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie"}

setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta", 400: "czterysta", 500: "piecset", 600: "szescset",
         700: " siedemset", 800: "osiemset", 900: "dziewiecset"}

slownik = {}

n = int(input("Wpisz liczbe:"))
napis = setki[n - n % 100]
n %= 100

if n in range(11, 20):
    napis = nastki[n]
else:
    napis += setki[n] + " " + dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]

print(napis)

# ********************************************************************************************
nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",

                  9: "dziewięć"}

nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "pietnascie",
          16: "szesnaście",

          17: "siedemnascie", 18: "osiemnaście", 19: "dziewietnascie"}

dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",

              40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt",

              90: "dziewięćdziesiąt"}

setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",

         400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",

         800: "osiemset", 900: "dziewiecset"}

n = int(input("wpisz liczbe:"))

napis = setki[n - n % 100]

n %= 100

if n in range(11, 20):

    napis += nastki[n]

else:

    napis += " " + dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]

print(napis)
