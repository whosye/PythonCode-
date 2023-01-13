import numpy as np
import pandas as pd



def model(ID):

    cislo_kusovniku = ID
    #### FF.xlsx jmeno porovnavaciho kus
    TVL = pd.read_excel("FF.xlsx", usecols=[50,64,69,73,75,76])

    NEXT = "NEXT"
    TVL = np.array(TVL)
    row, col = TVL.shape
    #print(row)

    P = []
    P.append(cislo_kusovniku)
    P.append(NEXT)
    #print("ROW: "+ str(row))
    for i in range(row):
        #print(TVL[i][0])
        if TVL[i][0] == ID:
            P.append(TVL[i][4])  # komponente
            P.append(TVL[i][3]) #menge
            P.append(TVL[i][5])  # nazev v nemcine
            #print("i: "+str(i))
            #print("KOMPONENTE: "+str(TVL[i][4]))
            #print("MENGE: " + str(TVL[i][3]))
            print("NAZEV NEMECKY: " + str(TVL[i][5]))

            L = str(TVL[i][2]) # Pos - material

            if L.isnumeric():
                if L[-4] != str(0):
                    L = L[-4:]
                    P.append(int(L))
                    #print("POS MATERIAL: "+str(L))
                elif L[-4] == str(0):
                    L = L[-3:]
                    P.append(int(L))
                    #print("POS MATERIAL: " + str(L))
            else:
                P.append("MISSING MAT.")
                #print("POS MATERIAL: "+str(L))
            # smycka pro Beschreibung / Beziehungswissen

            if ";" in TVL[i][1]:
                X = TVL[i][1]
                indicies_list = []
                for i, value in enumerate(X):
                    if value == ";":
                        indicies_list.append(i)
                indicies_list.append(indicies_list[-1] + 5)
                for j in range(len(indicies_list)):
                    batch = X[indicies_list[j] - 4:indicies_list[j]]
                    L = X[:indicies_list[0] - 4] + batch
                    newL = X[:3] + "_" + L[3:]
                    newL = newL.replace("-", "_")
                    P.append(newL)

                P.append(NEXT)
            elif ("0") not in TVL[i][1]:
                P.append(TVL[i][1])
                P.append(NEXT)

            else:
                T = TVL[i][1]
                T1 = T[0:3] + "_" + T[3:]
                T1 = T1.replace("-", "_")
                P.append(T1)
                P.append(NEXT)
    return P
