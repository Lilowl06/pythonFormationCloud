'''
*** Exo 1 ***
Demander à l'utilisateur de saisir un chiffre
Si le chiffre saisi est supérieur à guess_number
on affiche "c'est moins"
Si le chiffre saisi est inférieur à guess_number
on affiche "c'est plus"
Si le chiffre saisi est égal à guess_number
on affiche "Bravo, tu as deviné !"
'''
print("*** EXO 1: chiffre mystère à deviner ***")
guessNumber = 42

# votre code ici
playerInput = int(input("Veuillez saisir un chiffre ? "))
if playerInput > guessNumber : 
    print("C'est moins")
elif playerInput < guessNumber : 
    print("C'est plus")
else : 
    print("Bravo, tu as deviné !")

'''
# correction :
playerInput2 = int(input("Saisir un chiffre : "))
if playerInput2 == guessNumber :
    print("Bravo, tu as deviné !")
else :
    if playerInput2 > guessNumber :
        print("C'est moins !")
    else :
        print("C'est plus !")
'''
