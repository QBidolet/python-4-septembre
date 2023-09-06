from compte_bancaire import CompteBancaire
# from voiture import Voiture
# from voiture_de_course import VoitureDeCourse
#
# voiture = Voiture("Vert", "Tesla")
# voiture_2 = Voiture()
# if voiture == voiture_2:
#     print("Ce sont les mêmes voitures.")
# else:
#     print("Les voitures sont différentes.")
#
#
# voiture = VoitureDeCourse("Blanche", "Mercedes", 250)
# print(voiture)

compte_bancaire = CompteBancaire("BIDOLET", 1000000)
compte_bancaire.retirer(700000)
print(compte_bancaire)
compte_bancaire.deposer(250000)
print(compte_bancaire)
compte_bancaire.deposer(10.5)
print(compte_bancaire)
compte_bancaire.retirer()
