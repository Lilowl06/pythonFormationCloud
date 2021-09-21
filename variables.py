# Variables primitives
''' bloc comment (commentaire de bloc)
training = "Initiation au langage Python"
temperature = 15.6
'''

training = "Initiation au langage Python"
temperature = 15
pi = 3.14
isEarthRound = True

print(type(training)) # <class 'str'>
print(type(temperature)) # <class 'int'>
print(type(pi)) # <class 'float'>
print(type(isEarthRound)) # <class 'bool'>
#print (training)

# Opération sur les variables
print(temperature+10) # addition - on peut aussi utiliser - ; / ; * ; etc.
print(training+" 10") # concatenation
print(pi +10)
print(isEarthRound + 10 ) # on peut additionner le booleen à 10 car False vaut 0 et True vaut 1
                            # conduit implicitement Python a convertir le booléen en int

print("Le double de pi est : " + str(pi*2)) # permet de faire l'opération pi*2 et ensuite de convertir explicitement en string.
doublePi = str(pi*2)
triplePi = str(pi*3)
print("Le triple de pi est : " + triplePi)
print("Le triple de pi est :", pi*pi) # usage de print en multi-arguments --> convertion implicite