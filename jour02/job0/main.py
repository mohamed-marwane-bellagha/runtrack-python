class Personne():

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def Sepresenter(self):
        print("Bonjour ",self.prenom)
    def setnom(self):
        self.nom=input("Entrer votre nom:")

    def setprenom(self):
        self.prenom = input("Entrer votre prenom:")
# Personne.setnom("caca")

# Personne.setprenom("caca")
P1 = Personne("toti", "totoy")
P1.Sepresenter()