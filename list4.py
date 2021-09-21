students = ["Afouda Pamela",
"Castets Pierre",
"Dedals Alexandre",
"Pelle Piere-Jean",
"Saupagna Sébastien"
]

# Objectif : obtenir un email à partir de la chaïne Nom Prénom
# Exemple : "Afouda Pamela" => pamela.afouda@python.com

'''
student = "Afouda Pamela".lower() # mise en minuscule
spaceIndex = student.find(" ")
lastName = student[:spaceIndex] # nom de famille
firstName = student[spaceIndex + 1 :] # prénom
email = firstName + "." + lastName + "@python.com"
print(email)
'''

for s in students :
    student = s.lower() # mise en minuscule
    spaceIndex = student.find(" ")
    lastName = student[:spaceIndex] # nom de famille
    firstName = student[spaceIndex + 1 :] # prénom
    email = firstName + "." + lastName + "@python.com"
    emailNoAccent = email.replace("é", "e")
    print(emailNoAccent)

    # exemple de chaïnage de méthodes de str
    # print(s.lower().replace("é","e").replace("-","_"))