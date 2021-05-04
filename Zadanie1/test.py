import pandas as pd
import numpy as np
import collections


df = pd.read_csv('crx.data', header=None)


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


def config(a):
    j=-1
    for i in a[0]:
        j= j+1
        if type(i) == str:
            print('Wykryto znak: ' + i + ' w kolumnie: ', j)
            print('wczytuje kolumne:')
            print(df[j])
            print("""\n\nZdecyduj co chcesz zrobić z kolumną z tym znakiem:
                            1.Usun
                            2.Zamień na liczby
                            3.Nic""")
            response = int(input())
            if response == 1:
                del df[j]
                print(df)
            elif response == 2:
                arr = df[j].to_numpy()
                list = collections.Counter(arr)
                viter = iter(list)
                x = len(list.values())
                for k in viter:
                    df[j] = df[j].replace([k], x)
                    x= x-1
                print(df)
            elif response == 3:
                print(df)
                continue


print(df)
config(nf)
print(df)