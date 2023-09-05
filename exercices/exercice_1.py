"""
Vous devez écrire un programme qui demande à l'utilisateur de saisir une vitesse en miles/heure
 et vous devez afficher cette vitesse en km/h et m/s
Vous devez également réinviter votre utilisateur à saisir une valeur une fois
la conversion terminé et boucler de cette façon
Indication pour la conversion : pour passer des miles/heure au mètre par seconde il faut diviser par 2.237
Indication pour la conversion : pour passer des miles/heure au km par heure il faut multiplier par 1.609
"""
continuer = "oui"
while continuer == "oui":
    vitesse_mh = float(input("Veuillez saisir une vitesse en miles/heure.\n"))
    vitesse_kmh = vitesse_mh * 1.609
    vitesse_ms = vitesse_mh / 2.237
    print(f"Vitesse en km/h: {vitesse_kmh}")
    print(f"Vitesse en ms: {vitesse_ms}")
    continuer = input("Voulez-vous continuer ? (oui/non)").lower()

