# POO : Programmation Orientée Objet

class Student :
    # champ ou attribut
    # visibiilité public par défaut
    firstname = "xxx"
    lastname = "yyy"
    email = "test@test.com"
    member = True # membre dans l'établissement

    # Methode = focntion défini à l'intérieur d'une classe.
    def getFirstName(self) : # toujours mettre self si on doit créer une méthode de classe !
    # permet lors de l'instantiation a partir de la classe de résoudre certain appel.
        return self.firstname
    
    def getLastName(self) :
        return self.lastname
    
    def getFullName(self) :
        return self.firstname + "" + self.lastname
    
    def getInitials(self):
        return (self.firstname[:1] + self.lastname[:1]).upper()
    
    # Méthode d'accès en écriture aux propriétés des champs ciblées (setters)
    def setFirstName(self, fisrtname) :
        self.firstname = fisrtname
        return self.firstname # sinon la méthode return None

    def setLastName(self, lastname) :
        self.lastname = lastname
        return self.lastname # sinon la méthode return None    

    def unsubscribe(self):
        self.member = False


# Tant que la classe n'est pas instanciée, elle ne fait rien

student1 = Student() # Instancie la classe Student
student2 = Student()
student3 = Student()
# print(type(student1)) # <class '__main__.Student'> # c'est un objet appartenant à la classe
student1.setFirstName("Roberto")
student1.setLastName("Baggio")

student2.setFirstName("Lucas")
student2.setLastName("Blanco")

student3.setFirstName("Alessandro")
student3.setLastName("Nesta")

print(student1.firstname)
print(student2.getFirstName()) # accès via l'exécution d'une méthode.
print(student2.getFullName())
print(student3.getInitials())

student1.unsubscribe()

if student1.member:
    print(student1.getFullName(), "est membre de l'établissement")
else :
    print(student1.getFullName(), "n'est plus membre de l'établissement")