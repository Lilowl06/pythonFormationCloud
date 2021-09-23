# Le format csv est un fichier dans lequel les informations sont séparées par des ",".
# Ex : blabla,blzlff,48,fdF@edofi.dsf,dev ...
# Le format tsv c'est pareil mais séparé avec des tabulations

# Analyse du fichier cities.csv
f = open("files/cities.csv", "r")
content = f.read()
f.close()

# contente2 = f.read() # impossible car le fichier a été fermé

rows = content.splitlines() # renvoie une liste !
# print(len(rows))
cityNameIndex = 8
n = 0 # compteur du nombre de villes correspondant aux critères de recherche

for r in rows :
    cols = r.split(",") # virgule, comme séparateur
    cityName = cols[cityNameIndex].strip().strip("") # enlève les espaces en début/fin de chaïne, enlève les guillemets
    # print(cityName, "=>", len(cityName))
    if cityName.startswith("San") :
        n += 1

# r = "toto-tata-titi".split("-")
# print(r)

s = " \" Yakima\"".strip()
print(len(s))
