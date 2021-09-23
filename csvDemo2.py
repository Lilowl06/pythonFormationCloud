import csv

cityNameIndex = 8
n=0

with open("files/cities.csv", "r") as csvFile :
    # content = csvFile.read() # si je rajoute cette ligne, le nombre de ligne trouvées est de 0 car comme j'ai lu le fichier ici
    # et que la tête de lecture est en bas du fichier.
    rows = csv.reader(csvFile, delimiter=",")
    rows2 = [1,5,6]

    for r in rows :
        print(r)
        cityName = r[8].strip().strip("\"")
        if cityName.startswith("San") :
            n += 1

print("Nombre de villes trouvées : %d" % n)
# print(type(rows))

'''for x in range(5) :
    print(x)'''