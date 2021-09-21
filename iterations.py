# Une itération (boucle) consiste à reproduire des instructions un certain nombre de fois

#affiche "Bonjour" 5 fois. Approche "naïve"
'''print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")'''
# ctrl+/ permet de commenter automatiquement

# utilisation de la boucle while (tant que). Cette boucle a besoin d'une condition.
# while permet de faire une condition multiple.
# --> Le nombre d'itération est connue à l'avance. Ce sont des boucles finies

# incrémentation
cpt = 0
while cpt < 5 :
    print("Bonjour", cpt +1, "fois") # pour ne pas avoir le 0 fois, on peut commencer le cpt à 1 et finir la boucle à 6
    cpt +=1

# décrémentation
cpt2 = 5
while cpt2 != 0 :
    print("Au revoir", cpt2, "fois") # pour ne pas avoir le 0 fois, on peut commencer le cpt à 1 et finir la boucle à 6
    cpt2 -=1

cpt3 = 5
while cpt3 > 0 :
    print("Au revoir", cpt3, "fois") # pour ne pas avoir le 0 fois, on peut commencer le cpt à 1 et finir la boucle à 6
    cpt3 -=1


# Utilisation de la boucle for...in (pour chaque). 
# Boucle adaptée au parcours de collection de données
# range renvoie ici un ensemble de 5 éléments
for i in range(5): # borne 5 non incluse
    print("Bonjour", i+1, "fois")