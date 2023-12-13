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
