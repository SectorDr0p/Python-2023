lista = list(range(10, 0, -1))
lista
lista.sort()
lista
lista.sort(reverse=True)
lista
lista = [ str(i) for i in range(21)]
lista
lista.sort()
str(lista)
lista.sort(key=int)
str(lista)

dluga_lista = [ str(i) for i in range(21)] + [ str(i) for i in range(-1, -21, -1)]
str(dluga_lista)
dluga_lista.sort(key=int)


lista = []

while True:
    lst = input("wpisz cos albo enter")
    if (lst == ""):
        break
    lista.append(lst)

lista.sort(key=str)

print(lista)