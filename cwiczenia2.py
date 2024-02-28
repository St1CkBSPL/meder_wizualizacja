import sys

#Zad 1
zdanie = input("Wpisz wyraz: ")
slowa = zdanie.split()
ilosc = len(slowa)
print(f'Ilość słów w zdaniu --> {ilosc}')

#Zad 2
sys.stdout.write('Wprowadz 3 liczby: ')
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
wynik = a**b+c
print(f'Wynikiem działania {a}**{b}+{c} jest: {wynik}')

#Zad 3
l = input("Wpisz wyraz: ")
if l == l[::-1]:
    print("Jest palindromem ")
else:
    print("Nie jest palindromem ")

#Zad3 drugi sposob
def Palindrom(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s = "kajak"
ans = Palindrom(s)

if (ans):
    print("Tak, jest palindromem")
else:
    print("Nie, nie jest palindromem")

#Zad 4
n = int(input("Wpisz liczbę naturalną: "))
for x in range(2, n):
    if n % x == 0:
        print(n, 'equals', x, '*', n//x)
        break
    else:
        print(n, 'jest liczbą pierwszą')

#Zad 5
def czy_liczba_doskonala(liczba):
    suma_dzielnikow = sum([dzielnik for dzielnik in range(1, liczba) if liczba % dzielnik == 0])
    return suma_dzielnikow == liczba

def liczby_doskonale_do(limit):
    doskonale = [liczba for liczba in range(2, limit) if czy_liczba_doskonala(liczba)]
    return doskonale

limit = 1000
doskonale_do_1000 = liczby_doskonale_do(limit)

print(f"Liczby doskonałe do {limit}:")
print(doskonale_do_1000)

#Zad 6
lista4 = [2,4,3.5,8.5]
lista5 = [liczba4**2 for liczba4 in lista4]

print(lista4)
print(lista5)


#Zad 7
lista10 = []
while len(lista10) < 10:
    liczba = int(input("Wpisz liczbę naturalną: "))
    if liczba % 2 == 0:
        lista10.append(liczba)
print(lista10)

#Zad 8
def utworz_slownik_z_liczba_wystapien(elementy_listy):
    slownik_wystapien = {}
    for element in elementy_listy:
        slownik_wystapien[element] = slownik_wystapien.get(element, 0) + 1
    return slownik_wystapien

def usun_nie_liczbowe_elementy(slownik_wystapien):
    slownik_liczbowych_elementow = {klucz: wartosc for klucz, wartosc in slownik_wystapien.items() if isinstance(klucz, (int, float))}
    return slownik_liczbowych_elementow

przykladowa_lista = [1, 'jabłko', 2, 'pomarańcza', 1, 3, 'jabłko', 'banan', 2, 3, 4, 'banan']
slownik_wystapien = utworz_slownik_z_liczba_wystapien(przykladowa_lista)
print("Słownik przed filtrowaniem:", slownik_wystapien)
slownik_liczbowych_elementow = usun_nie_liczbowe_elementy(slownik_wystapien)
print("Słownik po filtrowaniu:", slownik_liczbowych_elementow)







