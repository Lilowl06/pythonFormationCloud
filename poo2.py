class Email :
    _body = "" # corps du message / l'ajout de _ devant body permet de changer la visibilité du champ body
    __dst = "" # destinataire de l'email

    # Méthode de construction ou constructeur : il s'execute automatiquement au moment de l'instanciation !
    def __init__(self, body, dst) :
        # print("constructeur exécuté!")
        self._body = body
        self.__dst = dst

    # Méthodes
    def getBody(self):
        return self._body
    
    def getDst(self):
        return self.__dst
    
    def setBody(self, body) :
        self._body = body
    
    def setDst(self, dst) :
        self.__dst = dst


# email1 = Email() # instanciation, ne fonctionne plus pour instancié s'il y a un cosntructeur car il manque les arguments
email1 = Email("Cio", "toto@nada.es")
'''email1.body = "Bonjour, ..." # que l'on mette le _ ou pas la déclaration de la variable et le print fonctionne.
# car le simple _ rend l'attribu protected (accessible depuis l'extérieur directement sans passer par un getter et ce sera une propriété héritée,
#  visible par un héritié). Le simple _ ne joue pas et ne change pas le nom de la variable, il ajoute seulement une propriétée au champ.
print(email1.body)
print(email1.getBody())'''
# email1.setBody("Bonjour, ...")
# print(f"Corps du message : {email1.getBody()}")
print(email1.getBody())

''' Attention à cette commande
email1.dst = "destinataire@blabla.fr" # la propriétée à été dynamiquement greffé, ajout d'une nouvelle propriétée qui n'est pas inné à la classe.
# Donc la classe est violable et c'est source d'erreur de bug !!
print(email1.dst)'''

# print(email1.dst) # erreur quand il y a le double _ devant le nom dst du champ car le champ est privé !
#email1.setDst("destinataire@blabla.fr")
#print(f"Destinataire du message : {email1.getDst()}") # par contre par un getter ca fonctionne, car il est défini dans la classe !
print(email1.getDst())