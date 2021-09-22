# Script créateur de fichiers dynamiques dans le dossier cible

# Comment créer un fichier en python :
'''
f = open("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/blabla.txt", "r") # la fonction open retourne quelque chose.
# Donc il faut stocker son retour dans une variable (l'adresse du début de fichier)
print(f.read()) # <class _io.TextIOWrapper name='/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/blabla.txt' mode='r' encoding='UTF-8'>
# f est un objet complexe
f.close()
'''

'''
f = open("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/blabla.txt", "a") # permet de faire de l'écriture mais on ne peut pas écraser
# le contenu actuel, seulement ajouter au fichier (append)
f.write("J'existeDonc je suis")
f.close
'''

'''
f = open("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/blabla.txt", "w")
f.write("J'existe, donc je suis")
f.close
'''

# Pour créer un fichier :
'''
f = open("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/test.txt", "w") # si l'on fait ca sur un fichier existant, il n'y a pas d'erreur
# préventive et cette option écrase le fichier. L'option "a" permet aussi de créer un fichier avec la même contrainte que "w"
f.write("Simple fichier test")
f.close()
'''

'''
f = open("/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/test.txt", "x") # si l'on fait ca sur un fichier existant, il y a une erreur
# afin de ne pas écraser involontairement le fichier. C'est à privilégier
f.write("Simple fichier test")
f.close()
'''

from random import randint
import os

def getRandomValue(l) : #fonction qui renvoie une valeur aléatoire sur la base de la liste donnée en entrée
    randIndex = randint(0, len(l)-1)
    return l[randIndex]


numFiles = 10 # nombre de fichier à générer (on peut aussi mettre un input pour rendre ca hyper flexible)
fileNames = ["script", "demo", "example", "test", "new"]
extensions = ["txt", "log", "json", "js", "exe"] # les différentes extensions possibles
targetDir = "/home/alyssia/Documents/vsCodeProject/pythonFormationCloud/files/" # le dossier cible dans lequel iront les fichiers

# print(getRandomValue(fileNames)) # test du bon fonctionnement de la fonction

'''
# Exemple concret : renommer des fichiers de photos qui aurait un nom affreux, par exemple ! On peut utiliser les scripts à des fin personnel.
for x in range(numFiles) :
    filename = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
    # print(filename) # test de l'état actuel du script, problème : il peut créer plusieurs fois le même nom !
    f = open(filename, "w") # on expérimente en w mais on va écraser s'il y a des doubles. 
    # On ne met rien dans les fichiers car selon l'extension, le contenu sera différent.
    # f = open(filename, "x") # erreur car il y a déjà un fichier existant.
    f.close()
    print("Création du fichier %s" % filename)
'''

# Nouvelle fonction avec l'ouverture en mode "x", afin d'apprendre à générer les erreurs avec Python Try Except !
# les mots clés sont try, except, finally

# Avant de créer les fichiers, il faut vérifier que le dossier cible existe ou le créer !
# Mais comment ?
# print(os.path.isdir(targetDir)) # il répond False si il n'existe pas et True s'il existe

# Donc on va pouvoir avancer sur ce problème et le régler
dirExists = os.path.isdir(targetDir)
if not dirExists : # ou if not os.path.isdir(targetDir) sans créer une variable inutile
    print("Le dossier cible '%s' n'existe pas" %targetDir)
    try :
        os.mkdir(targetDir)
        print("Le dossier cible '%s' a été créé" %targetDir)
    except :
        print("Impossible de créer le dossier cible '%s'" %targetDir)
        # on peut mettre un 'exit' pour faire une sortie gracieuse avec un joli print verbeux
        # et pas une sortie disgracieuse le programme crash.
        exit()

# Création des fichiers :
for x in range(numFiles) :
    filename = targetDir + getRandomValue(fileNames) + "." + getRandomValue(extensions)
    print("\nTentative de création du fichier %s" % filename)

    try : # essaye d'ouvrir et de fermer de fichier
        f = open(filename, "x")
        f.close()
        print("=> Succès ! Création du fichier %s" % filename)
    except FileExistsError : # s'il y a une erreur, j'apporte ma solution dans ce bloc
        # print("=> Erreur ! Le fichier n'a pas pu être créé") # ce n'est pas très clair comme print, on pourrait être plus fin
        # et dire que le fichier a déjà été crée, en décidant de réagir à une exception précise. Je trouve le nom de l'erreur dans la doc de l'ouverture 
        # en mode x (ou en expérimentant).
        print("=> Le fichier existe déjà")
    except :
        print("=> Erreur !")


# Avec la gestion des erreurs, le programme ne crash plus mais afin le message problème et crée les fichiers qu'il peut créer plutôt que de s'arrêter

# En supprimant le targetDir est en essayant le script, il n'y a pas de détaile d'erreur. On voit seulement que le fichier n'a pas pu être créé.
# Donc si l'on commente le bloc try - except. On retrouve de nouveau l'erreur, qui est un FileNotFoundError ! Donc avant de tenter d'écrire dans 
# le targetDir, il serait préférable de vérifier s'il existe et s'il n'existe pas le créer.