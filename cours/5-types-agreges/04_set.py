# Ensemble désordonné sans doublon.

prenoms = {
    "Quentin",
    "Julien",
    "Pierre"
}

# Ajouter un éléments
prenoms.add("Romain")
prenoms.add("Romain")
prenoms.add("Romain")
print(prenoms)

# Supprimer
prenoms.remove("Romain")
print(prenoms)

# Parcourir
for prenom in prenoms:
    print(prenom)

# Cas d'utilisation
ma_liste = [1, 2, 3, 3, 4, 5, 6, 6, 6]
sans_doublon = set(ma_liste)
print(sans_doublon)
