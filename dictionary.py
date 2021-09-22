# Un dictionnaire est une structure clé/valeur permettant de détailler une information/entité
# Sérialisation = convertir en chaîne de caractère un élément qui au départ n'en n'est pas un et qui est assez complexe.

import tools # car il est dans la même arborescence, pas besoin d'indiquer le chemin.

d = {}
# print(type(d)) # <class 'dict'>

student = {
    "firstname" : "Chris",
    "lastname" : "Dufour",
    "email" : "c.dufour@python.com",
    "age" : 99,
    "rates" : [8,12,17]
}

# print (student) # permet de sérialiser le dictionnaire.

# accès en lecture aux clés du dictionnaire :
print(student["firstname"], "a", student.get("age"), "ans")

# accès en écriture :
student["lastname"] = "DUFOUR"
student["rates"].append(15)
student["tel"] = "0788996633" # ajoute une nouvelle clé
student.pop("age") # supprime la clé
print(student)

# itération sur un dictionnaire :
for x in student :
    print(x, "=>", student[x])

# print("-------------------------------------")
tools.separator("-",30)

for v in student.values():
    print(v)

# print("-------------------------------------")
tools.separator("-",30)

for k in student.keys() :
    print(k)

