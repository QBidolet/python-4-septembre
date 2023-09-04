# Fonction print.
print("Hello World!")

# Séparateur
print("Hello", "World!", sep="-")

# Fin print
print("Hello", "World!", end="\n")
print("Hello", "World!", end="\n")

# Notons qu'on peut écrire une chaine de caractère
# en guillemet simple.
print('Hello "Quentin"')
print("Hello 'Quentin'")

quentin = "Quentin"
bidolet = "BIDOLET"

# Façon 1
print("Je suis {0} {1}.".format(quentin, bidolet))

# Façon 2
print("Je suis " + quentin + " " + bidolet + ".")

# Façon 3
print(f"Je suis {quentin} {bidolet}.")

# Echapper un caractère (escape).
print('J\'ai 29 ans.\nDeuxième ligne.')

# Retour à la ligne dans le string.
print('J\'ai 29 ans.\n' + \
      'Deuxième ligne.')
