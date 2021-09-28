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

# Attention, il faut garder le moins de chose possible dans les blocs try et except afin que si une erreur si produise je sache de quoi ca vient. Donc 
# il faudrait n'avoir que la ligne request dans le try !

'''Correction
import time, datetime
import requests
import sys

startTime = time.time() # donne le temps écoulé depuis janvier 1970. Permet de prendre ca comme un chronomètre, qui calcule le temps depuis 
le début de la fonction
logFilePath = "health.log" 

# ToDo : vérifier que les arguments ont été fournis à la commande et qu'ils sont acceptables (convertibles en int)
sleepTime = int(sys.argv[1])
maxTime = int(sys.argv[2]) # temps d'éxécution maximale du script # permet de géré les scriptes sans intervention humaine !

with open("websites.txt", "r") as sites :
    websites = sites.read().splitlines()

while True:
    logFile = open(logFilePath, "a")
    for w in websites:
        newLogLine = ""
        newLogLine += str(datetime.datetime.now()) + " " + w + " "
        print(newLogLine)
        try:
            response = requests.get(w)
            newLogLine += str(response.status_code)
        except:
            newLogLine += "error when requesting the website"
        logFile.write(newLogLine + "\n")
    logFile.close()
    time.sleep(sleepTime)
    if time.time() - startTime > maxTime:
        break
'''