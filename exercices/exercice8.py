'''
*** EXO 8: Health Check *** (permet de vérifier qu'une application ou serveur web répond (le status code renvoyé))
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond (status code avec requests)
à raison d'une requête toutes les n secondes (avec du .append "a" pour ne pas écraser. périodicité avec un module nommé time, la fonction sleep permet de
bloquer l'utilisation du programme pendant n secondes.)
la périodicité sera fournie en entrée par l'utilisateur (input : Tout les combien de temps voulez-vous check les sites web")
On produira en sortie un fichier de log ('healthCheck.log') qui contiendra :
    - la date de la requête de vérification
    - l'url interrogée
    - le status code obtenu ou une indication d'erreur en cas de non réponse
'''
"Boucle infini avec while true et l'isntruction break, check sur 5min ou s'autostop sur une certaine échéance"

print("*** EXO 8: Health Check ***")

# votre code ici
import requests as req
import datetime
import time

maxTime = int(input("Durant combien de temps voulez-vous vérifier la réponse des sites web ? (temps en seconde) "))
periodicTime = int(input("A quelle fréquence voulez-vous effectuer cette vérification ? "))
totalTime = 0
cmpCheck = 0
while True :
    if totalTime < maxTime :
        with open("files/websites.txt", "r") as webSites :
            lines = webSites.read().splitlines()
            for site in lines :
                try :
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    response = req.get(site)
                    with open("files/healthCheck.log", "a") as logFile :
                        logFile.write(str(date) + " " + site + " " + "Status code : " + str(response.status_code) + "\n")
                except :
                    with open("files/healthCheck.log", "a") as logFile :
                        logFile.write(str(date) + " " + site + " " + "Status code : ERREUR, pas de réponse " + "\n")
        print(f"La vérification n°{cmpCheck+1} a été effectuée, il reste {round((maxTime-totalTime)/60,2)} minutes de vérification")
        cmpCheck += 1
        time.sleep(periodicTime)
        totalTime += periodicTime
    else :
        print(f"Le temps est écoulé. Il y a eu {cmpCheck} vérification.")
        break