from voiture import Voiture

class VoitureDeCourse(Voiture):
    def __init__(self, couleur="Rouge", marque="Tesla", vitesse=200):
        Voiture.__init__(self, couleur, marque)
        self._vitesse = vitesse

    def get_vitesse(self):
        return self._vitesse

    def __str__(self):
        return f"Je suis une voiture de course {self._marque} " \
               f"de couleur {self._couleur} et de vitesse {self._vitesse}."
