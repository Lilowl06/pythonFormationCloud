title = "Les Trois Mousquetaires"

'''
for letter in title : # une liste de caractères est itérables
    print(letter)
'''

# print(title[0]) Renvoie la première lettre de la string, ici "L"
# title[0] = 'D' # error : 'str' object does not support item assignment
# Les chaînes de caractère sont des éléments parcourables qu'en lecture et non en écriture

'''
for letter in title[0:10]: #attention le 0 est inclus dans la borne, et 10 est exclu !
    print(letter)
'''

'''
for letter in title[:11]: #attention le 0 est inclus dans la borne, et 10 est exclu !
    print(letter)
'''

word = ""
for letter in title[4:9] :
    word += letter
print(word)

cmpOccurences = 0
searchedLetter = 'a'
for letter in title :
    if letter == searchedLetter :
        cmpOccurences += 1
print("La lettre '%s' a été trouvée %s fois dans le titre : %s" % (searchedLetter ,cmpOccurences, title))