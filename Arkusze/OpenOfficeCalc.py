# coding: utf-8

'''
    komunikacja z arkuszem OpenOffice Calc za pośrednictwem interfejsu UNO
    do uruchomienia w dowolnym systmie operacyjnym

    wymaga interpretera Pythona współpracującego z OpenOffice
    przed uruchomieniem skryptu trzeba uruchomić serwer danych OpenOffice
'''

import uno

def sumujWKolumnie(arkusz, kolumna):
    """ sumuje dane liczbowe z wskazanej kolumny arkusza """
    suma = 0.0
    wiersz = 0
    komorka = arkusz.getCellByPosition(kolumna, wiersz)
    while komorka.getString() != '':
        suma += arkusz.getCellByPosition(kolumna, wiersz).getValue()
        wiersz += 1
        komorka = arkusz.getCellByPosition(kolumna, wiersz)
    arkusz.getCellByPosition(kolumna, wiersz+1).setValue(suma)
    return None

def podsumujPierwszeKolumny(skoroszyt):
    ''' podsumowuje pierwsze kolumny na wszystkich stronach skoroszytu '''
    for ark in range(skoroszyt.Sheets.Count):
        sumujWKolumnie(skoroszyt.Sheets.getByIndex(ark), 0)
    return None

# tego fragmentu proszę nie analizować...
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
# host i port muszą wskazywać na adres uruchomionego serwera danych
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
biurko = ctx.ServiceManager.createInstanceWithContext( "com.sun.star.frame.Desktop", ctx)

FILEOPEN_SIMPLE = 0
FILESAVE_SIMPLE = 1

def OOoFileOpenDialog(ctx, fname, title):
        ' definiuje okno dialogowe wyboru pliku via OOo '
        picker = ctx.ServiceManager.createInstanceWithContext("com.sun.star.ui.dialogs.FilePicker", ctx)
        picker.initialize( (FILEOPEN_SIMPLE, ) )
        picker.setDisplayDirectory("file:///" + fname)
        picker.setTitle(title)
        if picker.execute():
            fname = picker.getFiles()[0]
        else:
            fname = None
        picker.dispose()
        return fname

# nazwapliku = 'file:///home/ktos/documents/tescik.ods'
nazwapliku = OOoFileOpenDialog(ctx, '', u'Otwórz plik')

# obiekt biurko reprezentuje serwer OpenOffice
skoroszyt = biurko.loadComponentFromURL(nazwapliku, '_blank', 0, ()) # otwiera istniejacy dokument
podsumujPierwszeKolumny(skoroszyt)
skoroszyt.store()
skoroszyt.close(True)