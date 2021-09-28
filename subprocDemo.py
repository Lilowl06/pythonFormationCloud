import subprocess

# python peut servir de glue entre différents programmes car il peut les ouvrir.

'''Recours à un sous processus qui n'est pas en interne au programme'''

''' Permet d'exécuter une commande bash ici ls en python
subprocess.run(["ls", "-l", "-a"]) 
Je souhaite exécuter le sous process dont je vais te donner le nom en entrée. Il peut accepter une chaine de caractère ou une liste en premier argument 
La liste d'arguments = commande + arguments (ici option de ls))
ou subprocess.run(["ls", "-la"])
ou subprocess.run("ls -la", shell=True) " permet de dire à python d'interpréter cette commande comme si c'était une commande shell
'''


''' Si on veut que le process soit dans une variable :
Par rapport à la commande os qui va déterminer dans quel environnement de travail nous nous trouvons (linux ou windows, etc...) La commande subprocess, elle 
est plus sensible. Il va falloir lui fournir les bonnes commandes selon l'environnement de travail.
out = subprocess.run(["ls", "-la"]) # si je mets juste ca, il y a une commande de sortie par défaut dans le terminal.
out = subprocess.run(["ls", "-la"], capture_output=True) # avec cette commande, je préviens que la capture ne doit pas être dans le terminal
print(out) # la sortie de l'exécution ls est ajouté à un objet. out n'est pas seulement que ls mais un objet contenant la réponse de ls
print(out.args) # permet d'afficher les arguments à l'origine du subprocess.
print(out.returncode) # ce veut dire que ca c'est bien passé !
print(out.stdout) #c'est moche comme sortie
print(out.stdout.decode()) # decode() => byte => str, permet d'avoir une sortie jolie
'''


'''
# Si je veux mettre ma sortie standard dans un fichier :
with open("files/output.txt", "w") as f :
    out= subprocess.run(["ls", "-la"], stdout=f, text=True)
'''


# out= subprocess.run(["lsp", "-la"], capture_output=True, stderr=subprocess.DEVNULL, text=True) # on a quand même une erreur dans le terminal, 
# ce que l'on veut enlever !
# l'utilisation de capture_output est exclusif. On ne peut pas utiliser stderr ou stdout. Ce sera soit l'un soit l'autre.
# print(out.stderr)
# DEVNULL est une constante présente dans le package subprocess, permet de rediriger l'erreur standard dans la nature, dans le vide pour la perdre.

# Comment faire pour que les deux ne n'exclu pas ?
# out= subprocess.run(["lsp", "-la"], stderr=subprocess.DEVNULL) # l'erreur ne provient pas par le programme en lui même mais au niveau du bash,
# donc du process parent ! Donc capter l'erreur standard n'aura pas de conséquence, car ce n'est pas la commande qui fait l'erreur.

# On va donc tester avec une erreur qui pourra être rediriger :
# out = subprocess.run(["ls", "-la", "-z"], stderr=subprocess.DEVNULL) # rien dans la sortie standard, car la commande n'a pas produit de sortie standard.
# Car elle s'est branchée sur la sortie erreure.
# print(out.stderr) # None
# print(out.stdout) # None
# out = subprocess.run(["ls", "-la", "-z"], capture_output=True, text=True) # si je ne mets pas de print, on ne sait pas qu'il y a eu une erreur.
# print(out.stderr) # capture de la sortie d'erreur qui a été stocké dans la variable stderr
# print(out.returncode) # c'est != de 0 ; donc une erreur c'est produit !
'''if out.returncode != 0 :
    print("La commande a échoué")'''

# equivalent à ls -la -a 2> /dev/null
# https://www.cyberciti.biz/faq/linux-redirect-error-output-to-file/
# out = subprocess.run(["ls", "-la", "-z"], stderr=subprocess.DEVNULL, text=True)

sp1 = subprocess.run(["cat", "students.txt"], capture_output=True, text=True)
# print(sp1.stdout)
# équivalent à cat student.txt | grep "la"
sp2 = subprocess.run(["grep", "la"], capture_output=True, input=sp1.stdout, text=True)
# print(sp2.stdout)
# en une ligne :
# sp3 = subprocess.run("cat students.txt | grep la", shell=True)


# Toute exécution d'un programme crée un processus (un processus est un programme en cours d'exécution -- vu avec top ou htop)
# Un processus children (child process) peut avoir un processus parent (parent process). Quand un process parent est kill, ca kill les enfants mais l'inverse
# n'est pas vrai. Quand l'enfant est kill, le parent reste en fonction.


'''
Toute exécution d'un programme crée un processus (un processus est un programme en cours d'exécution -- vu avec top ou htop)
Un processus children (child process) peut avoir un processus parent (parent process). Quand un process parent est kill, ca kill les enfants mais l'inverse
n'est pas vrai. Quand l'enfant est kill, le parent reste en fonction.


Un processus a une entrée standard (sdtin = 0). Le processus peut faire de la sortie (sortie standard du processus, stdout = 1 ; ex. ls -la 1> o.txt 
ou ls -la> o.txt) et s'il y a une erreur ce sera la sortie d'erreur (ou stderr = 2 ; ex. ls -la -z 2> err.txt).
La sortie d'un processus peut être l'entrée d'un autre (|).
Quand un programme return 0 c'est qu'il n'y a pas eu d'erreur. Quand il return un 2, alors c'est la sortie erreur.
Ex : command1 > out.txt 2> err.txt : ca veut dire que si la commande est bonne je redirige vers un fichier out.txt et s'il y a une erreur, je redirige vers
le fichier err.txt
Ex : ls -laz > tutto.txt 2>&1 : cette commande redirige soit la sortie soit l'erreur dans le même fichier.
Ex : ls-laz 2> /dev/null : permet de perdre l'erreur produite dans le néant.
'''
