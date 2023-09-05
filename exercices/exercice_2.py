"""
Écrivez un programme qui recherche le plus grand élément
présent dans une liste donnée.
Par exemple, si on l'appliquait à
la liste [32, 5, 12, 8, 3, 75, 2, 15],
ce programme devrait afficher : 75.
Contraintes : Ne pas utiliser les fonctions, min, max, sort etc.
"""

ma_liste = [32, 5, 12, 8, 3, 75, 2, 15]

if ma_liste:
    max = ma_liste[0]
    for nombre in ma_liste:
        if nombre > max:
            max = nombre
    else:
        print(f"Le maximum est {max}.")
else:
    print("Veuillez fournir une liste non vide.")