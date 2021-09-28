import platform, os

from colorama.ansi import Style
import tools
import mypackage.subpackage.subdemo as sd
from colorama import *
import time
import sys

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

'''
print("Bon...")
time.sleep(10)
print("...jour")
'''


'''print(sys.argv) # argv est une liste d'arguments de la commande inclu
# python3 demo.py toto tata
# Cette ligne return avec print(sys.argv) --> ['demo.py', 'toto', 'tata']
# Ils sont automatiquement mis dans la liste et donc ils sont indexé et récupérable via leurs indexs.
for a in sys.argv():
    print(a)'''

while True : #ici pas de sortie de boucle, donc boucle infini. Python print("coucou") ici est un processus enfant du processus Bash qui permet de lancer 
    # python en ligne de commande
    print("Coucou")
    time.sleep(5)
# je vais chercher dans le top, l'identifiant du programme --> python3 demo (id = 6927) et le kill. Ce qui a pour effet d'arrêter la boucle.
# Si je ferme la fenêtre bash, donc je tue bash, ca kill la boucle aussi car ca tue les enfants.
# Tous processus enfant qui continu à vivre quand le parent est mort : on dit qu'il est démonisé (daemon) ou orphelin