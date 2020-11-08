#!/usr/bin/env python
# coding: utf-8
"""
    dostęp do baz danych PostgreSQL z poziomu Pythona
    za pomocą modułu psycopg (zgodność z Python DB API Spec.)
    potrzebne: dowolny OS + Python + PsycoPg2
"""
import psycopg2
import easygui

#  wpisz parametry bazy danych z I semestru zajęć
polaczenie = psycopg2.connect(user='nazwa_twojego_konta', password='twoje_hasło', host='adres_serwera', database='nazwa_bazy', sslmode='prefer')

kursor = polaczenie.cursor()

pytanie = """
	select wojewodztwo as "województwo", 
	    count(distinct powiaty.klpow) as "liczba powiatów",
	    count(distinct klgm) as "liczba gmin"
	from gminy 
	    join powiaty on gminy.klpow = powiaty.klpow
	    join wojewodztwa on powiaty.klwoj = wojewodztwa.klwoj
	group by wojewodztwo 
	order by wojewodztwo;
"""

kursor.execute(pytanie)

# wyłuskać nazwy kolumn z odpowiedzi do listy naglowek
naglowek = []
for i in range(len(kursor.description)):
    naglowek.append( kursor.description[i][0] )

odpowiedz = kursor.fetchall()

kursor.close()
polaczenie.close()

if easygui.ynbox('Odpowiedź otrzymano. Czy pokazać wyniki?', 'Zapytanie do bazy'):
    tekst = naglowek[0] + '\t' + naglowek[1] + '\t' + naglowek[2] + '\n'
    for wpis in odpowiedz:
        tekst += wpis[0]+'\t'+str(wpis[1])+'\t'+str(wpis[2])+'\n'
    easygui.textbox('Treść zapytania:\n' + pytanie, 'Wyniki', tekst)
    del(tekst)

nazwapliku = easygui.filesavebox(None, 'Gdzie zapisać wyniki?', 'dane/*.txt')

if nazwapliku:
    plik = open(nazwapliku, 'w')
    plik.write('# ' + naglowek[0] + '\t' + naglowek[1] + '\t' + naglowek[2] + '\n')
    for wpis in odpowiedz:
        plik.write(wpis[0].encode('utf-8')+'\t'+str(wpis[1])+'\t'+str(wpis[2])+'\n')
    plik.close()

del(odpowiedz)