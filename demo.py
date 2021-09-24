import platform, os

from colorama.ansi import Style
import tools
import mypackage.subpackage.subdemo as sd
from colorama import *
import time

'''
print(platform.system())
print(platform.processor())
'''

import os # très très utile "Oprérating système" permet d'effectuer des opération en lecture et écriture ou nveiau du système d'explotation sous 
# jaccent au niveua de l'interpréteur python. De faire de l'administration système, création de fichiers, dossiers, lien symbolique, vérification accès, 
# droits, permission, etc...

'''
print(os.name) # return posix 
print(os.getcwd())
'''

# os.mkdir() : permet de créer un dossier en total automatisation
# arguments = (path, mode=0o777, *, dir_fd=None)
# os.mkdir("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/tmp") # création d'un fichier tmp

'''
for x in range(5) :
    # os.mkdir("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/tmp" + str((x+1)))
    os.rmdir("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/tmp" + str((x+1)))
'''

# On veut supprimer les dossiers que l'on a créer :
# os.remove : ne permet de ne supprimer que des fichiers
# os.rmdir : supprime les dossiers


# on ouvre plein de possibilité d'administration avec python !

import shutil # fait aussi parti du top 4/5 des modules les plus utilisés !

# ou en une ligne
# import platform, os, shutil

'''
students = ["Sébastien", "Pamela", "Aude"]
lenNames = [len(s) for s in students]
print(lenNames)
'''


'''
sd.subdemoprint() # exécution d'une fonction placée dans un sous-package que nous avons importé et aliasé
'''


'''
# Utilisation du module colorama afin de changer les couleurs dans l'interpréteur de commande
print(Fore.LIGHTMAGENTA_EX + "Bravo !")
print("Bravo, tu es le meilleur")
print(Style.RESET_ALL) # permet de stopper la coloration des prints
print(Fore.LIGHTYELLOW_EX + "Bravo !" + Style.RESET_ALL) # pour stopper la coloration directement
'''

'''
# On se demande si replace s'arrete à la première occurence trouvée :
s = "n\n\n<!DOCTYPE html>\n<html lan"
s2 = s.replace("n", "x").replace("\n","---")
print(s2)
'''

print("Bon...")
time.sleep(10)
print("...jour")