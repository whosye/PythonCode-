from find21 import Run
####VZOR####
#   KUS = "BOM_T193335.xlsx"
#   ID  = "T193335"
#   ID  .. jmeno excelu obsahujici veskere info o vsech kusovnicich
#   KUS .. jmeno excelu jednotliveho kusovniku s priponou .xlsx
############

#KUS = "BOM_T193335.xlsx"
#ID  = "T193335"

#KUS = "T187943_exp.xlsx"
#ID  = "T187943"

#KUS = "B_T188958.xlsx"
#ID = "T188958"

#KUS = "T187943.xlsx"
#ID ="T187943"


#KUS = "T183351.xlsx"
#ID ="T183351"

print("POROVNANI")
KUS = input("VLOZ JMENO EXCELU VE TVARU napr = T187943.xlsx:  ")
ID  = input("VLOZ ID KUSOVNIKU VE TVARU napr. = T187943:  ")

print("Zvolene jmeno kusovniku: "+str(KUS))
print("Zvolene ID    kusovniku: "+str(ID))

START = Run(KUS,ID)
try:
    START = START.main()



    input("PRO ZAVRENI KONSOLE STISKNI ENTER")

except:
    print("error")


