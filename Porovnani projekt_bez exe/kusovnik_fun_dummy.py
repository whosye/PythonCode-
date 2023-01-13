import numpy as np
import pandas as pd

def Kusovnik(KUS):

    kusovnik = pd.read_excel(KUS)
    kusovnik = np.array(kusovnik)
    row, column = kusovnik.shape
    NEXT = "NEXT"
    A = []
    print(row)
    print(column)
### ID nalezeni
    for i in range(0,1):
        for j in range(0,2):
            if type(kusovnik[j][i]) == str:
                cislo_kusovniku = kusovnik[j][i]
                A.append(cislo_kusovniku)
                print(cislo_kusovniku)
                A.append(NEXT)
                break
### Nalezeni potrebne polohy jednotlivych sloupcu

    for x in range(0,20):
        for y in range(0,20):
            if "Menge" in str(kusovnik[y][x]):
                MENGE = x
                print("MENGE: " + str(MENGE))
                for k in range(0,20):
                    if "Komponentenbezeichnung" in str(kusovnik[y][k]):
                        NAME  = k
                        KOMPO = k-1
                        POS   = k-2
                    elif k == 20:
                        print("Nenalezen  Komponentenbezeichnung")
        if x == 20:
            print("Nenalezen Menge")


    A_count =[]

    for xx in range(0,2):
        for yy in range(10,row):
            if "A" == str(kusovnik[yy][xx]):
                A_count.append(kusovnik[yy][xx])
                A_MIN = A_count.count("A")
                if A_MIN < 5:
                    pass
                else:
                    Beschr = xx
                    print("Beschr: "+str(Beschr))
                    break
        if xx == 2:
            print("Nenalezen Beschr.. ")
            break






    for j in range(row):
        if type(kusovnik[j][MENGE]) == int or ("." or ",") in str(kusovnik[j][MENGE]):
            menge = kusovnik[j][MENGE]

            for l in range(j,row):
                if type(kusovnik[l][KOMPO]) == int:
                    Num = kusovnik[l][KOMPO]
                    A.append(Num)
                    A.append(menge)
                else:
                    break
            for k in range(j,row):

                if type(kusovnik[k][NAME]) == str:
                    name = kusovnik[k][NAME]
                    #print(name)
                    A.append(name)
                else:
                    break

            for p in range(j,row):
                if type(kusovnik[p][POS]) == int:
                    Pos = kusovnik[p][POS]
                    A.append(Pos)
                elif type(kusovnik[p][POS]) != float:
                    A.append("ERROR-POS")
                    break
                else:
                    break

            for u in range(j, row):
                if kusovnik[j][Beschr] == "A":
                    if "Hinzu:" in str(kusovnik[j+1][Beschr]) and "TC" in str(kusovnik[j+2][Beschr]):
                        for bb in range(j+2,j+12):
                            if kusovnik[bb][Beschr] == "A":
                                break
                            elif str(kusovnik[bb][Beschr]) == "nan":
                                break
                            else:
                                T = kusovnik[bb][Beschr]
                                T = T.replace(" ", "")
                                T = T[3:]
                                #print(str(T))
                                A.append(T)
                                if ";" in str(T): #396_04_1100_0010;0020;0030;0040; 0050
                                    count = T.count(";")
                                    T1 = T[0:12]
                                    for P in range(count):
                                        if P == 0:
                                            T2 = T1 + T[(12):(16)]
                                            A.append(T2)
                                            #print(T2)
                                        else:
                                            A.append(T3)
                                            T3 = T1 + T[(12 + (5 * P)):(16 + (5 * P))]
                                            #print(T3)
                                    else:
                                        #print(str(T))
                                        A.append(T)
                        break

                    elif "TC" in str(kusovnik[j+1][Beschr]):
                        for bb in range(j+1,j+12):
                            if kusovnik[bb][Beschr] == "A":
                                break
                            elif str(kusovnik[bb][Beschr]) == "nan":
                                break
                            else:
                                T = kusovnik[bb][Beschr]
                                T = T.replace(" ", "")
                                T = T[3:]
                                if ";" in str(T): #396_04_1100_0010;0020;0030;0040; 0050
                                    count = T.count(";")
                                    T1 = T[0:12]
                                    for P in range(count):
                                        if P == 0:
                                            T2 = T1 + T[(12):(16)]
                                            A.append(T2)
                                            #print(T2)
                                        else:
                                            T3 = T1 + T[(12 + (5 * P)):(16 + (5 * P))]
                                            A.append(T3)
                                            #print(T3)
                                else:
                                    #print(str(T))
                                    A.append(T)
                        break

                    elif str(kusovnik[j+1][Beschr]) == "nan":
                        T4 = "EMPTY"
                        A.append(T4)
                        break
                    else:
                        if "Hinzu:" in str(kusovnik[j+1][Beschr]):
                            for c in range(j+2,j+8):
                                #print("C: "+str(c))
                                if str(kusovnik[c][Beschr]) == "nan":
                                    break
                                elif str(kusovnik[c][Beschr]) == "A":
                                    break
                                else:
                                    T5 = kusovnik[c][Beschr].replace(" ", "")
                                    A.append(T5)
                        break


            A.append(NEXT)
    return A
