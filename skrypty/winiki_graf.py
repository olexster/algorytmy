#!/usr/bin/env python
# coding: utf-8
""" demonstracja przygotowania danych do zrobienia wykresu
    za pomocą programu Gnuplot wywołanego poleceniem systemu operacyjnego
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


def piszskrypt(skrypt, dane, wykres, komentarz):
	""" tworzy plik skryptowy z poleceniami dla Gnuplota
	"""
	plik = open(skrypt, 'w')
	rysuj = 'plot "' + dane + '" using 1:2 with lp title "' + komentarz[1] + '"' \
																			 ', "' + \
			dane + '" using 1:3 with lp title "' + komentarz[2] + '"'
	plik.write(rysuj + '\n')
	plik.write('pause -1\n')
	plik.write('set terminal svg\nset output "' + wykres + '"\nreplot\n')
	plik.close()


# tworzymy dane
dane = generuj(20)
naglowek = ['X', 'pierwiastek z X', 'logarytm X']

# zapisujemy je do pliku
nazwadane = 'wyniki.txt'
dopliku(nazwadane, dane, naglowek)

# tworzymy skrypt z poleceniami dla Gnuplota
nazwaskrypt = 'wykres.gp'
nazwawykres = 'wykres.svg'
piszskrypt(nazwaskrypt, nazwadane, nazwawykres, naglowek)

# na koniec uruchamiamy Gnuplota i każemy mu wykonać przygotowany skrypt
gnuplot = '/usr/bin/gnuplot'
os.spawnv(os.P_NOWAIT, gnuplot, ['gnuplot', nazwaskrypt])

# i to jest koniec