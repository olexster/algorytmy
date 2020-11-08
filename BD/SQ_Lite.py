#!/usr/bin/env python
# coding: utf-8
"""
    dostęp do baz danych SQLite z poziomu Pythona
    potrzebne: dowolny OS + Python
"""
import sqlite3
import easygui

#  wpisz nazwę pliku bazy danych
baza = 'admPL.db'

polaczenie = sqlite3.connect(baza)
kursor = polaczenie.cursor()

pytanie = """
	select powiat as "powiat", 
	    count(distinct gminy.klgm) as "liczba gmin",
	    count(1) as "liczba miejscowości"
	from miejscowosci
	    join gminy on miejscowosci.klgm = gminy.klgm
	    join powiaty on gminy.klpow = powiaty.klpow
	group by powiat
	order by powiat;
"""

kursor.execute(pytanie)

# wyłuskać nazwy kolumn z odpowiedzi do listy naglowek
naglowek = []
for i in range(len(kursor.description)):
	naglowek.append(kursor.description[i][0])

odpowiedz = kursor.fetchall()

kursor.close()
polaczenie.close()

if easygui.ynbox('Odpowiedź otrzymano. Czy pokazać wyniki?', 'Zapytanie do bazy'):
	tekst = naglowek[0] + '\t' + naglowek[1] + '\t' + naglowek[2] + '\n'
	for wpis in odpowiedz:
		tekst += wpis[0].encode('utf-8') + '\t' + str(wpis[1]) + '\t' + str(wpis[2]) + '\n'
	easygui.textbox('Treść zapytania:\n' + pytanie, 'Wyniki', tekst)
	del (tekst)

nazwapliku = easygui.filesavebox(None, 'Gdzie zapisać wyniki?', 'dane/*.txt')

if nazwapliku:
	plik = open(nazwapliku, 'w')
	plik.write('# ' + naglowek[0] + '\t' + naglowek[1] + '\t' + naglowek[2] + '\n')
	for wpis in odpowiedz:
		plik.write(wpis[0].encode('utf-8') + '\t' + str(wpis[1]) + '\t' + str(wpis[2]) + '\n')
	plik.close()

del (odpowiedz)
