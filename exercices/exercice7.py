'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

import csv

with open("files/deniro.csv", "r") as csvFile :
    rows = csv.reader(csvFile, delimiter=",")
    next(rows, None)
    meilleurScore = 0
    cmpAnnee = 0
    for r in rows :
        score = int(r[1].strip().strip("\""))
        annee = int(r[0].strip().strip("\""))
        title = r[2].strip().strip("\"")
        if score > meilleurScore :
            meilleurScore = score
            meilleurFilmTitle = title
        if annee > 1999 and annee < 2011 :
                cmpAnnee += 1

with open("deniroReport.txt", "w") as txtFile :
    txtFile.write(f"Le titre du film ayant obtenu le meilleur score est {meilleurFilmTitle}.\nEntre 2000 et 2010 Deniro a joué dans {cmpAnnee} films")