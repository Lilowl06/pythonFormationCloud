'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5 : flags => flagsBis ***")

import os
import shutil

# Détermination de l'emplacement du dossier cible qui contiendra tous les fichiers flags renommés
targetDir = "/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/flagsBis"

# Vérification de l'existance du dossier. Si le dossier n'existe pas, alors il est créé.
if not os.path.isdir(targetDir):
    print("Le dossier cible '%s' n'existe pas" %targetDir)
    try :
        os.mkdir(targetDir)
        print("Le dossier cible '%s' a été créé" %targetDir)
    except :
        print("Impossible de créer le dossier cible '%s'" %targetDir)
        exit()

# Déplacer et renommer les fichiers flags du dossier d'origine flags vers le dossier flagsBis
files = os.listdir("formation-python/exos/flags/")
numMovedFiles = 0
pathOldDir = "/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/formation-python/exos/flags/"
pathNewDir = "/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/flagsBis/"

for f in files :
    twoFirstLetter = f[:2].upper()
    # mettre une exception si deux pays on les mêmes premières lettres, trouver une solution
    fileOldDir = pathOldDir + f
    fileNewDir = pathNewDir + twoFirstLetter + ".png"

    if f != "missing.png" :
        try :
            cmp = 1
            while os.path.exists(fileNewDir) :
                fileNewDir = pathNewDir + twoFirstLetter + "_" + str(cmp) + ".png"
                cmp += 1
            
            shutil.copy(fileOldDir, fileNewDir)
            numMovedFiles += 1
            print(f"Le fichier {f} a été copié et renommé vers son dossier de destination")

        except :
            print(f"=> Erreur ! Le fichier {f} n'a pas peu être copié !")

print("%d fichiers ont été copiés et renommés" % numMovedFiles)