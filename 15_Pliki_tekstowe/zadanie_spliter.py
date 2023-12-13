import os

print(os.getcwd())
first_line = None
data = []
with open('C:\\Users\\localadmin\\PycharmProjects\\Python-2023\\15_Pliki_tekstowe\\data\\jamesbond.csv') as f:
    for l in f:
        if first_line is None:
            first_line = l.strip().split(',')
        else:
            dane = l.strip().split(',')
            slownik = dict(zip(first_line, dane))
            print(slownik)
