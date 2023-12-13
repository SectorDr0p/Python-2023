def suma(x=5):
    print(x + x)


def power(x=5):
    print(x * x)


s = {'f1': suma, 'f2': power}

inp = input("Podaj klucz: f1 lub f2")
print(s[inp])

f = s[inp]
f()


# ----------------------------------------


def alphabet(start='a', stop='z', step=1):
    return [chr(x) for x in range(ord(start), ord(stop), step)]


alphabet_letters = alphabet()
print(alphabet_letters)


# --------------------------------------

def suma(*args):
    sum = 0
    for d in args:
        sum += d
    return sum


su = suma(1, 2, 3, 4, 5, 6)
print(su)


# -----------------------------------------

def slownie_do999(liczba=999):
    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
                      8: "osiem",

                      9: "dziewięć"}

    nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "pietnascie",
              16: "szesnaście",

              17: "siedemnascie", 18: "osiemnaście", 19: "dziewietnascie"}

    dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",

                  40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt",
                  80: "osiemdziesiąt",

                  90: "dziewięćdziesiąt"}

    setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",

             400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",

             800: "osiemset", 900: "dziewiecset"}

    number = int(input("wpisz liczbe:"))
    output = setki[number - number % 100]
    number %= 100

    if number in range(11, 20):
        output += nastki[number]
    else:
        output += " " + dziesiatki[number - number % 10] + " " + nazwy_jednosci[number % 10]

    print(output)


def _slownie_do999():
    nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem",
                      8: "osiem",

                      9: "dziewięć"}

    nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "pietnascie",
              16: "szesnaście",

              17: "siedemnascie", 18: "osiemnaście", 19: "dziewietnascie"}

    dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",

                  40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt",
                  80: "osiemdziesiąt",

                  90: "dziewięćdziesiąt"}

    setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",

             400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",

             800: "osiemset", 900: "dziewiecset"}

    krotka = []

    number = int(input("wpisz liczbe:"))
    output = setki[number - number % 100]
    # print(number - number % 100, output)
    krotka.append((number - number % 100, output))
    number %= 100

    if number in range(11, 20):
        output += nastki[number]
        krotka.append((10, 'dziesiec'))
    else:
        output += " " + dziesiatki[number - number % 10] + " " + nazwy_jednosci[number % 10]
        krotka.append((number, dziesiatki[number % 10]))
        krotka.append((number % 10, nazwy_jednosci[number % 10]))
        print(output)
        print(krotka)

    print(output)


slownie_do999()


# -------------------------------------------------------------------
def _slownie999(n):
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

        return ret
