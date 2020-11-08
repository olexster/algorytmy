
# coding: utf-8
def bmi(imie,wzrost,masa):
    indexBMI = masa/wzrost
    imie = imie.capitalize()
    if imie[-1] == 'a':
        if imie == 'Kuba':
            plec = 'Pan'
        else:
            plec = 'Pani'
    else:
        plec = 'Pan'
    if indexBMI < 16:
        waga = 'wygłodzenie'
    elif indexBMI < 17:
        waga = 'wychudzenie'
    elif indexBMI < 18.5:
        waga = 'niedowagę'
    elif indexBMI < 25:
        waga = 'wagę prawidłową'
    elif indexBMI < 30:
        waga = 'nadwagę'
    elif indexBMI < 35:
        waga = 'I stopień otyłości'
    elif indexBMI < 40:
        waga = 'II stopień otyłości (otyłość kliniczna)'
    else:
        waga = 'III stopień otyłości (otyłość skrajna)'
    print(plec+' '+ imie+' ma ' + waga)
    print(str(imie) +' '+ str(wzrost) +' '+ str(masa)+'\n')
bmi('kuba',1,25)
bmi('julia',1,24.9)
bmi('Jan',10,184)
