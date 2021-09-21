'''
if 2 > 1 :
    print("2 est supérieur à 1")

if 2 > 3 :
    print("2 est supérieur à 3")
'''

isEarthRound = True
message = "2 est strictement supérieur à 1"
condition = 2 > 1 # cette variable vaut True

# version courte
if isEarthRound :
    print("La terre est ronde")

# version longue
if isEarthRound == True:
    print("La terre est ronde")

if condition :
    print(message)

n = 5
if n >= 7 :
    print("Assez nombreux pour jouer au foot")
else :
    print("Forfait, pas assez de joueurs")

'''
if n >= 7+1 : # and est le "et" logique donc intersection ; or est le "ou"
    print("Assez nombreux pour jouer au foot")
else :
    print("Forfait, pas assez de joueurs")
'''

exemple1 = False or True
print("False or True =>", exemple1) # exemple1 vaut True car True gagne. Dans or : si un est vrai alors l'expression est vrai

exemple2 = False and True
print("False and True =>", exemple2) # Dans le and : il suffit qu'il y ait un false pour que ce soit false.

exemple3 = not False
print("not False =>", exemple3)

n = 7
observeFifaRules = True
if n >= 7 and observeFifaRules : # les deux doivent être vrai pour rentrer dans le if. On est plus restrictif car si l'un est vrai ce sera faux quand même
    print("Assez nombreux pour jouer au foot")
else :
    print("Forfait, pas assez de joueurs")