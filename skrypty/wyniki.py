#!/usr/bin/python
# coding: utf-8
"""
    prezentacja danych wynikowych za pomocą zewnętrznego programu
"""
import math
import os


def generuj(n):
	""" przygotowuje tablicę kolejnych liczb całkowitych od 0 do n,
	ich pierwiastków oraz ich logarytmów
	"""
	dane = []
	for i in range(n + 1):
		if (i > 0):
			y2 = math.log(i)
		else:
			y2 = None
		dane.append([i, math.sqrt(i), y2])
	return dane


def dopliku(nazwa, dane, komentarz):
	""" zapisuje dane do pliku tekstowego
	"""
	plik = open(nazwa, 'w')
	plik.write('# ' + komentarz[0] + '\t' + komentarz[1] + '\t' + komentarz[2] + '\n')
	for rekord in dane:
		plik.write(str(rekord[0]) + '\t' + str(rekord[1]) + '\t' + str(rekord[2]) + '\n')
	plik.close()


# tworzymy dane
dane = generuj(20)
naglowek = ['X', 'Sqrt(X)', 'Ln(X)']

# zapisujemy je do pliku
nazwadane = 'wyniki.txt'
dopliku(nazwadane, dane, naglowek)

# na koniec uruchamiamy SciTE i każemy mu wczytać plik wynikowy
edytor = 'c:/Program Files/Notepad++/notepad++.exe'
os.spawnv(os.P_NOWAIT, edytor, [edytor, nazwadane])

# i to jest koniec