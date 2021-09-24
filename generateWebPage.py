template = '''
<!DOCTYPE html>
<html>
    <head>
        <title>[name]</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>[name]</h1>
        <p>Vous avez obtenu la note de [note] sur 20.</p>
    </body>
</html>
'''

# Ce qui nous intéresse ici c'est le côté automatique et massive.
# Si j'ai un ensemble d'étudiant à qui j'ai fourni des notes.
# Pour chacun de mes étudiants je veux mettre en ligne et produire les ressources pour le faire.
students = [
    {"name": "Sébastien", "note": 16},
    {"name": "Pamela", "note": 19.5},
    {"name": "Aude", "note": 17}
]

# On va itéré sur les étudians et créer une page html qui contient le nom et la note.
for s in students :
    filepath = "files/" + s["name"].lower().replace("é","e") + "_note.htlm"

    content = template.replace("[name]", s["name"]).replace("[note]", str(s["note"]))
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Fichier HTML généré pour l'étudiant {s['name']}")


#with open("simplePage.html","w") as f :
#    f.write(html)
# dans head --> title --> ce sont les titres des onglets

