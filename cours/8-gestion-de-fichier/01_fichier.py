# 4 modes d'ouvertures
# w : pour écrire et écraser le contenu
# (crée le fichier si inexistant)
# r : pour lire
# x : pour écrire seulement si le fichier est inexistant.
# a : pour ajouter à la suite.

# Méthode classique d'ouverture de fichier.
fichier = open("mon_fichier.txt", "a")
fichier.write("Hello print!")
fichier.close()

# Méthode pythonic
with open("mon_fichier.txt", "r") as fichier:
    # fichier.write("Hello with!")
    contenu = fichier.read()
    print(contenu)


