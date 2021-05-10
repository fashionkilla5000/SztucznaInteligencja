import pandas as pd
import numpy as np
import math as m
import collections
import random

def main():
    def normalize_all():
        print("\nPodaj przedział do normalizacji: ")
        global nmin
        global nmax
        nmin = int(input("Przedział dolny: "))
        nmax = int(input("Przedział górny: "))
        for x in range(len(df.columns)-1):
            df[x] = normalize(df[x], nmin, nmax)


    def normalize(array, nmin, nmax):
        new = []
        for x in array:
            new.append(((x - min(array)) / (max(array) - min(array))*(nmax-nmin))+nmin)
        return new


    def toFloat(name):
        for i in range(len(name)):
            for j in range(len(name[i])):
                try:
                    float(name[i][j])
                    name[i][j] = float(name[i][j])
                except ValueError:
                    continue


    def config(array):
        j = -1
        for i in array[0]:
            j = j + 1
            if type(i) == str and j<len(array[0])-1:
                arr = df[j].to_numpy()
                list = collections.Counter(arr)
                del list[np.nan]
                viter = iter(list)
                x = len(list.values())
                for k in viter:
                    df[j] = df[j].replace([k], x)
                    x = x - 1


    print("""\nWybierz jendą z opcji:
            1.Wczytaj australian
            2.Wczytaj breast-cancer-wisconsin
            3.Wczytaj crx""")
    response = int(input())
    if response == 1:
        df = pd.read_csv('australian.dat', header=None, na_values='?', delim_whitespace=True)
        normalize_all()
        print('\nWyświetlam plik:')
        print(df)
    elif response == 2:
        df = pd.read_csv('breast-cancer-wisconsin.data', header=None, na_values='?')
        normalize_all()
        print('\nWyświetlam plik:')
        print(df)
    elif response == 3:
        df = pd.read_csv('crx.data', header=None, na_values='?')
        toFloat(df.to_numpy())
        config(df.to_numpy())
        normalize_all()
        print('\nWyświetlam plik:')
        print(df)

    def metryka_logarytm(row1, row2):
        odleglosc = 0.0
        for i in range(len(row1) - 1):
            if np.isnan(row1[i]) or np.isnan(row2[i]):
                continue
            else:
                odleglosc += m.fabs(m.log10(row1[i]) - m.log10(row2[i]))
        return odleglosc


    def metryka_czebyszew(row1, row2):
        odleglosc = 0.0
        for i in range(len(row1) - 1):
            if np.isnan(row1[i]) or np.isnan(row2[i]):
                continue
            else:
                odleglosc += (m.log10(row1[i]) - m.log10(row2[i]))
        return max(odleglosc)


    def metryka_minkowski(row1, row2, p):
        odleglosc = 0.0
        for i in range(len(row1) - 1):
            if np.isnan(row1[i]) or np.isnan(row2[i]):
                continue
            else:
                odleglosc += m.fabs(row1[i] - row2[i]) ** p
        return odleglosc ** (1 / p)


    def metryka_euklides(row1, row2):
        odleglosc = 0.0
        for i in range(len(row1) - 1):
            if np.isnan(row1[i]) or np.isnan(row2[i]):
                continue
            else:
                odleglosc += ((row1[i] - row2[i]) ** 2)
            odleglosc += ((row1[i] - row2[i]) ** 2)
        return m.sqrt(odleglosc)

    def najblizsze_probki(data, probka, k, decyzja,p):
        list = []
        for row in data:
            if decyzja == 1:
                odl = metryka_euklides(probka, row)
            if decyzja == 2:
                odl = metryka_minkowski(probka, row, p)
            if decyzja == 3:
                odl = metryka_czebyszew(probka, row)
            if decyzja == 4:
                odl = metryka_logarytm(probka, row)
            list.append((row,odl))
        list.sort(key=lambda tup: tup[1])
        najblizsze = []
        for i in range(k):
            najblizsze.append(list[i][0])
        print("\n\nNajlblizsze probki: \n")
        return najblizsze

    def pierwszy(probki, atrybuty):
        n = len(probki.columns) - 1 #15 kolumn
        num = probki.to_numpy()
        c = collections.Counter(num[:, n])
        a = c.most_common(1)[0]
        try:
            err = c.most_common(2)[1]  ## err[1]
            er = c.most_common(1)[0]
            l = [err[1], er[1]]
            if len(l) > 1 and err[1] == er[1]:
                print("Error: nie można przypisać klasy decyzyjnej")
                atrybuty.append('?')
                return atrybuty
        except:
            pass

        print("\nKlasa decyzyjna: ",a[0])
        atrybuty.append(a[0])
        return atrybuty

    def ostatni(arr,k,decyzja,p):
        col = len(arr.columns)
        row = len(arr[0])
        poprawnie = 0
        zle = 0
        error = 0
        for x in range(row):
            arr = arr.to_numpy()
            atrybuty = arr[x,:-1]
            wiersz = arr[x,:]
            wiersz = wiersz.tolist()
            atrybuty = atrybuty.tolist()
            x = najblizsze_probki(arr,atrybuty,k,decyzja,p)
            x = pd.DataFrame(x)
            arr = pd.DataFrame(arr)
            dec = pierwszy(x,atrybuty)
            print(wiersz)
            print(dec)
            pd.DataFrame(dec)
            if dec[col-1] == wiersz[-1]:
                poprawnie += 1
            elif dec[col - 1] == '?':
                error+=1
            else:
                zle+=1

        print("\n\nPoprawne: ",poprawnie)
        print("Błędnie: ",zle)
        print("Nie da się sklasyfikować: ",error)
        print('Współczynnik poprawności: ',int((poprawnie/(zle+error+poprawnie))*100), '%')


    def losuj_atrybuty():
        randomlist = random.sample(range(0, 50), len(df.columns) - 1)
        randomlist = normalize(randomlist, nmin, nmax)
        print('Wylosowane atrybuty po normalizacji :\n', randomlist)
        return randomlist


    def wczytaj_atrybuty():
        atrybuty = []
        print('Podaj kolejno atrybuty')
        while (len(atrybuty) != len(df.columns) - 1):
            atrybuty.append(int(input()))
        atrybuty = normalize(atrybuty, nmin, nmax)
        print('Podane atrybuty po normalizacji: \n', atrybuty)
        return atrybuty


    def najblizsze_probki2(data, probka, k,decyzja,p):
        list = []
        for row in data:
            if decyzja == 1:
                odl = metryka_euklides(probka, row)
            if decyzja == 2:
                odl = metryka_minkowski(probka, row, p)
            if decyzja == 3:
                odl = metryka_czebyszew(probka, row)
            if decyzja == 4:
                odl = metryka_logarytm(probka, row)
            list.append((row,odl))
        list.sort(key=lambda tup: tup[1])
        print(pd.DataFrame(list))
        najblizsze = []
        for i in range(k):
            najblizsze.append(list[i][:])
        return najblizsze

    def podziel(arr, k,atrybuty,metryka,p):
        n = len(arr.columns) - 1
        num = arr.to_numpy()
        myset = set(num[:, n])
        viter = iter(myset)
        uniq = []
        for x in viter:
            print('vitter',x)
            uniq.append(x)

        minusy = arr.loc[arr[n] == uniq[0]]
        plusy = arr.loc[arr[n] == uniq[1]]

        minusy = minusy.to_numpy()
        plusy = plusy.to_numpy()

        minusy = najblizsze_probki2(minusy, atrybuty, k,metryka,p)
        plusy = najblizsze_probki2(plusy, atrybuty, k,metryka,p)

        print("Najblizsze probki : \n\n")
        print(uniq[0])
        print(pd.DataFrame(minusy))
        print('\n\n',uniq[1])
        print(pd.DataFrame(plusy))

        minus = zlicz(pd.DataFrame(minusy))
        plus = zlicz(pd.DataFrame(plusy))

        if minus < plus :
            decyzja = uniq[0]
        if plus < minus:
            decyzja = uniq[1]

        print("\n\nKlasa decyzyjna: ", decyzja)
        atrybuty.append(decyzja)
        print('\n', atrybuty)

    def zlicz(arr):
        suma = 0
        for x in arr[1]:
            suma += x
        return suma

    response = int(input("""\nWybierz
        1. cz1
        2. cz2\n"""))
    if response == 1:
        print("""\nWybierz sposób:
                1.najwiecej klas decyzyjnych w k najblizszych probkach
                2.najmniejsza suma odleglosci w najblizszych probkach z kazdej klasy decyzyjnej""")
        response = int(input())
        if response == 1:
            response = int(input("""\nCo dalej?:
            1.Wczytaj atrybuty
            2.Losuj atrybuty\n"""))
            if response == 1:
                atrybuty = wczytaj_atrybuty()
            elif response == 2:
                atrybuty = losuj_atrybuty()
            decyzja = int(input("""\nWybierz metrykę:
                                1.Euklidesa
                                2.Minkowskiego
                                3.Czebyszewa"
                                4.z logarytmem\n"""))
            k = int(input("\n\nPodaj parametr k: "))
            if decyzja == 2:
                p = int(input("Podaj parametr p: "))
            else:
                p = 1
            probki = pd.DataFrame(najblizsze_probki(df.to_numpy(), atrybuty, k,decyzja,p))
            print(probki)
            print(pierwszy(probki, atrybuty))
            input("\n\nWciśnij Enter aby zacząć od nowa")
            main()
        if response == 2:

            response = int(input("""\nCo dalej?:
                            1.Wczytaj atrybuty
                            2.Losuj atrybuty"""))
            if response == 1:
                atrybuty = wczytaj_atrybuty()
            elif response == 2:
                atrybuty = losuj_atrybuty()
            decyzja = int(input("""\nWybierz metrykę:
                                1.Euklidesa
                                2.Minkowskiego
                                3.Czebyszewa"
                                4.z logarytmem\n"""))
            k = int(input("\n\nPodaj parametr k: "))
            if decyzja == 2:
                p = int(input("Podaj parametr p: "))
            else:
                p = 1
            podziel(df, k,atrybuty,decyzja,p)
            input("\n\nWciśnij Enter aby zacząć od nowa")
            main()
    if response == 2:
        decyzja = int(input("""\nWybierz metrykę:
                            1.Euklidesa
                            2.Minkowskiego
                            3.Czebyszewa"
                            4.z logarytmem\n"""))
        k = int(input("\n\nPodaj parametr k: "))
        if decyzja == 2:
            p = int(input("Podaj parametr p: "))
        else:
            p = 1
        ostatni(df, k,decyzja,p)
        input("\n\nWciśnij Enter aby zacząć od nowa")
        main()

main()

