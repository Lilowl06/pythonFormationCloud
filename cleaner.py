# Ce script supprime les fichiers .txt qu'il trouve dans le dossier cible
import os

# lister la totalité des fichiers qu'il trouve dans le dossier files
files = os.listdir("files")
numRemovedFiles = 0

for f in files :
    # print(f)
    extension = f[-3:]
    if extension == "txt" :
        os.remove("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/"+f)
        numRemovedFiles += 1
        print("Fichier '%s' supprimé" %f)

    # print(extension)

print("%d fichiers ont été supprimés" % numRemovedFiles)