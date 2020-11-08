# coding: utf-8

'''
    komunikacja z arkuszem Excel przez Component Object Model
    wymaga systemu operacyjnego z rodziny Windows

'''
import win32com.client
import easygui

def sumujWKolumnie(arkusz, kolumna):
    """ sumuje dane liczbowe z wskazanej kolumny arkusza """
    suma = 0.0
    wiersz = 1
    komorka = arkusz.Cells(wiersz, kolumna)
    while str(komorka.Value) != '':
        suma += float(arkusz.Cells(wiersz, kolumna).Value)
        wiersz += 1
        komorka = arkusz.Cells(wiersz, kolumna)
    arkusz.Cells(wiersz+1, kolumna).setValue(suma)
    return None

def podsumujPierwszeKolumny(skoroszyt):
    ''' podsumowuje pierwsze kolumny na wszystkich stronach skoroszytu '''
    for ark in range(skoroszyt.Worksheets.Count):
        sumujWKolumnie(skoroszyt.Worksheets(ark+1), 1)
    return None

# nazwapliku = 'c:\\documents and settings\\ktos\\dane\\tescik.xls'
nazwapliku = easygui.fileopenbox()
if nazwapliku == None:
    exit()
# Excel wymaga nazw z separatorami '\'
nazwapliku = nazwapliku.replace('/','\\')

sesja = win32com.client.Dispatch("Excel.Application")
sesja.Visible = 1	# jezeli chcemy ogladac co sie dzieje
skoroszyt = sesja.Workbooks.Open(nazwapliku)
podsumujPierwszeKolumny(skoroszyt)
skoroszyt.Save()
skoroszyt.Close()
sesja.Quit()