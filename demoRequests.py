import requests as req

response = req.get("https://pypi.org/project/requests/") # donne 200
# response = req.get("https://pypi.org/project/requests/fssdfdd") # donne 404, non trouvée

print(response) # <Response [200]> # la réquête c'est produit avec succès.
# print(type(response)) # <class 'requests.models.Response'> objet de la classe réponse
print(response.status_code)
# print(response.content) # body de la page web, donc le code HTML

# body = response.content # réponse du contenu de la page HTML
# print(type(body)) # <class 'bytes'> la réponse est de type bytes.
# On essaye de convertir notre réponse du coup
body = str(response.content)

# print(type(body))
# on veut supprimer les \n du corps body, donc enlever les sauts de ligne.
body.replace("\\n", "") # ne fonctionne pas, certainement car dans la conversion str, il y a eu des caractères parasites qui ont été rajoutés.

with open("response.html", "w") as f : # création d'un fichier contenant le contenu du body HTML.
    f.write(body) # c'est comme si on téléchargeait la page.

print("Page téléchargée") # pour voir la page correctement, il suffit de clique droit --> mettre le document en forme pour avoir une vision en forme html
# du code.


