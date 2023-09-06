class Voiture:
    def __init__(self, couleur="Rouge", marque="Tesla"):
        self._couleur = couleur
        self._marque = marque

    def klaxonner(self):
        print("tut tut")
        # return "tut tut"

    def repeindre(self, couleur):
        self.couleur = couleur

    def changer_marque(self, marque):
        self.marque = marque

    def __str__(self):
        return f"Je suis une voiture de marque " \
               f"{self._marque} et de couleur {self._couleur}."

    def __eq__(self, obj):
        return self._marque == obj._marque