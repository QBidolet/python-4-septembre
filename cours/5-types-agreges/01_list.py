une_liste = ["pomme", "banane", "kiwi"]
print(une_liste)

une_liste = [
    "pomme", 1.0, True, ["kiwi"], [],
]
print(une_liste)

# sélection avec un indice
print(une_liste[0], type(une_liste[3][0]))

# ajouter
une_liste.append("Hello")
print(une_liste)
une_liste.insert(0, "Hello")
print(une_liste)
print(une_liste.count("Hello"))

# supprimer un élément
del une_liste[0]
print(une_liste)
une_liste.remove("Hello")
print(une_liste)

# gestion mémoire
a = [1, 2, 3, 4]
b = a
a[0] = 0
print(a, b)

# test d'appartenance
if 0 in a:
    print("0 est dans a.")

# parcours
for element in a:
    print(element)

# trie
a = [5, 9, 4, 0, 3]
a.sort(reverse=True)
print(a)