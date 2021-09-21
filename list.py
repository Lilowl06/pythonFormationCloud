l = []
print(type(l)) # <class 'list'> vide

numbers = [2,19,14,10,6]

# accès en lecture :
print("Premier chiffre :", numbers[0])
# index négatif (inversé) : on part de la fin
print("Dernier chiffre :", numbers[-1]) # il part de la fin de la liste, dernier de la liste
print("Avant-dernier chiffre :", numbers[-2]) # avant dernier de la liste
# print(numbers[5])# error : list index out of range

# Il est possible de calculer les indices :
print("Troisième chffre :", numbers[1+1])

# accès en écriture :
numbers[0] = 4
print("Premier chiffre :", numbers[0])

# numbers[0] = True
# print("Premier chiffre :", numbers[0]) # on peut mettre des valeurs de différent type dans une liste

index = 0
for n in numbers :
    #print("Le double de :", n, "est", n*2) # pas d'altération de la liste d'origine
    #n = n*2 # racourci en n *= 2 # n n'est pas modifié en dehors de la boucle
    #print(n) 
    numbers[index] = n*2 # mutation du tableau dans sa totalité
    index += 1

for n in numbers :
    print(n) # rien n'a doublé car n est une copie de la valeur n

print("__________________________")
# ajout d'un élément  à ma liste
numbers.append(20)
numbers.append(5)

for n in numbers :
    print(n)

print("__________________________")

for n in enumerate(numbers) : # apporte une surcouche à la liste pour ajouter un mécanisme supplémentaire
    print(n) # il renvoie sous forme de tuple (l'index, et la valeur de l'élément)

print("__________________________")

for index, value in enumerate(numbers) :
    print(index, "=>", value)