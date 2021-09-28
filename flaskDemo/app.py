from flask import Flask, render_template # import de la classe Flask depuis le module flask

app = Flask(__name__) # instanciation de la classe (pour cela, il faut donner le nom du package dans lequel on travail), 
# __name__ : sert à obtenir le nom du package dans lequel le code est exécuter.
# le fichier app.py n'est pas enpackagé, il n'appartient pas à un package. En l'absence d'un package non définit, le package par défaut sera toujours 
# __main__, la valeur par défaut de __name__.

# print(type(app)) # <class 'flask.app.Flask'>

# Décorateur : s'utilise en appuie de fonction.
# Définir une fonction qui sera exécutée quand un client HTTP enverra une requête (nous nous sommes le serveur)
@app.route("/") # lorsque le client requiera la fonction / sur le serveur, il sera redirigé vers la page d'accueil
def home(): # cette fonction sera déclanchée quand l'utilisateur demandera la page d'accueil, la racine.
    return "Page d'acceuil"

@app.route("/login")
def login():
    content = ''' # c'est méthode n'est pas top, il vaut mieux donner une page
    <!DOCTYPE html>
    <html>
        <head>
            <title>Login</title>
            <meta charset="utf-8">
        </head>
        <body>
        <h1>Identification</h1>
        </body>
    </html>
    '''
    # pour mettre un titre dans mon onglet
    return content # dans la vraie vie, il faudra renvoyer une jolie interface, avec des champs de saisie et autre

@app.route("/page")
def page():
    with open("page.html", "r") as f:
        return f.read()

# pour rendre une page accessible, il faut obligatoirement la rendre accessible à l'aide d'un serveur web.
@app.route("/student")
def student():
    studentData = {"name" :"Aude", "note":17}
    studentName = "Aude"
    return render_template("student.html", s=studentData) # en l'absence de configuration, cette fonction va chercher par défaut un fichier dans le dossier templates dans 
    # le dossier flask et fait un lecture et ouverture du fichier student. Petite nuance : on va pouvoir faire du templating. C'est a dire avoir une
    # structure en dur en concatenation avec des éléments dynamiques (variables).

@app.route("/student/note/xxxx")
def studentNote():
    # route retournant la note obtenue par l'étudiant dont le nom/id sera fournie dans l'URL
    return ""


app.run(host="0.0.0.0", port=8080) # c'est deux informations sont retrouvées dans une situation incalculable DevOps ; 0.0.0.0 (adresse IPV4, adresse sur 
# laquelle notre serveur sera accessible, le 0.0.0.0 est traduit par l'adresse de notre PC) ; toutes machines connectées à un réseau à plein de port à 
# dispoistion (métaphore : comme des portes). On s'adresse à une machine par un port standardisé (mySQL = 3306, bases de données) ; sur un serveur web se 
# sera le 80. Un seul et même port ne peut pas être utilisé par deux processus en même temps. Un serveur web est un processus chargé en mémoire qui tourne 
# en boucle infini, son entrée standard prends une requête et sa sortie standard envoie une réponse.

# Quand on lance le script la : il y a un serveur qui tourne en boucle infini. Ici, c'est un serveur local, seulement accessible sur notre machine.
# Si on va sur l'URL donnée après le ligne Running : on arrive sur notre application web qui dit "page d'accueil".
# En mode de développement, on peut choisir le port que l'on veut.

# Le message d'erreur : err_connection_refused : c'est que le serveur qui doit nous répondre est arrêté.