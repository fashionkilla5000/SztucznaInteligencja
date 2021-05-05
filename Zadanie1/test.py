import pandas as pd
from numpy import nan
import collections
import json, codecs
import subprocess
import time

def main():

    print("""\n\nWybierz plik do wczytania:
        1.australian
        2.breast-cancer-wisconsin
        3.crx""")
    response = int(input())
    if response == 1:
        df = pd.read_csv('australian.dat', header=None, na_values = '?', delim_whitespace=True)
        print('\nWyświetlam plik:')
        print(df)
    elif response == 2:
        df = pd.read_csv('breast-cancer-wisconsin.data', header=None, na_values = '?')
        print('\nWyświetlam plik:')
        print(df)
    elif response == 3:
        df = pd.read_csv('crx.data', header=None, na_values = '?')
        print('\nWyświetlam plik:')
        print(df)
    else:
        print("\n\n Coś poszło nie tak, spróbuj jeszcze raz")
        main()

    def toFloat(name):
        for i in range(len(name)):
            for j in range(len(name[i])):
                try:
                    float(name[i][j])
                    name[i][j] = float(name[i][j])
                except ValueError:
                    continue


    def normalize(array,nmin,nmax):
        new = []
        for x in array:
            new.append(((x - min(array)) / (max(array) - min(array)))*((nmax-nmin)+nmin))
        return new

    def config(array):
        j=-1
        print("\n\nSzukam liter w pierwszym wierszu")
        for i in array[0]:
            j= j+1
            if type(i) == str:
                print('\nWykryto znak: ' + i + ' w kolumnie: ', j)
                print('\nwczytuje kolumne:')
                print(df[j])
                print("""\n\nZdecyduj co chcesz zrobić z kolumną z tym znakiem:
                                1.Usun
                                2.Zamień na liczby
                                3.Nic""")
                response = int(input())
                if response == 1:
                    del df[j]
                    print('\nDane po zmianach: ')
                    print(df)
                elif response == 2:
                    arr = df[j].to_numpy()
                    list = collections.Counter(arr)
                    print(list)
                    del list[nan]
                    viter = iter(list)
                    x = len(list.values())
                    for k in viter:
                        df[j] = df[j].replace([k], x)
                        x= x-1
                    print('\nDane po zmianach: ')
                    print(df)
                elif response == 3:
                    print('\nDane po zmianach: ')
                    print(df)
                    continue
                else:
                    print("\nCoś poszło nie tak, spróbuj jeszcze raz")
                    config(nf)

        input("\n\nPress Enter to continue...")
    def menu_normalizuj():
        print("""\n\nCzy chcesz znormalizować wybrane kolumny?:
                                        1.Tak
                                        2.Nie
                                        3.Normalizuj calosc """)
        response = int(input())
        if response == 1:
            n = int(input('podaj liczbe kolumn do normalizacji: '))
            print("\nPodaj przedział do normalizacji: ")
            nmin = int(input())
            nmax = int(input())
            print("\nPodaj kolejno kolumny do normalizacji: ")
            i = 0
            while i < n:
                try:
                    x = int(input())
                    df[x] = normalize(df[x],nmin,nmax)
                    i=i+1
                except:
                    print('\nCoś poszło nie tak, wybierz prawidłową kolumnę')
            print('\nDane po zmianach: ')
            print(df)

        elif response == 2:
            pass
        elif response == 3:
            print("\nPodaj przedział do normalizacji: ")
            nmin = int(input())
            nmax = int(input())
            try:
                for x in range(len(df.columns)):
                    df[x] = normalize(df[x], nmin, nmax)
                print(df)
            except:
                print('\nCoś poszło nie tak, spróbuj jeszcze raz')
                menu_normalizuj()

    def menu_zapisz():
        print("""\n\nCo dalej?:
            1.zapisz do Json
            2.zapisz do Excel
            3.zapisz do Html
            4.zacznij od nowa
            5.zakończ""")
        response = int(input())
        if response == 1:
            Fson = df.to_numpy().tolist()
            json.dump(Fson, codecs.open('name.json', "w"), separators=(',', ':'), sort_keys=True, indent=4)
            #df.to_json('name.json')
            print("\nPlik zapisany pomyślnie!\n\n")
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "/t", 'file:///C:/Users/User/Desktop/SztucznaInteligencja/SztucznaInteligencja/Zadanie1/name.json'])
            input("\n\nPress Enter to continue...")
            menu_zapisz()
        elif response == 2:
            df.to_excel('name.xlsx')
            print("\nPlik zapisany pomyślnie!")
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\Root\\Office16\\EXCEL.EXE", "/t", 'name.xlsx'])
            input("\n\nPress Enter to continue...")
            menu_zapisz()
        elif response == 3:
            df.to_html(r'name.html')
            print("\nPlik zapisany pomyślnie!")
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "/t", 'file:///C:/Users/User/Desktop/SztucznaInteligencja/SztucznaInteligencja/Zadanie1/name.html'])
            input("\n\nPress Enter to continue...")
            menu_zapisz()
        elif response == 4:
            main()
        elif response == 5:
            exit()


    nf = df.to_numpy()
    toFloat(nf)
    config(nf)
    menu_normalizuj()
    menu_zapisz()
main()