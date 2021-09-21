postCodes = [67200, 75012, 68520, 15000, 75020, 67200, 75012, 68520, 15000, 75020,
67275, 75013, 75990, 15000, 75820]

# print(len((postCodes))) affiche la longueur de la liste => 10

# Combien de codes parisiens ?
# Si ce sont des nombres : on peut dire que les codes parisiens sont compris entre 75000 et 75999
# Si ce sont des string : on peut dire que si les deux premières lettre sont égales à 75 alors c'est un code parisien

'''
code = "75020"
code2 = 75020
if code[:2] == "75": # si je remplace la valeur pas code 2 ; ca ne fonctionne pas # error : 'int' object is not subscriptable
    print("Paris")
else :
    print("Ce n'est pas Paris")
'''

numParis = 0
for code in postCodes:
    if code >= 75000 and code < 76000:
        numParis +=1

print("Nombre de codes postaux parisiens :", numParis, "sur", len(postCodes))