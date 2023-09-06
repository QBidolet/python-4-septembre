"""
Exercice3
Il faut créer un programme qui affiche les 20 premiers
 termes de la table de multiplication de 7.
 Utiliser la notion de fonction.
Bonus : Pouvoir rendre variable le nombre de termes
et la table choisie.x
"""


def generer_table_multiplication(table=5, nombre_terme=20):
    for nombre in range(1, nombre_terme + 1):
        print(f"{table} X {nombre} = {table * nombre}")


generer_table_multiplication(table=5, nombre_terme=20)
