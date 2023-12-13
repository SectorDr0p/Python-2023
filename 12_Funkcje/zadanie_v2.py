def _slownie999(n, jednostki=['metr', 'metry', 'metrów']):
    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",

                      8: "osiem", 9: "dziewięć"}
    nazwy_nastki = {11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście",

                    16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście", 19: "dziewietnaście"}
    nazwy_dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści", 40: "czterdzieści",

                        50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt",

                        80: "osiemdziesiąt", 90: "dziewięćdziesiąt"}
    nazwy_setki = {0: "", 100: "sto", 200: "dwieście", 300: "trzysta", 400: "czterysta", 500: "pięćset",

                   600: "sześćset", 700: "siedemset", 800: "osiemset", 900: "dziewięćset"}

    ret = []
    jednosci = n % 10
    dziesiatki = n % 100 - jednosci
    setki = n - dziesiatki - jednosci

    if setki:
        ret.append((setki, nazwy_setki[setki]))

    if dziesiatki == 10 and jednosci > 0:
        nastki = 10 + jednosci
        ret.append((nastki, nazwy_nastki[nastki]))

    else:
        if dziesiatki:
            ret.append((dziesiatki, nazwy_dziesiatki[dziesiatki]))
        if jednosci:
            ret.append((jednosci, nazwy_jednosci[jednosci]))

    if ret[-1][0] in [2, 3, 4]:
        ret.append((ret[-1][0], jednostki[1]))

    elif len(ret) == 1 and ret[-1][0] == 1:
        ret = [(ret[-1][0], jednostki[0])]

    else:
        ret.append((ret[-1][0], jednostki[2]))

    return ret

def _sklej(lista):
    return [t[1] for t in lista]

def slownie(n):
    jednosci = n % 1000
    tysiace = n // 1000 % 1000
    miliony = n // 1_000_000 % 1000
    miliardy = n // 1_000_000_000 % 1000

    ret = []
    if miliardy:
        ret += (_slownie999(miliardy, jednostki=['miliard', 'miliardy', 'miliardow', ]))
    if miliony:
        ret += (_slownie999(miliony, jednostki=['milion', 'miliony', 'milionow', ]))
    if tysiace:
        ret += (_slownie999(tysiace, jednostki = ['tysiac', 'tysiace', 'tysiecy', ]))
    if jednosci:
        ret += (_slownie999(jednosci, jednostki=['', '', '', ]))

    return " ".join(_sklej(ret)).strip()

for i in [1,2,3,4,5,6]:
    print(i)
for k in [(1,1) , (2,2) , (3,3) , (4,4) , (5,5), (6,6)]:
    print(k)

#assert _slownie999(313) == [(300, 'trzysta'), (13, 'trzynaście')]
print(_slownie999(543))
print(slownie(654_789_322))

