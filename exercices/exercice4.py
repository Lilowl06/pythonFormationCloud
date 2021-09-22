'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''

print("*** EXO 4: somme de saisies ***")

# Votre code ici
userInput = int(input("Veuillez saisir un chiffre ? "))
cptSaisi = []
while userInput != 0 :
    cptSaisi.append(userInput)
    userInput = int(input("Veuillez saisir un chiffre ? "))

print(f"=> La somme des valeurs saisies : {sum(cptSaisi)}, {cptSaisi}")

# Correction avec une boucle while True

def sumNumbers(numbers) :
    s = 0 # somme
    for n in numbers :
        s += n
    return s


values = []
while True :
    userInput = int(input("Saisir un chiffre (0 pour quitter le programme) :"))
    if userInput == 0 :
        break # sortie de boucle
    else :
        values.append(userInput)

# valuesFormatted = str(values).replace("[", "(").replace("]",")")
valuesFormatted = "(valeurs saisies : " + str(values).strip("[]")+")"

print("Somme des valeurs saisies :", sumNumbers(values), valuesFormatted)