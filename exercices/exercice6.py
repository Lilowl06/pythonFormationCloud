'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins un caractères spécial (/;|%, etc.)
La longeur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 6 : Générateur de mot de passe ***")

import random
import string

def makePassWord():
    try :
        lenPassWord = int(input("Veuillez choisir un nombre entier correspondant à la taille du mot de passe ? La taille minimale est de 4 "))
    except ValueError :
        print("=> Erreur : la valeur saisie n'est pas un entier !")
        exit()

    if lenPassWord > 4 :
        # Liste de différents types de caractères :
        upperLetters = [chr(index) for index in range(65,91)] # string.ascii_lowercase
        lowerLetters = [chr(index) for index in range(97,123)] # string.ascii_uppercase
        numbers = [str(i) for i in range(10)] # string.digit
        specialCharacters =["!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","{","|","}","~"] 
        # string.ascii.punctuation

        tmpPassWord = ""
        for i in range(lenPassWord-4):
            tmpPassWord += random.choice(upperLetters+lowerLetters+numbers+specialCharacters)

        tmpPassWord = tmpPassWord + random.choice(upperLetters) + random.choice(lowerLetters) + random.choice(numbers) + random.choice(specialCharacters)
        tmpPassWord = list(tmpPassWord)
        random.shuffle(tmpPassWord)
        passWord = "".join(tmpPassWord)
        return passWord

    else :
        print("=> Erreur : le chiffre saisi est  inférieur à 4 !")

print(makePassWord())