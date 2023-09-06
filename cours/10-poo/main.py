from voiture import Voiture
from voiture_de_course import VoitureDeCourse

voiture = Voiture("Vert", "Tesla")
voiture_2 = Voiture()
if voiture == voiture_2:
    print("Ce sont les mêmes voitures.")
else:
    print("Les voitures sont différentes.")


voiture = VoitureDeCourse("Blanche", "Mercedes", 250)
print(voiture)
