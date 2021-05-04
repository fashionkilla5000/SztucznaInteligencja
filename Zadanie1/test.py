import pandas as pd
import numpy as np
import collections

def main():
    df = pd.read_csv('crx.data', header=None, na_values = '?')


    nf = df.to_numpy()

    def toFloat(name):
        for i in range(len(name)):
            for j in range(len(name[i])):
                try:
                    float(name[i][j])
                    name[i][j] = float(name[i][j])
                except ValueError:
                    continue

    toFloat(nf)

    def normalize(array,nmin,nmax):
        new = []
        for x in array:
            new.append((x - min(array) / max(array) - min(array))*((nmax-nmin)+nmin))
        return new

    def config(array):
        j=-1
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

        input("\n\nPress Enter to continue...")

        print("""\n\nCzy chcesz znormalizować wybrane kolumny?:
                                        1.Tak
                                        2.Nie""")
        response = int(input())
        if response == 1:
            n = int(input('podaj liczbe kolumn do normalizacji: '))
            print("\nPodaj przedział do normalizacji: ")
            nmin = int(input())
            nmax = int(input())
            print("\nPodaj kolejno kolumny do normalizacji: ")
            for i in range(0, n):
                x = int(input())
                df[x] = normalize(df[x],nmin,nmax)

            print('\nDane po zmianach: ')
            print(df)

        elif response == 2:
            pass


    print(df)
    input("\n\nPress Enter to continue...")
    config(nf)

main()