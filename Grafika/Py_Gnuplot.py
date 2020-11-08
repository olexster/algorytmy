#!/usr/bin/env python
# coding: utf-8
""" tworzenie wykresu przy użyciu programu graficznego Gnuplot
    za pośrednictwem pakietu Gnuplot-py
"""
import PyGnuplot

def f1(x):
        return 1.0/(x**2+1)

def f2(x):
        return abs(x+0.5)**1.5

seria1 = []
seria2 = []
n = 10
for i in range(-n, n+1):
        t = 0.1*i
        seria1.append([t, f1(t)])
        seria2.append([t, f2(t)])

sesja = PyGnuplot.Gnuplot()

## dwa następne polecenia dają większą władzę nad seriami danych,
## pozwalając ustalić ich nazwy oraz styl inny, niż domyślny
seria1 = PyGnuplot.Data(seria1, with_='lines', title='funkcja 1')
seria2 = PyGnuplot.Data(seria2, with_='linespoints', title='funkcja 2')

sesja('set style data linespoints')
sesja.plot(seria1)
sesja.replot(seria2)

sesja.title('Wykresik')
sesja.xlabel('Iksiki')
sesja.ylabel('Ygreczki')

# po czym albo
sesja.hardcopy('wykresGp.svg', 'svg')
# albo
'''
sesja('set terminal svg')
sesja('set output "wykresGp.svg"')
sesja.replot()
'''
sesja.close()