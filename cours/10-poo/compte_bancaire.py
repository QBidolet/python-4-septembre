"""
Définissez une classe CompteBancaire(),
 qui permet d’instancier des objets tels que compte1, compte2, etc.
Le constructeur de cette classe initialisera
deux attributs d’instance nom et solde,
avec les valeurs par défaut ’Dupont’ et 1000.
Trois autres méthodes seront définies :
• depot(somme) permettra d’ajouter une certaine somme au solde ;
• retrait(somme) permettra de retirer une certaine somme du solde ;
• afficher sa représentation en string qui affichera le nom
du titulaire et le solde de son compte.
"""

class CompteBancaire:
    def __init__(self, nom="Dupont", solde=1000):
        self._nom = nom
        self._solde = solde

    def deposer(self, somme):
        if somme > 0:
            self._solde += somme
        else:
            print("Vous ne pouvez ajouter une somme "
                  "inférieur ou égal à zéro.")

    def retirer(self, somme):
        if somme >= 0:
            self._solde -= somme

    def __str__(self):
        return f"Compte bancaire de {self._nom}.\n" \
               f"Solde : {self._solde}."

