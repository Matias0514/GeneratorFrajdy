import random

class Pesel:
    def __init__(self,imie,nazwisko,data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
    def utworz_pesel(self,imie,nazwisko,data_urodzenia):
        #pobieranie znaków z daty urodzenia
        znak1 = self.data_urodzenia[0]
        znak2 = self.data_urodzenia[1]
        znak3 = self.data_urodzenia[2]
        znak4 = self.data_urodzenia[3]
        znak5 = self.data_urodzenia[5]
        znak6 = self.data_urodzenia[6]
        znak7 = self.data_urodzenia[8]
        znak8 = self.data_urodzenia[9]
        liczba1 = int(znak3)
        liczba2 = int(znak4)
        liczba3 = int(znak5)
        liczba4 = int(znak6)
        liczba5 = int(znak7)
        liczba6 = int(znak8)
        #rocznik ZNAK 1 I 2
        cyfra12 = znak3 + znak4
        
        #tworzenie roku
        rok = znak1 + znak2 + znak3 + znak4;
        rok = int(rok)
        
        #określanie miesiąca ZNAK 3 I 4
        if rok>1999:
            mies = znak5 + znak6
            mies = int(mies)
            mies = mies + 20 
            cyfra34 = str(mies)
        else:
            cyfra34 = znak5 + znak6
        
        #tworzenie dnia 5 I 6
        cyfra56 = znak7 + znak8

        #Ustalanie losowych liczb 7,8,9
        pula = [0,1,2,3,4,5,6,7,8,9]
        liczba7 = random.choice(pula)
        liczba8 = random.choice(pula)
        liczba9 = random.choice(pula)
        cyfra7 = str(liczba7)
        cyfra8 = str(liczba8)
        cyfra9 = str(liczba9)
        
        #ustalanie płci ZNAK 10 
        litera = self.imie[-1]
        
        if litera=='a':
            kobieta = [0,2,4,6,8]
            liczba10 = random.choice(kobieta)
        else:
            mezczyzna = [1,3,5,7,9]
            liczba10 = random.choice(mezczyzna)

        cyfra10 = str(liczba10)

        #ustalenie liczby kontrolnej
        ck1 = liczba1*1
        ck2 = liczba2*3
        ck3 = liczba3*7
        ck4 = liczba4*9
        ck5 = liczba5*1
        ck6 = liczba6*3
        ck7 = liczba7*7
        ck8 = liczba8*9
        ck9 = liczba9*1
        ck10 = liczba10*3
        if (ck1>9):
            ck1 = str(ck1)
            ck1 = ck1[-1]
            ck1 = int(ck1)
        else:
            ck1 = ck1

        if (ck2>9):
            ck2 = str(ck2)
            ck2 = ck2[-1]
            ck2 = int(ck2)
        else:
            ck2 = ck2

        if (ck3>9):
            ck3 = str(ck3)
            ck3 = ck3[-1]
            ck3 = int(ck3)
        else:
            ck3 = ck3

        if (ck4>9):
            ck4 = str(ck4)
            ck4 = ck4[-1]
            ck4 = int(ck4)
        else:
            ck4 = ck4

        if (ck5>9):
            ck5 = str(ck5)
            ck5 = ck5[-1]
            ck5 = int(ck5)
        else:
            ck5 = ck5

        if (ck6>9):
            ck6 = str(ck6)
            ck6 = ck6[-1]
            ck6 = int(ck6)
        else:
            ck6 = ck6

        if (ck7>9):
            ck7 = str(ck7)
            ck7 = ck7[-1]
            ck7 = int(ck7)
        else:
            ck7 = ck7

        if (ck8>9):
            ck8 = str(ck8)
            ck8 = ck8[-1]
            ck8 = int(ck8)
        else:
            ck8 = ck8

        if (ck9>9):
            ck9 = str(ck9)
            ck9 = ck9[-1]
            ck9 = int(ck9)
        else:
            ck9 = ck9

        if (ck10>9):
            ck10 = str(ck10)
            ck10 = ck10[-1]
            ck10 = int(ck10)
        else:
            ck10 = ck10
            
        liczbakontrolna = ck1+ck2+ck3+ck4+ck5+ck6+ck7+ck8+ck9+ck10
        liczbakontrolna = str(liczbakontrolna)
        liczbakontrolna = liczbakontrolna[-1]
        liczbakontrolna = int(liczbakontrolna)
        liczba11 = 10 - liczbakontrolna
        cyfra11 = str(liczba11)

        pesel = cyfra12 + cyfra34 + cyfra56 + cyfra7 + cyfra8 + cyfra9 + cyfra10 + cyfra11
        print("Pesel to " + pesel)

osoba1 = Pesel('Mieczysław','Wątochuj','1998-12-24')
osoba1.utworz_pesel(osoba1.imie,osoba1.nazwisko,osoba1.data_urodzenia)

#NOELO