from sklearn import preprocessing
import numpy as np
import pandas as pd
import json, codecs

def main():
    #np.set_printoptions(suppress=True)
    array2D = []
    data = []
    ## wczytanie pliku
    def wypisz(T):
        for r in T:
            for c in r:
                print(c, end=" ")
            print()

    def uploadFile(name):
        if name == 'australian.dat':
            with open(name, "r") as f:
                for line in f.readlines():
                    line = line.rstrip()
                    line = line.split(" ")
                    array2D.append(line)

            data = np.array(array2D)
            return data

        elif name == 'breast-cancer-wisconsin.data':
            with open(name, "r") as f:
                for line in f.readlines():
                    line = line.rstrip()
                    line = line.split(",")
                    array2D.append(line)

            # for i in range(len(array2D)):
            #     for j in range(len(array2D[i])):
            #         if array2D[i][j] == '?':
            #             array2D[i][j] = None

            data = np.array(array2D)
            return data

        elif name == 'crx.data':
            with open(name, "r") as f:
                for line in f.readlines():
                    line = line.rstrip()
                    line = line.split(",")
                    array2D.append(line)

            # for i in range(len(array2D)):
            #     for j in range(len(array2D[i])):
            #         if array2D[i][j] == '?':
            #             array2D[i][j] = None

            #data = np.array(array2D)
            return array2D

    # ## zamiana na float
    def toFloat(name):
        for i in range(len(name)):
            for j in range(len(name[i])):
                try:
                    float(name[i][j])
                    name[i][j] = float(name[i][j])
                except ValueError:
                    continue


    array2D = uploadFile('crx.data')

    def config(a):
        for i in a[0]:
            if type(i) == str:
                print('Wykryto znak: ' + i)
                for j in range(len(a)):
                    arr = []
                    arr.append(a[j])
                ## decyzja czy usunac czy normalizowac czy zostawic
                ##usun(kol[i])
                ##normalizuj(kol[i])
                ##zostaw(kol[i])
                print(arr)
                print("""\n\nZdecyduj co chcesz zrobić z kolumną z tym znakiem:
                1.Usun
                2.Normalizuj
                3.Nic""")
                response = int(input())
                if response == 1:
                    del array2D[0][1]
                    wypisz(array2D)
                elif response == 2:
                    uploadFile('breast-cancer-wisconsin.data')
                    config(array2D)
                elif response == 3:
                    uploadFile('crx.data')
                # arr = []
                # for j in range(len(a)):
                #     arr.append(a[j][i])

    print("\n wczytuje")
    print(array2D)
    toFloat(array2D)
    config(array2D)

    # ##normalize data
    # def normalize(data):
    #     data = np.array(array2D)
    #     normalized = preprocessing.normalize(data)
    #     return normalized
    #
    # ##adding to csv file
    # def csvFile(name,data):
    #     np.savetxt(name, data.T, delimiter=',', fmt='%f')
    #
    # ##adding to json file
    # def jsonFile(name,data):
    #     Fson = data.tolist()
    #     json.dump(Fson, codecs.open(name, "w"), separators=(',', ':'), sort_keys=True, indent=4)
    #
    # ##adding normalized to html
    # def htmlFile(name,data):
    #     df = pd.DataFrame(data)
    #     html = df.to_html()
    #     f = open(name,'w')
    #     f.write(html)
    #     f.close()
    #
    # ##wywoływanie funkcji
    #
    # #uploadFile('australian.dat')
    # #toFloat(array2D)
    # #csvFile('australian.csv',normalize(array2D))
    # #jsonFile('australian.json',normalize(array2D))
    # #htmlFile('australian.html',normalize(array2D))
    #
    # def print_menu_read():
    #     print("""\n\nWybierz plik do wczytania:
    #     1.australian
    #     2.breast-cancer-wisconsin
    #     3.crx""")
    #     response = int(input())
    #     if response == 1:
    #         uploadFile('australian.dat')
    #     elif response == 2:
    #         uploadFile('breast-cancer-wisconsin.data')
    #         config(array2D)
    #     elif response == 3:
    #         uploadFile('crx.data')
    #
    # print_menu_read()
    #
    #
    # print("\nplik po normalizacji:")
    # print(normalize(data))
    #
    # def readFile(name):
    #     print("\nWyświetlam plik:")
    #     f = open(name,"r")
    #     for line in f:
    #         print(line, end="")
    #
    # def print_options():
    #     print("""\n\nCo dalej?:
    #         1.zapisz do json
    #         2.zapisz do csv
    #         3.zapisz do html
    #         4.wybierz inny plik
    #         5.zakończ""")
    #     response = int(input())
    #     if response == 1:
    #         jsonFile('file.json',normalize(array2D))
    #         readFile('file.json')
    #     elif response == 2:
    #         csvFile('file.csv',normalize(array2D))
    #         readFile('file.csv')
    #     elif response == 3:
    #         htmlFile('file.html',normalize(array2D))
    #         readFile('file.html')
    #     elif response == 4:
    #         main()
    #     elif response == 5:
    #         exit()
    #
    # while True:
    #     print_options()


main()
