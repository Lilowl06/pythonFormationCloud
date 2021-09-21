'''
*** EXO 3 ***
Ecrire un script python , qui calculera et affichera pour chacun des prix le prix TTC.
Créer une fonction qui calculera le prix TTC du prix HT en entrée

'''

print("*** EXO 3 ***")

pricesHt = [14,100,30,10,8]
tva = 20 #c'est un pourcentage 20%

def getPriceWithTva(prixHt, tva):
    return round(prixHt * (1 + tva/100), 2) # retour du prix Ttc arrondi

for prix in pricesHt :
    print(getPriceWithTva(prix,7))