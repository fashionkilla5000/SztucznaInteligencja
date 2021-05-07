import pandas as pd
from numpy import nan
import numpy as np
import collections
import json, codecs
import subprocess

def main():

    def toFloat(name):
        for i in range(len(name)-1):
            for j in range(len(name[i])):
                try:
                    float(name[i][j])
                    name[i][j] = float(name[i][j])
                except ValueError:
                    continue

    def config(array):
        j=-1
        print("\nZnalazłem litery w pierwszym wierszu")
        for i in array[0]:
            j= j+1
            if type(i) == str and j<len(array[0])-1:
                print('\nWykryto znak: ' + i + ' w kolumnie: ', j)
                print('\nwczytuje kolumne:')
                print(df[j])
                print("""\n\nZdecyduj co chcesz zrobić z kolumną z tym znakiem:
                                1.Usun
                                2.Zamień na liczby
                                3.Nic""")
                response = int(input())
                if response == 1:
                    df.drop(j, axis=1, inplace=True)
                    print('\nDane po zmianach: ')
                    print(df)
                elif response == 2:
                    arr = df[j].to_numpy()
                    list = collections.Counter(arr)
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
                    config(df.to_numpy())
        input("\n\nPress Enter to continue...")

    def struktura():

        f = open("data.txt", "w")
        f.seek(0)
        f.truncate()
        f.close()

        list = [int(item) for item in input("Podaj strukturę (w formacie: 3-2-1) : ").split('-')]
        s = []
        while len(list) > 1:
            i = 0
            col = list[i] + 1
            row = list[i + 1]
            s.append(col-1)
            if len(list) == 2:
                s.append(row)
            tem = np.random.random((row, col))
            file_object = open('data.txt', 'a')
            file_object.write(np.array2string(tem))
            file_object.write("\n\n")
            del list[i]
            i = i + 1

        file_object = open('data.txt', 'a')
        file_object.write("\nstruktura: ")
        file_object.write('-'.join([str(elem) for elem in s]))
        file_object.write("\n\n")
        print("\nwczytaj strukturę w polu wyboru: ")

    def wczytaj_strukture():
        print("\n\n")
        f = open("data.txt", "r")
        print(f.read())
        f.close()
        main()

    print("""\nWybierz jendą z opcji:
        1.Wczytaj australian
        2.Wczytaj breast-cancer-wisconsin
        3.Wczytaj crx
        4.Stworz strukture
        5.Wczytaj strukture""")
    response = int(input())
    if response == 1:
        df = pd.read_csv('australian.dat', header=None, na_values = '?', delim_whitespace=True)
        print('\nWyświetlam plik:')
        print(df)
        input("\n\nPress Enter to continue...")
    elif response == 2:
        df = pd.read_csv('breast-cancer-wisconsin.data', header=None, na_values = '?')
        print('\nWyświetlam plik:')
        print(df)
        input("\n\nPress Enter to continue...")
    elif response == 3:
        df = pd.read_csv('crx.data', header=None, na_values = '?')
        print('\nWyświetlam plik:')
        print(df)
        input("\n\nPress Enter to continue...")
        toFloat(df.to_numpy())
        config(df.to_numpy())
    elif response == 4:
        struktura()
        main()
    elif response == 5:
        wczytaj_strukture()
    else:
        print("\n\n Coś poszło nie tak, spróbuj jeszcze raz")
        main()

    def normalize(array,nmin,nmax):
        new = []
        for x in array:
            new.append(((x - min(array)) / (max(array) - min(array))*(nmax-nmin))+nmin)
        return new

    def menu_normalizuj():

        print("""\n\nCzy chcesz znormalizować wybrane kolumny?:
                                        1.Tak
                                        2.Nie
                                        3.Normalizuj calosc """)
        response = int(input())
        if response == 1:
            print("\nPodaj przedział do normalizacji:\n")
            nmin = int(input("Przedział dolny: "))
            nmax = int(input("Przedział górny: "))
            list = [int(item) for item in input("Podaj numery wierszy po przecinku : ").split(',')]
            for i in range(len(list)):
                df[list[i]] = normalize(df[list[i]],nmin,nmax)
            print('\nDane po zmianach: ')
            print(df)

        elif response == 2:
            pass
        elif response == 3:
            list = [*range(0, len(df.columns))]
            df.set_axis(list, axis='columns', inplace=True)
            print("\nPodaj przedział do normalizacji: ")
            nmin = int(input("Przedział dolny: "))
            nmax = int(input("Przedział górny: "))
            try:
                for x in range(len(df.columns)-1):
                    df[x] = normalize(df[x], nmin, nmax)
                print("\nDane po zmianach:")
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
            print("\nPlik zapisany pomyślnie!\n\n")
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "/t", 'file:///C:/Users/User/Desktop/SztucznaInteligencja/SztucznaInteligencja/Zadanie1/name.json'])
            menu_zapisz()
        elif response == 2:
            df.to_excel('name.xlsx')
            print("\nPlik zapisany pomyślnie!")
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\Root\\Office16\\EXCEL.EXE", "/t", 'name.xlsx'])
            menu_zapisz()
        elif response == 3:
            df.to_html(r'name.html')
            print("\nPlik zapisany pomyślnie!")
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                    "/t", 'file:///C:/Users/User/Desktop/SztucznaInteligencja/SztucznaInteligencja/Zadanie1/name.html'])
            menu_zapisz()
        elif response == 4:
            main()
        elif response == 5:
            exit()

    menu_normalizuj()
    menu_zapisz()


main()