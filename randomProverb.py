proverbs = [
    "Il ne faut pas vendre le peau de l'ours avant de l'avoir tué",
    "Omnia labor vincit", #entre dire et faire, il y a entre deux la mer
    "Tra il dire e il fare c'è in mezzo il mare",
    "Ad astra per aspera" # c'est par la difficulté que l'on obtient la gloire
    "An apple a day keeps the doctor away"
    "Un tiens vaut mieux que deux tu l'auras"
]

# On veut que quand on excute ce fichier, avoir de manière aléatoire un des proverbes de la liste
from random import randint

indexMax = len (proverbs) -1
randomIndex = randint(0, indexMax)
print(proverbs[randomIndex])
# print(proverbs[0])

# Randint est très utilisé dans la génération aléatoire de mdp, lors de la création d'utilisateur