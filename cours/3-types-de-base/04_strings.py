# Escape avec \
print('J\'ai 29 ans.')

# Combiner avec +
prenom = "Quentin"
nom = "BIDOLET"
print(prenom + " " + nom)

# Je veux écrire la phrase :
# Je m'appelle Quentin BIDOLET.

# simple
phrase = "Je m'appelle " + prenom + " " + nom + "."
print(phrase)

# version python 2
ma_phrase = "Je m'appelle %s %s." % (prenom, nom)
print(ma_phrase)

# version pythonic
ma_phrase = f"Je m'appelle {prenom} {nom}."

# Duppliquer avec #.
print('#'*25)

# Extraction de chaine de caractère avec [ ].
alphabet = "abcdef"
# [start:end:step]
print(alphabet[0])
# end non inclus.
print(alphabet[0:2])

# tout sélectionner
print(alphabet[:])

# sélectionner à partir d'un indice.
print(alphabet[2:])

# sélectionner jusqu'à un indice (non inclus)
print(alphabet[:2])

# extraire la chaine de deux en deux.
print(alphabet[::2])

# lire à l'envers
print(alphabet[::-1])

# indice négatif, parce exemple -2 en partant de la fin
print(alphabet[:-2])